# Options for nuitka compilation:
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --onefile
# nuitka-project: --include-data-dir={MAIN_DIRECTORY}/resources=resources
# nuitka-project: --output-dir={MAIN_DIRECTORY}/../dist/{OS}/{Arch}
# nuitka-project: --remove-output
# nuitka-project-if: {OS} in ("Windows"):
#   nuitka-project: --msvc=latest
#   nuitka-project: --onefile-windows-splash-screen-image={MAIN_DIRECTORY}/splash.png
#   nuitka-project: --windows-icon-from-ico={MAIN_DIRECTORY}/resources/icon_main.png
# nuitka-project: --deployment

import sys
import os, tempfile

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtWidgets import QMenuBar, QMenu
from PySide6.QtWidgets import QFileDialog, QDialog, QDialogButtonBox, QMessageBox

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QShortcut, QKeySequence, QCloseEvent, QAction, QActionGroup

from ui_form import Ui_jpgearqt

from Gear import Gear
from MplCanvas import MplCanvas
import Units
from helper import is_number, invF, revInvF
import draw
import stress

from math import floor

import numpy as np
from numpy import pi, sin, cos, tan, arcsin, arccos, arctan
from numpy import rad2deg, deg2rad
from numpy import sqrt, zeros, linspace, real
# why isn't this in numpy???
tau = 2*pi

from scipy.optimize import fsolve, least_squares

import matplotlib.pyplot as pyplot
import matplotlib.collections as mcollections
import matplotlib.transforms as mtransforms
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT

import json

###############################################################################
# Use this code to signal the splash screen removal.
if "NUITKA_ONEFILE_PARENT" in os.environ:
   splash_filename = os.path.join(
      tempfile.gettempdir(),
      "onefile_%d_splash_feedback.tmp" % int(os.environ["NUITKA_ONEFILE_PARENT"]),
   )

   if os.path.exists(splash_filename):
      os.unlink(splash_filename)

###############################################################################
class jpgearqt(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "resources/icon_main.png")))
        self.ui = Ui_jpgearqt()
        self.ui.setupUi(self)

        # import icons
        self.good_pixmap = QPixmap(os.path.join(os.path.dirname(__file__), "resources/icon_good.png"))
        self.bad_pixmap = QPixmap(os.path.join(os.path.dirname(__file__), "resources/icon_bad.png"))

        self.createMenu()
        self.connectUI()
        self.setupShortcuts()
        self.setupCanvases()

        # for saving JSON
        self.savePath = ''

        # gear objects
        self.G1 = Gear(1)
        self.G2 = Gear(2)
        self.resetMeshParams()

        self.initGearDesignFields()

# Setup #######################################################################
    def createMenu(self):
        # create menu bar
        menuBar = QMenuBar(self)

        # File Menu
        menuFile = menuBar.addMenu('&File')

        actOpen = menuFile.addAction('Open')
        actOpen.setShortcut(QKeySequence("Ctrl+O"))
        actOpen.triggered.connect(lambda: self.openJSON())

        actSave = menuFile.addAction('Save')
        actSave.setShortcut(QKeySequence("Ctrl+S"))
        actSave.triggered.connect(lambda: self.saveJSON(self.savePath))

        actSaveAs = menuFile.addAction('Save As')
        actSaveAs.setShortcut(QKeySequence("Ctrl+Shift+S"))
        actSaveAs.triggered.connect(lambda: self.saveAsJSON())

        actExportDXF = menuFile.addAction('Export DXF')
        actExportDXF.triggered.connect(lambda: self.exportDXF())

        menuFile.addSeparator()

        actExit = menuFile.addAction('Exit')
        actExit.setShortcut(QKeySequence("Ctrl+Q"))
        actExit.triggered.connect(lambda: sys.exit())

        # Options Menu
        # UI unit labels
        self.unitsList = Units.unitsList
        self.units = self.unitsList[0]

        self.modLabelList = [
            self.ui.lb_targetMod_unit,
            self.ui.lb_mod_unit,
        ]

        self.lengthLabelList = [
            self.ui.lb_targetCD_unit,
            self.ui.lb_CD_bkl_unit,
            self.ui.lb_CD_unit,
            self.ui.lb_Rf_unit,
            self.ui.lb_Rff_unit,
            self.ui.lb_Ro_unit,
            self.ui.lb_Roe_unit,
            self.ui.lb_Romax_unit,
            self.ui.lb_Ros_unit,
            self.ui.lb_Rp_unit,
            self.ui.lb_Rr_unit,
            self.ui.lb_Rrs_unit,
            self.ui.lb_Rs_unit,
            self.ui.lb_Rtip_unit,
            self.ui.lb_Rtipmax_unit,
            self.ui.lb_bkl_unit,
            self.ui.lb_rtcl_unit,
            self.ui.lb_tt_unit,
            self.ui.lb_tts_unit,
            self.ui.lb_FW_unit
        ]

        self.torqueLabelList = [
            self.ui.lb_torque_unit
        ]

        self.pressureLabelList = [
            self.ui.lb_E_unit,
            self.ui.lb_stressB_unit,
            self.ui.lb_stressC_unit
        ]

        self.velLabelList = [
            self.ui.lb_pitchLineVel_unit
        ]

        menuOptions = menuBar.addMenu('&Options')

        menuUnits = menuOptions.addMenu('Units')
        # use an ActionGroup to keep the unit chooses exclusive
        self.groupUnits = QActionGroup(self)
        self.groupUnits.setExclusive(True)

        for i in range(len(self.unitsList)):
            action = self.groupUnits.addAction(self.unitsList[i].lenName + " / " + self.unitsList[i].torqueName)
            menuUnits.addAction(action)
            action.setCheckable(True)
            action.triggered.connect(lambda _, index=i: self.setUnits(index))

            if i == 0:
                action.setChecked(True)

        # add menu to ui
        self.ui.topLayout.insertWidget(0, menuBar)

    def setupShortcuts(self):
        # cycle tabs
        self.SC_cycleTabFW = QShortcut(QKeySequence("PgDown"), self)
        self.SC_cycleTabFW.activated.connect(lambda: self.cycleTab(dir='forward'))
        self.SC_cycleTabRV = QShortcut(QKeySequence("PgUp"), self)
        self.SC_cycleTabRV.activated.connect(lambda: self.cycleTab(dir='backward'))
        # draw gears
        self.SC_drawGear = QShortcut(QKeySequence("Ctrl+D"), self)
        self.SC_drawGear.activated.connect(lambda: draw.drawGear(self, self.G1, _updateAxes=True))
        self.SC_drawGear.activated.connect(lambda: draw.drawGear(self, self.G2, _updateAxes=True))
        self.SC_drawGear.activated.connect(lambda: draw.drawMesh(self, _updateAxes=True))

    def connectUI(self):
        # First tab
        #################
        self.ui.rb_ext_layout.clicked.connect(lambda: self.setType("external"))
        self.ui.rb_int_layout.clicked.connect(lambda: self.setType("internal"))

        self.ui.pb_calcGearSizes.clicked.connect(lambda: self.findGearSizes())
        self.ui.le_pN.editingFinished.connect(lambda: self.updatePinionN())

        # list of layout options
        rb_list = self.ui.bg_layout.buttons()
        for button in rb_list:
            button.toggled.connect(lambda: draw.drawHelper())
        # use layout button
        self.ui.pb_useLayout.clicked.connect(lambda: self.useLayout())

        # Second tab
        #################
        self.ui.rb_ext_design.clicked.connect(lambda: self.setType("external"))
        self.ui.rb_int_design.clicked.connect(lambda: self.setType("internal"))

        self.ui.le_mod.editingFinished.connect(lambda: self.set_mod(self.ui.le_mod.text()))

        self.ui.le_PA_deg.editingFinished.connect(lambda: self.set_PA_deg(self.ui.le_PA_deg.text()))

        self.ui.cb_CD_bkl.currentIndexChanged.connect(lambda: self.swapBklandCD())
        self.ui.le_CD_bkl.editingFinished.connect(lambda: self.updateBklandCD())

        self.ui.le_N1.editingFinished.connect(lambda: self.set_N(self.G1, self.ui.le_N1.text()))
        self.ui.le_N2.editingFinished.connect(lambda: self.set_N(self.G2, self.ui.le_N2.text()))

        self.ui.le_x1.editingFinished.connect(lambda: self.set_x(self.G1, self.ui.le_x1.text()))
        self.ui.le_x2.editingFinished.connect(lambda: self.set_x(self.G2, self.ui.le_x2.text()))

        self.ui.le_Ro1.editingFinished.connect(lambda: self.set_Ro(self.G1, self.ui.le_Ro1.text()))
        self.ui.le_Ro2.editingFinished.connect(lambda: self.set_Ro(self.G2, self.ui.le_Ro2.text()))

        self.ui.le_Rr2.editingFinished.connect(lambda: self.set_Rr(self.ui.le_Rr2.text()))
        self.ui.le_Rrim.editingFinished.connect(lambda: self.set_Rrim(self.G2, self.ui.le_Rrim.text()))

        self.ui.le_Rtip1.editingFinished.connect(lambda: self.set_Rtip(self.G1, self.ui.le_Rtip1.text()))
        self.ui.le_Rtip2.editingFinished.connect(lambda: self.set_Rtip(self.G2, self.ui.le_Rtip2.text()))

        self.ui.le_rtcl1.editingFinished.connect(lambda: self.set_rtcl(self.G1, self.ui.le_rtcl1.text()))
        self.ui.le_rtcl2.editingFinished.connect(lambda: self.set_rtcl(self.G2, self.ui.le_rtcl2.text()))

        self.ui.le_Rf1.editingFinished.connect(lambda: self.set_Rf(self.G1, self.ui.le_Rf1.text()))
        self.ui.le_Rf2.editingFinished.connect(lambda: self.set_Rf(self.G2, self.ui.le_Rf2.text()))

        self.ui.le_FW1.editingFinished.connect(lambda: self.set_FW(self.G1, self.ui.le_FW1.text()))
        self.ui.le_FW2.editingFinished.connect(lambda: self.set_FW(self.G2, self.ui.le_FW2.text()))

        # draw gear button
        self.ui.pb_drawGear.clicked.connect(lambda: draw.drawGear(self, self.G1, _updateAxes=True))
        self.ui.pb_drawGear.clicked.connect(lambda: draw.drawGear(self, self.G2, _updateAxes=True))
        self.ui.pb_drawGear.clicked.connect(lambda: draw.drawMesh(self, _updateAxes=True))
        # single tooth view checkboxes
        self.ui.cb_singleViewG1.checkStateChanged.connect(lambda: draw.drawGear(self, self.G1, _updateAxes=True))
        self.ui.cb_singleViewG2.checkStateChanged.connect(lambda: draw.drawGear(self, self.G2, _updateAxes=True))
        self.ui.cb_singleViewMesh.checkStateChanged.connect(lambda: draw.drawMesh(self, _updateAxes=True))
        # circles checkboxes
        self.ui.cb_circlesG1.checkStateChanged.connect(lambda: draw.drawGear(self, self.G1, _updateAxes=False))
        self.ui.cb_circlesG2.checkStateChanged.connect(lambda: draw.drawGear(self, self.G2, _updateAxes=False))
        self.ui.cb_circlesMesh.checkStateChanged.connect(lambda: draw.drawMesh(self, _updateAxes=False))
        # LoC checkbox
        self.ui.cb_LoC.checkStateChanged.connect(lambda: draw.drawMesh(self, _updateAxes=False))
        # mesh slider
        self.ui.hSlider_Mesh.valueChanged.connect(lambda: draw.drawMesh(self, _updateAxes=False))
        # animate button
        self.ui.pb_animate.clicked.connect(lambda: draw.createAnimWindow(self))

        # Stress tab
        #################
        self.ui.le_RPM.editingFinished.connect(lambda: self.set_RPM(self.ui.le_RPM.text()))
        self.ui.le_torque.editingFinished.connect(lambda: self.set_torque(self.ui.le_torque.text()))
        self.ui.le_E1.editingFinished.connect(lambda: self.set_E(self.G1, self.ui.le_E1.text()))
        self.ui.le_E2.editingFinished.connect(lambda: self.set_E(self.G2, self.ui.le_E2.text()))
        self.ui.le_nu1.editingFinished.connect(lambda: self.set_nu(self.G1, self.ui.le_nu1.text()))
        self.ui.le_nu2.editingFinished.connect(lambda: self.set_nu(self.G2, self.ui.le_nu2.text()))

        # stress button
        self.ui.pb_stress.clicked.connect(lambda: self.updateStress())

    def cycleTab(self, dir='forward'):
        tabs = self.ui.tabW_main

        if dir=='forward':
            newIndex = (tabs.currentIndex()+1) % tabs.count()
            tabs.setCurrentIndex(newIndex)
        elif dir=='backward':
            newIndex = (tabs.currentIndex()-1) % tabs.count()
            tabs.setCurrentIndex(newIndex)

    def setupCanvases(self):
        # layout helper tab
        self.canvasHelper = MplCanvas(self)
        helper_layout = QVBoxLayout(self.ui.f_helper_layout)
        helper_layout.addWidget(self.canvasHelper)

        # gear designer tabs
        # gear 1
        self.canvasG1 = MplCanvas(self)
        self.ui.vLayout_canvasG1.insertWidget(0,self.canvasG1)
        toolbarG1 = NavigationToolbar2QT(self.canvasG1, self)
        self.ui.hLayout_toolbarG1.insertWidget(0, toolbarG1)
        # gear 2
        self.canvasG2 = MplCanvas(self)
        self.ui.vLayout_canvasG2.insertWidget(0,self.canvasG2)
        toolbarG2 = NavigationToolbar2QT(self.canvasG2, self)
        self.ui.hLayout_toolbarG2.insertWidget(0, toolbarG2)
        # mesh
        self.canvasMesh = MplCanvas(self)
        self.ui.vLayout_canvasMesh.insertWidget(0,self.canvasMesh)
        toolbarMesh = NavigationToolbar2QT(self.canvasMesh, self)
        self.ui.hLayout_toolbarMesh.insertWidget(0, toolbarMesh)
        # animation
        # self.canvasAnim = MplCanvas(self)

        # stress
        stress_layout1 = QVBoxLayout(self.ui.tab_stress1)
        self.canvasStress1 = MplCanvas(self)
        stress_layout1.addWidget(self.canvasStress1)
        toolbarStress1 = NavigationToolbar2QT(self.canvasStress1, self)
        stress_layout1.insertWidget(1, toolbarStress1)

        stress_layout2 = QVBoxLayout(self.ui.tab_stress2)
        self.canvasStress2 = MplCanvas(self)
        stress_layout2.addWidget(self.canvasStress2)
        toolbarStress2 = NavigationToolbar2QT(self.canvasStress2, self)
        stress_layout2.insertWidget(1, toolbarStress2)

    def resetMeshParams(self):
        # mesh parameters
        self.mod = -1                   # module
        self.PA_deg = 20                # pressure angle, degrees
        self.PA = deg2rad(self.PA_deg)  # pressure angle, radians
        self.OPA_deg = -1               # operating pressure angle, degrees
        self.OPA = -1                   # operating pressure angle, radians
        self.bkl = 0                    # backlash
        self.rtcl1 = -1                 # root clearances
        self.rtcl2 = -1
        self.CD = -1                    # center distance
        self.CR = 0                     # contact ratio
        self.RPM = 1                  # pinion speed
        self.torque = 1                 # pinion torque

    def initGearDesignFields(self):
        # Called on startup and whenever a file is loaded

        # gear design tab
        if self.mod > 0:
            if self.units.modMult == "M":
                self.setText(self.ui.le_mod, self.mod)
            elif self.units.modMult == "T":
                self.setText(self.ui.le_mod, 25.4/self.mod)

        self.setText(self.ui.le_PA_deg, self.PA_deg, 1, "{:.1f}")
        self.swapBklandCD()

        if self.G1.N > 0:
            self.setText(self.ui.le_N1, self.G1.N)
        if self.G2.N > 0:
            self.setText(self.ui.le_N2, self.G2.N)

        self.setText(self.ui.le_x1, self.G1.x)
        self.setText(self.ui.le_x2, self.G2.x)

        if self.G1.Ro > 0:
            self.setText(self.ui.le_Ro1, self.G1.Ro, self.units.lenMult)
        if self.G2.Ro > 0:
            self.setText(self.ui.le_Ro2, self.G2.Ro, self.units.lenMult)

        self.setText(self.ui.le_Rtip1, self.G1.Rtip, self.units.lenMult)
        self.setText(self.ui.le_Rtip2, self.G2.Rtip, self.units.lenMult)

        if self.rtcl1 > 0:
            self.setText(self.ui.le_rtcl1, self.rtcl1, self.units.lenMult)
        if self.rtcl2 > 0:
            self.setText(self.ui.le_rtcl2, self.rtcl2, self.units.lenMult)

        self.setText(self.ui.le_Rf1, self.G1.Rf, self.units.lenMult)
        self.setText(self.ui.le_Rf2, self.G2.Rf, self.units.lenMult)

        self.setType(self.G2.type)

        # mesh slider
        self.sliderScale = 100    # the slider can only handle ints, show scale up everthing
        self.ui.hSlider_Mesh.setMinimum(0)
        self.ui.hSlider_Mesh.setMaximum(2*self.sliderScale)
        self.ui.hSlider_Mesh.setSliderPosition(1*self.sliderScale)    # pitch point happens at slider = 1

        # stress tab
        self.setText(self.ui.le_FW1, self.G1.FW, self.units.lenMult)
        self.setText(self.ui.le_FW2, self.G2.FW, self.units.lenMult)

        self.setText(self.ui.le_E1, self.G1.E, self.units.pressureMult, "{:.0f}")
        self.setText(self.ui.le_E2, self.G2.E, self.units.pressureMult, "{:.0f}")

        self.setText(self.ui.le_nu1, self.G1.nu, 1)
        self.setText(self.ui.le_nu2, self.G2.nu, 1)

        self.setText(self.ui.le_RPM, self.RPM, 1, "{:.0f}")
        self.setText(self.ui.le_torque, self.torque, self.units.torqueMult, "{:.0f}")

    def exportDXF(self):
        for gear in [self.G1, self.G2]:
            if gear.Rb < 0 :
                messageBox = QMessageBox.critical(self, "Error exporting", "Could not export geometry for gear "+str(gear.ID))
            else:
                draw.layoutGear(self, gear, save=True)

    def openJSON(self):
        loadPath, selectedFilter = QFileDialog.getOpenFileName(self, 'Load Design')

        if loadPath == '':
            return
        else:
            self.savePath = loadPath

            with open(loadPath, 'r', encoding='utf-8') as f:
                dictFull = json.load(f)

            dictG1 = dictFull["Gear1"]
            dictG2 = dictFull["Gear2"]
            dictM = dictFull["Mesh"]

            # start with a clean slate
            self.G1.reset()
            self.G2.reset()
            self.resetMeshParams()

            # set mesh parameters
            self.setUnits(int(dictM["units"]))
            actionsList = self.groupUnits.actions()
            actionsList[int(dictM["units"])].setChecked(True)

            self.setType(dictM["type"])

            self.set_mod(dictM["mod"])
            self.set_PA_deg(dictM["PA_deg"])

            if dictM["set_CD_bkl"] == 0:
                # use backlash
                self.ui.cb_CD_bkl.setCurrentIndex(0)
            else:
                # use center distance
                self.ui.cb_CD_bkl.setCurrentIndex(1)

            self.set_bkl(dictM["bkl"])
            self.set_CD(dictM["CD"])

            # set gear parameters
            for gear, dict in zip([self.G1, self.G2], [dictG1, dictG2]):
                self.set_N(gear, dict["N"])
                self.set_x(gear, dict["x"])
                self.set_Ro(gear, dict["Ro"])
                self.set_Rtip(gear, dict["Rtip"])

            if dictM["type"] == "internal":
                self.set_Rrim(self.G2, dictG2["Rrim"])
                self.set_Rr(dictG2["Rr"])

            self.set_rtcl(self.G1, dictM["rtcl1"])
            self.set_rtcl(self.G2, dictM["rtcl2"])

            # split it up so that both N's and rtcl's are set before Rf
            for gear, dict in zip([self.G1, self.G2], [dictG1, dictG2]):
                self.set_Rf(gear, dict["Rf"])
                self.set_FW(gear, dict["FW"])
                self.set_E(gear, dict["E"])
                self.set_nu(gear, dict["nu"])

            self.set_RPM(dictM["speed"])
            self.set_torque(dictM["torque"])

            self.initGearDesignFields()

    def saveAsJSON(self):
        if self.savePath == '':
            defaultName = 'gear_design.json'
        else:
            defaultName = self.savePath

        savePath, selectedFilter = QFileDialog.getSaveFileName(self, 'Save Design', defaultName)

        if savePath == '':
            return
        else:
            self.savePath = savePath
            self.saveJSON(self.savePath)

    def saveJSON(self, _path):
        if self.savePath == '':
            self.saveAsJSON()
        else:
            dictFull = {
                        "Gear1" : self.createJSONGear(self.G1),
                        "Gear2" : self.createJSONGear(self.G2),
                        "Mesh" : self.createJSONMesh()
                    }

            with open(_path, 'w', encoding='utf-8') as f:
                json.dump(dictFull, f, ensure_ascii=False, indent=4)

    def createJSONGear(self, _gear):
        return {
            "N" : _gear.N,
            "x" : _gear.x,
            "Ro" : _gear.Ro / self.units.lenMult,
            "Rtip" : _gear.Rtip / self.units.lenMult,
            "Rr" : _gear.Rr / self.units.lenMult,
            "Rf" : _gear.Rf / self.units.lenMult,
            "Rrim" : _gear.Rrim / self.units.lenMult,
            "FW" : _gear.FW / self.units.lenMult,
            "E" : _gear.E / self.units.pressureMult,
            "nu" : _gear.nu,
        }
    def createJSONMesh(self):
        if self.units.modMult == "M":
            mod = self.mod
        elif self.units.modMult == "T":
            mod = 25.4 / self.mod

        return {
            "type" : self.G2.type,
            "units": self.unitsList.index(self.units),
            "mod" : mod,
            "PA_deg" : self.PA_deg,
            "set_CD_bkl" : self.ui.cb_CD_bkl.currentIndex(),
            "bkl" : self.bkl / self.units.lenMult,
            "CD" : self.CD / self.units.lenMult,
            "rtcl1" : self.rtcl1 / self.units.lenMult,
            "rtcl2" : self.rtcl2 / self.units.lenMult,
            "speed" : self.RPM,
            "torque" : self.torque / self.units.torqueMult
        }

    def setUnits(self, unit):
        self.units = self.unitsList[unit]

        for label in self.modLabelList:
            label.setText(self.units.modName)

        for label in self.lengthLabelList:
            label.setText(self.units.lenName)

        for label in self.torqueLabelList:
            label.setText(self.units.torqueName)

        for label in self.pressureLabelList:
            label.setText(self.units.pressureName)

        for label in self.velLabelList:
            label.setText(self.units.velName)

    def setText(self, label, variable, mult=1, _format="{:.3f}"):
        label.setText(str(_format.format(variable/mult)))

    def setType(self, _type)  :
        if _type == "external":
            self.G2.type = "external"
            self.ui.rb_ext_layout.setChecked(True)
            self.ui.rb_ext_design.setChecked(True)
            self.ui.lb_Rrim_text.setHidden(True)
            self.ui.lb_Rrim_unit.setHidden(True)
            self.ui.le_Rrim.setHidden(True)
            self.ui.le_Ro2.setEnabled(True)
            self.ui.le_Rr2.setEnabled(False)

        elif _type == "internal":
            self.G2.type = "internal"
            self.ui.rb_int_layout.setChecked(True)
            self.ui.rb_int_design.setChecked(True)
            self.ui.lb_Rrim_text.setHidden(False)
            self.ui.lb_Rrim_unit.setHidden(False)
            self.ui.le_Rrim.setHidden(False)
            self.setText(self.ui.le_Rrim, self.G2.Rrim, self.units.lenMult)
            self.ui.le_Ro2.setEnabled(False)
            self.ui.le_Rr2.setEnabled(True)

        if self.ui.tabW_main.currentIndex() == 0: # layout helper tab
            draw.drawHelper(self)

        if self.ui.tabW_main.currentIndex() == 1: # design tab
            self.updateBaseAndPitch(self.G2)

# Helper Tab ##################################################################
    def findGearSizes(self):
        try:
            if self.units.modMult == "M":
                mod = float(self.ui.le_targetMod.text())
            elif self.units.modMult == "T":
                mod = 25.4 / float(self.ui.le_targetMod.text())
            GR = float(self.ui.le_targetGR.text())
            size = float(self.ui.le_targetSize.text()) * self.units.lenMult
        except:
            return

        if self.G2.type == "external":
            if self.ui.cb_CD_width.currentIndex() == 0:
                """
                (N1*mod)/2 + (N2*mod)/2 = CD  →  (mod/2)*N1 + (mod/2)*N2 = CD
                N2 / N1 = GR  →  GR*N1 - N2 = 0

                | mod/2 mod/2 | | N1 | = | CD |
                | GR    -1    | | N2 |   | 0  |
                """
                matA = np.array([ [mod/2, mod/2], [GR, -1] ])
                matB = np.array([ [size], [0] ])
                matX = np.matmul(np.linalg.inv(matA), matB)

                N1 = round(float(matX[0, 0]))
                N2 = round(N1*GR)
                # N2 = round(float(matX[1, 0]))

                # self.ui.le_pN.setText(str("{:.0f}".format(N1)))
                # self.ui.lb_gN3.setText(str("{:.0f}".format(N2)))
                self.setText(self.ui.le_pN, N1, 1, "{:.0f}")
                self.setText(self.ui.lb_gN3, N2, 1, "{:.0f}")

                self.populateChart(N2)
            else:
                """
                mod*N1/2 + mod*N2/2 + mod*(N1+2)/2 + mod*(N2+2)/2 = width  →  mod*N1 + mod*N2 = width - 2*mod
                N2 / N1 = GR  →  GR*N1 - N2 = 0

                | mod mod | | N1 | = | width - 2*mod |
                | GR  -1  | | N2 |   | 0             |
                """
                matA = np.array([ [mod, mod], [GR, -1] ])
                matB = np.array([ [size - 2*mod], [0] ])
                matX = np.matmul(np.linalg.inv(matA), matB)

                N1 = round(float(matX[0, 0]))
                N2 = round(N1*GR)

                self.setText(self.ui.le_pN, N1, 1, "{:.0f}")
                self.setText(self.ui.lb_gN3, N2, 1, "{:.0f}")

                self.populateChart(N2)

        elif self.G2.type == "internal":
            if self.ui.cb_CD_width.currentIndex() == 0:
                """
                (N2*mod)/2 - (N1*mod)/2 = CD  →  -(mod/2)*N1 + (mod/2)*N2 = CD
                N2 / N1 = GR  →  GR*N1 - N2 = 0

                | -mod/2 mod/2 | | N1 | = | CD |
                | GR     -1    | | N2 |   | 0  |
                """
                matA = np.array([ [-mod/2, mod/2], [GR, -1] ])
                matB = np.array([ [size], [0] ])
                matX = np.matmul(np.linalg.inv(matA), matB)

                N1 = round(float(matX[0, 0]))
                N2 = round(N1*GR)

                self.setText(self.ui.le_pN, N1, 1, "{:.0f}")
                self.setText(self.ui.lb_gN3, N2, 1, "{:.0f}")

                self.populateChart(N2)
            else:
                """
                mod*(N2+2) = width  →  mod*N2 = width - 2*mod
                N2 / N1 = GR  →  GR*N1 - N2 = 0

                | 0   mod | | N1 | = | width - 2*mod |
                | GR  -1  | | N2 |   | 0             |
                """
                matA = np.array([ [0, mod], [GR, -1] ])
                matB = np.array([ [size - 2*mod], [0] ])
                matX = np.matmul(np.linalg.inv(matA), matB)

                N1 = round(float(matX[0, 0]))
                N2 = round(N1*GR)

                self.setText(self.ui.le_pN, N1, 1, "{:.0f}")
                self.setText(self.ui.lb_gN3, N2, 1, "{:.0f}")

                self.populateChart(N2)

        draw.drawHelper()

    def updatePinionN(self):
        try:
            GR = float(self.ui.le_targetGR.text())
            N1 = int(self.ui.le_pN.text())
        except:
            return

        N2 = round(N1 * GR)

        self.populateChart(N2)
        draw.drawHelper()

    def populateChart(self, _N2):
        try:
            if self.units.modMult == "M":
                mod = float(self.ui.le_targetMod.text())
            elif self.units.modMult == "T":
                mod = 25.4 / float(self.ui.le_targetMod.text())
            N1 = int(self.ui.le_pN.text())
        except:
            return

        # display gear options
        N2_list = list(range(_N2-2, _N2+3))

        N2_label_list = [
                        self.ui.lb_gN1,
                        self.ui.lb_gN2,
                        self.ui.lb_gN3,
                        self.ui.lb_gN4,
                        self.ui.lb_gN5
                        ]

        icon_label_list = [
                        self.ui.lb_icon1,
                        self.ui.lb_icon2,
                        self.ui.lb_icon3,
                        self.ui.lb_icon4,
                        self.ui.lb_icon5
                        ]

        for N2, label, icon in zip(N2_list, N2_label_list, icon_label_list):
            self.setText(label, N2, 1, "{:.0f}")
            if np.gcd(N1, N2) == 1:
                icon.setPixmap(self.good_pixmap)
            else:
                icon.setPixmap(self.bad_pixmap)

        GR_label_list = [
                        self.ui.lb_GR1,
                        self.ui.lb_GR2,
                        self.ui.lb_GR3,
                        self.ui.lb_GR4,
                        self.ui.lb_GR5
                        ]

        for N2, label in zip(N2_list, GR_label_list):
            GR = N2 / N1
            self.setText(label, GR, 1, "{:.3f}")

        CD_label_list = [
                        self.ui.lb_CD1,
                        self.ui.lb_CD2,
                        self.ui.lb_CD3,
                        self.ui.lb_CD4,
                        self.ui.lb_CD5
                        ]

        for N2, label in zip(N2_list, CD_label_list):
            if self.G2.type == "external":
                CD = mod * (N1 + N2)/2
            elif self.G2.type == "internal":
                CD = mod * (N2 - N1)/2
            self.setText(label, CD, self.units.lenMult, "{:.3f}")

        width_label_list = [
                        self.ui.lb_width1,
                        self.ui.lb_width2,
                        self.ui.lb_width3,
                        self.ui.lb_width4,
                        self.ui.lb_width5
                        ]

        for N2, label in zip(N2_list, width_label_list):
            Ros1 = mod * (N1 + 2)/2
            if self.G2.type == "external":
                Ros2 = mod * (N2 + 2)/2
                CD = mod * (N1 + N2)/2
                width = Ros1 + CD + Ros2
            elif self.G2.type == "internal":
                Ros2 = mod * (N2 + 2 + 3)/2 # add an addition 3*mod for the rim thickness
                CD = mod * (N2 - N1)/2
                width = 2 * Ros2
            self.setText(label, width, self.units.lenMult, "{:.3f}")



    def useLayout(self):
        if self.ui.le_pN.text() == "":
            return

        N2_label_list = [
                        self.ui.lb_gN1,
                        self.ui.lb_gN2,
                        self.ui.lb_gN3,
                        self.ui.lb_gN4,
                        self.ui.lb_gN5
                        ]

        radio_button_list = [
                           self.ui.rb_1,
                           self.ui.rb_2,
                           self.ui.rb_3,
                           self.ui.rb_4,
                           self.ui.rb_5
                           ]

        N2 = -1
        for N, radioButton in zip(N2_label_list, radio_button_list):
            if radioButton.isChecked():
                N2 = int(N.text())
                break

        self.ui.le_mod.setText(self.ui.le_targetMod.text())
        self.set_mod(self.ui.le_targetMod.text())

        self.ui.le_N1.setText(self.ui.le_pN.text())
        self.set_N(self.G1, self.ui.le_pN.text())

        self.ui.le_N2.setText(str(N2))
        self.set_N(self.G2, N2)

        self.ui.tabW_main.setCurrentIndex(1)

# Gear Design Tab #############################################################
    def swapBklandCD(self):
        # input backlash
        if self.ui.cb_CD_bkl.currentIndex() == 0:
            self.setText(self.ui.le_CD_bkl, self.bkl, self.units.lenMult)

            self.ui.lb_bkl_text.hide()
            self.ui.lb_bkl_unit.hide()
            self.ui.lb_bkl_value.hide()

            self.ui.lb_CD_text.show()
            self.ui.lb_CD_unit.show()
            self.ui.lb_CD_value.show()
            if self.CD > 0:
                self.setText(self.ui.lb_CD_value, self.CD, self.units.lenMult)

        # input center distance
        elif self.ui.cb_CD_bkl.currentIndex() == 1:
            self.setText(self.ui.le_CD_bkl, self.CD, self.units.lenMult)

            self.ui.lb_CD_text.hide()
            self.ui.lb_CD_unit.hide()
            self.ui.lb_CD_value.hide()

            self.ui.lb_bkl_text.show()
            self.ui.lb_bkl_unit.show()
            self.ui.lb_bkl_value.show()
            self.setText(self.ui.lb_bkl_value, self.bkl, self.units.lenMult)

    def set_N(self, _gear, _N):
        if is_number(_N):
            _gear.N = int(_N)
            if self.G1.N > 1 and self.G2.N > 1:
                self.setText(self.ui.lb_GR, self.G2.N / self.G1.N)
            self.updateBaseAndPitch(_gear)

    def set_mod(self, _mod):
        if is_number(_mod):
            if self.units.modMult == "M":
                self.mod = float(_mod)
            elif self.units.modMult == "T":
                self.mod = 25.4 / float(_mod)
            self.updateBaseAndPitch(self.G1)
            self.updateBaseAndPitch(self.G2)

    def set_PA_deg(self, _PA_deg):
        if is_number(_PA_deg):
            self.PA_deg = float(_PA_deg)
            self.PA = deg2rad(self.PA_deg)
            self.updateBaseAndPitch(self.G1)
            self.updateBaseAndPitch(self.G2)

    def updateBaseAndPitch(self, _gear):
        if _gear.N > 0 and self.mod > 0 and self.PA > 0:
            _gear.Rs = (self.mod * _gear.N) / 2
            _gear.Rb = _gear.Rs * cos(self.PA)
            _gear.Pb = tau * _gear.Rb / _gear.N
            _gear.Ps = tau * _gear.Rs / _gear.N

            if _gear.type == "external":
                _gear.Ros = (self.mod * (_gear.N+2)) / 2
            elif _gear.type == "internal":
                _gear.Ros = (self.mod * (_gear.N+2.5)) / 2
                _gear.Rrim = (self.mod * (_gear.N+5)) / 2
            _gear.Ro = _gear.Ros

            # update UI
            if _gear.ID == 1:
                self.setText(self.ui.lb_Rs1, self.G1.Rs, self.units.lenMult)
                self.setText(self.ui.lb_Ros1, self.G1.Ros, self.units.lenMult)
                self.setText(self.ui.le_Ro1, self.G1.Ro, self.units.lenMult)
            else:
                self.setText(self.ui.lb_Rs2, self.G2.Rs, self.units.lenMult)
                self.setText(self.ui.lb_Ros2, self.G2.Ros, self.units.lenMult)
                self.setText(self.ui.le_Ro2, self.G2.Ro, self.units.lenMult)
                if _gear.type == "external":
                    pass
                elif _gear.type == "internal":
                    self.setText(self.ui.le_Rrim, self.G2.Rrim, self.units.lenMult)

            self.updateStandardToothThickness(_gear)

    def set_x(self, _gear, _x):
        if is_number(_x):
            _gear.x = float(_x)
            self.updateStandardToothThickness(_gear)

    def updateStandardToothThickness(self, _gear):
        if self.mod > 0 and self.PA > 0:
            # GOIG 6.11
            _gear.tts = self.mod * (pi/2 + 2*_gear.x*tan(self.PA))
            if _gear.ID == 1:
                self.setText(self.ui.lb_tts1, self.G1.tts, self.units.lenMult)
            else:
                if _gear.type == "external":
                    self.setText(self.ui.lb_tts2, self.G2.tts, self.units.lenMult)
                if _gear.type == "internal":
                    self.setText(self.ui.lb_tts2, self.G2.Ps - self.G2.tts, self.units.lenMult)

            self.calcStandardRtcl(_gear)
            self.updateCenterDistance()
            self.updateRomax(_gear)

    def calcStandardRtcl(self, _gear):
        # standard root clearance
        addendum = self.mod
        rtcl = (0.25 * addendum)
        # standard root radius
        Rrs_ext = _gear.Rs - addendum - rtcl
        Rrs_int = _gear.Rs - addendum

        if _gear.ID == 1:
            _gear.Rrs = Rrs_ext
            self.setText(self.ui.lb_Rrs1, self.G1.Rrs, self.units.lenMult)
        else:
            if _gear.type == "external":
                _gear.Rrs = Rrs_ext
                self.setText(self.ui.lb_Rrs2, self.G2.Rrs, self.units.lenMult)
            elif _gear.type == "internal":
                _gear.Rrs = Rrs_int
                self.setText(self.ui.lb_Rrs2, self.G2.Rrs, self.units.lenMult)

        if _gear.Rr < 0 :
            _gear.Rr = _gear.Rrs

        if _gear.type == "internal":
            if _gear.Rr < _gear.Rb:
                _gear.Rr = _gear.Rrs
            elif _gear.Rr > _gear.Rs:
                _gear.Rr = _gear.Rrs

        if self.G1.N > 0 and self.G2.N > 0:
            if self.rtcl1 < 0:
                self.set_rtcl(self.G1, rtcl)
                self.setText(self.ui.le_rtcl1, self.rtcl1, self.units.lenMult)
            if self.rtcl2 < 0:
                self.set_rtcl(self.G2, rtcl)
                self.setText(self.ui.le_rtcl2, self.rtcl2, self.units.lenMult)

    def updateRomax(self, _gear):
        if _gear.Rs > 0:
            # max OD is when theta_A is 0, i.e. the involute hits the tooth centerline
            # theta_A = (gear.tts / (2*gear.Rs)) + invF(gear.PA) - invF(phi_A)
            # 0 = (gear.tts / (2*gear.Rs)) + invF(gear.PA) - invF(phi_A)
            # invF(phi_A) = (gear.tts / (2*gear.Rs)) + invF(gear.PA)
            phi_A = revInvF((_gear.tts / (2*_gear.Rs)) + invF(self.PA))
            _gear.Romax = _gear.Rb / cos(phi_A)

            if _gear.ID == 1:
                self.setText(self.ui.lb_Romax1, self.G1.Romax, self.units.lenMult)
            else:
                self.setText(self.ui.lb_Romax2, self.G2.Romax, self.units.lenMult)

            self.set_Ro(_gear, _gear.Ro)

    def set_Ro(self, _gear, _Ro):
        if _gear.Romax < 0:
            return

        if is_number(_Ro):
            if float(_Ro) * self.units.lenMult > _gear.Romax:
                _gear.Ro = _gear.Romax
            else:
                _gear.Ro = float(_Ro) * self.units.lenMult

            if _gear.ID == 1:
                self.setText(self.ui.le_Ro1, self.G1.Ro, self.units.lenMult)
            else:
                self.setText(self.ui.le_Ro2, self.G2.Ro, self.units.lenMult)
            # check that Rtip is still valid, shrink if necessary
            self.updateRootRadius(self.G1)
            self.updateRootRadius(self.G2)
            self.updateMaxTipRadius(_gear)
            self.set_Rtip(_gear, _gear.Rtip)

    def updateMaxTipRadius(self, _gear):
        """
        ##########################################
        A : point on involute where fillet starts
        E : tangent point on base circle, determined by A and phi_A
        C : center point of gear
        F : center point of fillet

        ##########################################
        # angle between A and tooth centerline
        theta_A = (tts/(2*Rs)) + invF(PA) - invF(phi_A)

        # angle between line CE and tooth centerline
        alpha = phi_A - theta_A

        # length of line from E to A
        EA = Rb*tan(phi_A)

        # length of line from E to F
        EF = Rb*tan(alpha)

        # the tip fillet radius is the difference between EA and EF
        RTip1 = EA - EF
        Rtip = Rb*tan(phi_A) - Rb*tan(alpha)
        Rtip = Rb*tan(phi_A) - Rb*tan(phi_A - theta_A)
        Rtip = Rb*tan(phi_A) - Rb*tan(phi_A - (tts/(2*Rs)) - invF(PA) + invF(phi_A))

        # length of line from C to F
        CF = Rb / cos(alpha)

        # the tip fillet radius is the difference between Ro and CF
        Rtip2 = Ro - CF
        Rtip2 = Ro - (Rb / cos(alpha))
        Rtip2 = Ro - (Rb / cos(phi_A - theta_A))
        Rtip2 = Ro - (Rb / cos(phi_A - (tts/(2*Rs)) - invF(PA) + invF(phi_A)))

        """

        if _gear.N <= 1:
            return

        Ro = _gear.Ro
        Rb = _gear.Rb
        Rs = _gear.Rs
        tts = _gear.tts
        PA = self.PA

        def RTip1(phi_A):
            return Rb*tan(phi_A) - Rb*tan(phi_A - (tts/(2*Rs)) - invF(PA) + invF(phi_A))

        def RTip2(phi_A):
             return Ro - (Rb / (cos(phi_A - (tts/(2*Rs)) - invF(PA) + invF(phi_A))))

        # RTip1 and RTip2 are equal, so this should be zero
        def func(phi_A):
            return RTip1(phi_A) - RTip2(phi_A)

        # initial guess is at standard pitch radius
        initialGuess = arccos(Rb/Rs)
        phi_A_solved = least_squares(func, x0=initialGuess).x.item()
        _gear.Rtip_max = float(RTip1(phi_A_solved))
        if _gear.ID == 1:
            # self.ui.lb_Rtipmax1.setText(str("{:.3f}".format(self.G1.Rtip_max)))
            self.setText(self.ui.lb_Rtipmax1, self.G1.Rtip_max, self.units.lenMult)
        else:
            # self.ui.lb_Rtipmax2.setText(str("{:.3f}".format(self.G2.Rtip_max)))
            self.setText(self.ui.lb_Rtipmax2, self.G2.Rtip_max, self.units.lenMult)

    def set_Rtip(self, _gear, _Rtip):
        if is_number(_Rtip):
            if float(_Rtip) * self.units.lenMult > _gear.Rtip_max:
                _gear.Rtip = _gear.Rtip_max
                if _gear.ID == 1:
                    self.setText(self.ui.le_Rtip1, self.G1.Rtip, self.units.lenMult)
                else:
                    self.setText(self.ui.le_Rtip2, self.G2.Rtip, self.units.lenMult)
            else:
                _gear.Rtip = float(_Rtip) * self.units.lenMult

            self.updateRoe(_gear)

    def updateRoe(self, _gear):
        if _gear.Rb < 0:
            return

        if _gear.Ro < 0 and _gear.Ros > 0:
            _gear.Ro = _gear.Ros
            if _gear.ID == 1:
                self.setText(self.ui.le_Ro1, self.G1.Ro, self.units.lenMult)
            else:
                self.setText(self.ui.le_Ro2, self.G2.Ro, self.units.lenMult)

        _gear.Roe = sqrt( _gear.Rb**2 + ( sqrt((_gear.Ro-_gear.Rtip)**2 - _gear.Rb**2) + _gear.Rtip )**2 )

        if _gear.ID == 1:
            self.setText(self.ui.lb_Roe1, self.G1.Roe, self.units.lenMult)
        else:
            self.setText(self.ui.lb_Roe2, self.G2.Roe, self.units.lenMult)

        self.updateContactRatio()

    def set_bkl(self, _bkl):
        if is_number(_bkl):
            self.bkl = float(_bkl) * self.units.lenMult
            self.updateCenterDistance()

    def set_CD(self, _CD):
        if is_number(_CD):
            self.CD = float(_CD) * self.units.lenMult
            self.updateCenterDistance()

    def updateBklandCD(self):
        # backlash
        if self.ui.cb_CD_bkl.currentIndex() == 0:
            self.set_bkl(float(self.ui.le_CD_bkl.text()))
        # center distance
        elif self.ui.cb_CD_bkl.currentIndex() == 1:
            self.set_CD(float(self.ui.le_CD_bkl.text()))

    def updateCenterDistance(self):
        if self.G1.Rs < 0 or self.G2.Rs < 0:
            return

        Rp1, Rp2, tt1, tt2 = self.updatePitchRadius()
        # update pitch radius
        self.G1.Rp = Rp1.item()
        self.G2.Rp = Rp2.item()
        # update tooth thickness at new pitch radius
        self.G1.tt = tt1.item()
        self.G2.tt = tt2.item()

        self.setText(self.ui.lb_Rp1, self.G1.Rp, self.units.lenMult)
        self.setText(self.ui.lb_Rp2, self.G2.Rp, self.units.lenMult)
        self.setText(self.ui.lb_tt1, self.G1.tt, self.units.lenMult)
        self.setText(self.ui.lb_tt2, self.G2.tt, self.units.lenMult)

        if self.ui.cb_CD_bkl.currentIndex() == 0: # update center distance
            if self.G2.type == "external":
                self.CD = self.G1.Rp + self.G2.Rp
            elif self.G2.type == "internal":
                self.CD = self.G2.Rp - self.G1.Rp
            self.setText(self.ui.lb_CD_value, self.CD, self.units.lenMult)

        elif self.ui.cb_CD_bkl.currentIndex() == 1: # update backlash
            self.bkl = (tau*self.G1.Rp)/self.G1.N - self.G1.tt - self.G2.tt
            self.setText(self.ui.lb_bkl_value, self.bkl, self.units.lenMult)

        # Operating pressure angle at updated center distance
        if self.G2.type == "external":
            self.OPA = arccos((self.G1.Rb+self.G2.Rb) / self.CD)
        elif self.G2.type == "internal":
            self.OPA = arccos((self.G2.Rb-self.G1.Rb) / self.CD)
        self.OPA_deg = rad2deg(self.OPA)

        self.updateContactRatio()
        self.updateRootRadius(self.G1)
        self.updateRootRadius(self.G2)

    def updatePitchRadius(self):
        """Finds pitch radius and effective tooth thickness"""
        N1 = self.G1.N
        N2 = self.G2.N
        # Precalculate involute function at standard pitch / PA
        invS = invF(self.PA)
        # Standard pitch radius
        Rs1 = self.G1.Rs
        Rs2 = self.G2.Rs
        # Base circle radius
        Rb1 = self.G1.Rb
        Rb2 = self.G2.Rb
        # Standard tooth thickness with profile shift
        mod = self.mod
        tts1 = self.G1.tts
        tts2 = self.G2.tts
        bkl = self.bkl
        CD = self.CD

        def func(x): # the input x is a vector: [Rp1, Rp2, tt1, tt2]
            F = zeros(4)

            # pitch circle is determined by mod and number of teeth => mod = Rp/N
            # both pinion and gear must have same mod, so Rp1/N1 = Rp2/N2
            # => N2*Rp1 - N1*Rp2 = 0
            F[0] = N2*x[0] - N1*x[1]
            # calculate tooth thickness at new pitch radius
            # tt = Rp*( (tts/Rs) + 2*(invF(PA) - invF(acos(Rb/Rp)) ) )
            # => Rp*( (tts/Rs) + 2*(invF(PA) - invF(acos(Rb/Rp)) ) ) - tt = 0
            F[1] = x[0]*( (tts1/Rs1) + 2*(invS - invF(arccos(Rb1/x[0])) ) ) - x[2]
            F[2] = x[1]*( (tts2/Rs2) + 2*(invS - invF(arccos(Rb2/x[1])) ) ) - x[3]

            # use backlash
            if self.ui.cb_CD_bkl.currentIndex() == 0:
                if self.G2.type == "external":
                    # circular pitch is sum of each tooth thickness and backlash
                    # (tau*Rp1)/N1 = tt1 + tt2 + bkl [equivalently, (tau*Rp2)/N2 = tt1 + tt2 + bkl]
                    # => (tau*Rp1)/N1 - tt1 - tt2 - bkl = 0
                    F[3] = (tau*x[0])/N1 - x[2] - x[3] - bkl
                elif self.G2.type == "internal":
                    # circular pitch is sum of each tooth thickness and backlash
                    # internal gear tooth thickness is external tooth thickness plus backlash
                    # tt2 = tt1 + bkl
                    # => tt2 - tt1 - bkl = 0
                    F[3] = x[3] - x[2] - bkl
            # use center distance
            elif self.ui.cb_CD_bkl.currentIndex() == 1:
                # CD = Rp1 + Rp2
                # => Rp1 + Rp2 - CD = 0
                F[3] = x[0] + x[1] - CD

            return F

        #   For initial guess, use standard values
        initialGuess = [Rs1, Rs2, tts1, tts2]
        root = least_squares(func, x0=initialGuess).x

        return root

    def updateContactRatio(self):
        if self.G1.Rs < 0 or self.G2.Rs < 0:
            return
        if self.G2.type == "external":
            # AGMA-908 Parameters
            # max line action, Rb to Rb
            C6 = self.CD * sin(self.OPA)
            # start of line of contact, when G2 is at Roe
            C1 = C6 - sqrt(self.G2.Roe**2 - self.G2.Rb**2)
            # end of line of contact, when G1 is at Roe
            C5 = sqrt(self.G1.Roe**2 - self.G1.Rb**2)
            # point where line of contact intersects center line (not used)
            #C3 = (self.G1.N/(self.G1.N+self.G2.N)) * C6

            # Line of contact
            LoC = C5 - C1;
            # Contact ratio
            self.CR = LoC / self.G1.Pb;
            self.setText(self.ui.lb_CR, self.CR, 1)
            if is_number(self.CR):
                # minimum number of teeth engaged at any time
                n = int(self.CR)

                # lowest point of single tooth contact for G1
                C2 = C5 - n*self.G1.Pb
                # highest point of single tooth contact for G1
                C4 = C1 + n*self.G1.Pb

                # Highest point of single tooth contact
                self.G1.Rhp = sqrt(self.G1.Rb**2 + C4**2)
                self.G2.Rhp = sqrt(self.G2.Rb**2 + (C6-C2)**2)

        elif self.G2.type == "internal":
            # GOIG 12.30
            E1P = self.G1.Rb * tan(self.OPA)
            E2P = self.G2.Rb * tan(self.OPA)
            E1T1 = sqrt(self.G1.Roe**2 - self.G1.Rb**2)
            E2T2 = sqrt(self.G2.Rr**2 - self.G2.Rb**2)
            E1T2 = E1P - (E2P - E2T2)

            # Line of contact
            LoC = (E2P - E2T2) + (E1T1 - E1P)

            # Contact ratio
            self.CR = LoC / self.G1.Pb;
            self.setText(self.ui.lb_CR, self.CR, 1)
            if is_number(self.CR):
                # minimum number of teeth engaged at any time
                n = int(self.CR)
                # Highest point of single tooth contact
                self.G1.Rhp = sqrt(self.G1.Rb**2 + (E1T2 + n*self.G1.Pb)**2)
                self.G2.Rhp = sqrt(self.G2.Rb**2 + (E2T2 + n*self.G2.Pb)**2)

    def set_rtcl(self, _gear, _rtcl):
        if is_number(_rtcl):
            if _gear.ID == 1:
                self.rtcl1 = float(_rtcl) * self.units.lenMult
                self.updateRootRadius(self.G1)
            else:
                self.rtcl2 = float(_rtcl) * self.units.lenMult
                self.updateRootRadius(self.G2)

    def set_Rr(self, _Rr):
        if is_number(_Rr):
            self.G2.Rr = float(_Rr) * self.units.lenMult
            self.checkUndercut(self.G2)
            self.updateMaxRootFillet(self.G2)
            self.updateRootRadius(self.G1)

    def updateRootRadius(self, _gear):
        if self.CD < 0:
            return

        if _gear.ID == 1:
            if self.G2.type == "external":
                self.G1.Rr = self.CD - self.G2.Ro - self.rtcl1
            elif self.G2.type == "internal":
                self.G1.Rr = self.G2.Rr - self.CD - self.rtcl1
                self.updateContactRatio()
            self.setText(self.ui.lb_Rr1, self.G1.Rr, self.units.lenMult)
        else:
            if self.G2.type == "external":
                self.G2.Rr = self.CD - self.G1.Ro - self.rtcl2
                self.setText(self.ui.le_Rr2, self.G2.Rr, self.units.lenMult)
            elif self.G2.type == "internal":
                self.G2.Ro = self.CD + self.G1.Ro + self.rtcl2
                self.updateRoe(self.G2)
                self.updateMaxTipRadius(self.G2)
                self.set_Rtip(self.G2, self.G2.Rtip)
                self.setText(self.ui.le_Ro2, self.G2.Ro, self.units.lenMult)
                self.setText(self.ui.le_Rr2, self.G2.Rr, self.units.lenMult)

        self.checkUndercut(_gear)
        self.updateMaxRootFillet(_gear)

    def updateMaxRootFillet(self, _gear):
        if _gear.N < 0 or _gear.Rr < 0:
            return

        ###########################################################################
        #   Calculate fillet radius. This function computes two separate distances:
        #   1.) the distance from the fillet center to the involute curve, and
        #   2.) the distance from the fillet center to the root circle
        #   The function then finds the condition where these two distances are the
        #   same.

        N = _gear.N
        tts = _gear.tts
        Rs = _gear.Rs
        Rb = _gear.Rb
        Rr = _gear.Rr
        PA = self.PA

        # phi_A - profile angle at some point A on the involute
        # theta_A - angle between tooth centerline and some point A on the involute
        # phi_F - profile angle between fillet centerline and Rb, where a line tangent to
        #   the base circle goes through some point A on the involute
        # Rf_1 - distance between fillet centerline and some point A on the
        #   involute, along a line tangent to the base circle
        # Rf_2 - distance between the fillet center and the root circle
        # JFI - junction of fillet and involute
        ###########################################################################

        # angle between tooth centerline and involute at base circle (phi_A = 0)
        theta_A = tts/(2*Rs) + invF(PA)
        # angle between involute at base circle and center of tooth gap
        alpha = pi/N - theta_A
        # full fillet radius assuming the JFI is on the base circle
        Rfu = Rb * tan(alpha)
        Rrmin = Rb - Rfu

        # Undercut
        if Rr < Rrmin:
            _gear.Rff = -(Rr*sin(alpha))/(sin(alpha) - 1)
        else:
            # angle between tooth centerline and fillet centerline = pi/N
            # phi_F = pi/N - theta_A + phi_A
            # where: theta_A = tts/(2*Rs) + invF(PA) - invF(phi_A)
            # where: invF(phi_A) = tan(phi_A) - phi_A
            # => phi_F = pi/N - (tts/(2*Rs) + invF(PA) - (tan(phi_A) - phi_A)) + phi_A
            def phi_F(phi_A):
                  return pi/N - tts/(2*Rs) - invF(PA) + tan(phi_A)

            def Rf1(phi_A):
                  return Rb*(tan(phi_F(phi_A)) - tan(phi_A))

            def Rf2(phi_A):
                return Rb/cos(phi_F(phi_A)) - Rr

            # Rf1 and Rf2 are equal, so this should be zero
            def func(phi_A):
                return Rf1(phi_A) - Rf2(phi_A)

            # initial guess is at standard pitch radius
            initialGuess = arccos(Rb/Rs)
            phi_JFI = least_squares(func, x0=initialGuess).x.item()

            # _gear.phi_JFI = phi_JFI
            newRff = Rf1(phi_JFI)
            if newRff < 0:
                _gear.Rff = 0
            else:
                _gear.Rff = newRff

        if _gear.Rf > _gear.Rff:
            self.set_Rf(_gear, _gear.Rff)

        # update UI
        if _gear.ID == 1:
            self.setText(self.ui.le_Rf1, self.G1.Rf, self.units.lenMult)
            self.setText(self.ui.lb_Rff1, self.G1.Rff, self.units.lenMult)
        else:
            self.setText(self.ui.le_Rf2, self.G2.Rf, self.units.lenMult)
            self.setText(self.ui.lb_Rff2, self.G2.Rff, self.units.lenMult)

    def set_Rf(self, _gear, _Rf):
        if is_number(_Rf):
            if float(_Rf) * self.units.lenMult > _gear.Rff:
                _gear.Rf = _gear.Rff
                if _gear.ID == 1:
                    self.setText(self.ui.le_Rf1, self.G1.Rf, self.units.lenMult)
                else:
                    self.setText(self.ui.le_Rf2, self.G2.Rf, self.units.lenMult)
            else:
                _gear.Rf = float(_Rf) * self.units.lenMult

            self.checkUndercut(_gear)

    def checkUndercut(self, _gear):
        if _gear.Rr < 0:
            return

        # get correct ui element
        if _gear.ID == 1:
            label = self.ui.lb_undercut1
        else:
            label = self.ui.lb_undercut2

        # distance from the gear center to the center point of the root fillet,
        # assuming the JFI is on the base circle
        # this forms a right triangle with Rb and Rf
        CF = sqrt(_gear.Rb**2 + _gear.Rf**2)
        # CF sets the minimum Rr for a given Rf
        Rrmin = CF - _gear.Rf

        # Undercut check
        if _gear.Rr < Rrmin:
            _gear.undercut = True
            label.setText("<font color=\"Red\">Undercut</font>")
        else:
            _gear.undercut = False
            label.setText("")

        self.updateJFI(_gear)

    def updateJFI(self, _gear):
        if _gear.Rr < 0:
            return

        if _gear.undercut == True:
            _gear.phi_JFI = 0

            theta_A = (_gear.tts/(2*_gear.Rs)) + invF(self.PA)
            # angle between JFI and center of fillet circle
            alpha_F = arcsin(_gear.Rf / (_gear.Rr + _gear.Rf))
            _gear.theta_F = theta_A + alpha_F
        else:
            # profile angle through center of fillet circle
            phi_F = arccos(_gear.Rb / (_gear.Rr + _gear.Rf))
            # line tangent to base circle through fillet center point
            EF = sqrt((_gear.Rr+_gear.Rf)**2 - _gear.Rb**2)
            # line tangent to base circle to involute
            EA = EF - _gear.Rf
            # profile angle at JFI
            phi_A = arctan(EA / _gear.Rb)
            theta_A = (_gear.tts/(2*_gear.Rs)) + invF(self.PA) - invF(phi_A)
            theta_F = phi_F - phi_A + theta_A

            _gear.phi_JFI = phi_A
            _gear.theta_F = theta_F

    def set_Rrim(self, _gear, _Rrim):
        if is_number(_Rrim):
            _gear.Rrim = float(_Rrim) * self.units.lenMult

# Stress ######################################################################
    def set_FW(self, _gear, _FW):
        if is_number(_FW):
            _gear.FW = float(_FW) * self.units.lenMult
    def set_RPM(self, _RPM):
        if is_number(_RPM):
            self.RPM = float(_RPM)

    def set_torque(self, _torque):
        if is_number(_torque):
            self.torque = float(_torque) * self.units.torqueMult

    def set_E(self, _gear, _E):
        if is_number(_E):
            _gear.E = float(_E) * self.units.pressureMult

    def set_nu(self, _gear, _nu):
        if is_number(_nu):
            _gear.nu = float(_nu)

    def updateStress(self):
        if self.G1.N < 1 or self.G2.N < 1:
            return
        if self.G1.FW <= 0 or self.G2.FW <= 0:
            return

        # use smallest face width
        FW = min(self.G1.FW, self.G2.FW)

        # convert torque to force through HPSTC tangent to base circle
        w = self.torque / (self.G1.Rb * FW)

        stress.calcPitchLineVelocity(self)
        stress.calcContactStress(self, w)
        stress.calcBendingStress(self, w)

# Main ########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = jpgearqt()
    widget.show()
    sys.exit(app.exec())
