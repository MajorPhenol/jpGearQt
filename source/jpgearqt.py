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

import sys, os, tempfile

from PySide6.QtWidgets import QApplication, QWidget, QLayout, QVBoxLayout, QLabel
from PySide6.QtWidgets import QMenuBar, QMenu
from PySide6.QtWidgets import QFileDialog, QDialog, QDialogButtonBox, QMessageBox, QToolTip

from PySide6.QtCore import Qt, QPoint, QEvent, QCoreApplication, QTimer

from PySide6.QtGui import QIcon, QPixmap, QShortcut, QKeySequence
from PySide6.QtGui import QAction, QActionGroup
from PySide6.QtGui import QPalette, QColor
from PySide6.QtGui import QIntValidator, QDoubleValidator

from ui_main import Ui_MainForm

from Gear import Gear
from MplCanvas import MplCanvas
import Units
from helper import *
from file import *
import draw
import stress

from math import floor

import numpy as np
from numpy import pi, sin, cos, tan, arcsin, arccos, arctan
from numpy import rad2deg, deg2rad
from numpy import sqrt, zeros, linspace, real

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
        super().__init__()
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "resources/icon_main.png")))
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        VERSION = "3.0"
        self.setWindowTitle(str("jpGear v" + VERSION))

        self.defaultPalette = QApplication.palette()
        self.errorPalette = self.defaultPalette
        self.errorPalette.setColor(QPalette.Window, Qt.red)
        self.errorPalette.setColor(QPalette.WindowText, Qt.white)

        # import icons
        self.good_pixmap = QPixmap(os.path.join(os.path.dirname(__file__), "resources/icon_good.png"))
        self.bad_pixmap = QPixmap(os.path.join(os.path.dirname(__file__), "resources/icon_bad.png"))

        self.labelUI()
        self.createMenu()
        self.setupCanvases()
        self.connectUI()
        self.setupShortcuts()

        # gear objects
        self.G1 = Gear(1)
        self.G2 = Gear(2)
        self.G3 = Gear(3)
        self.gearList = [self.G1, self.G2, self.G3]

        self.setType(Type.external.value)

        self.resetMeshParams()
        self.initGearDesignFields()

        # for saving JSON
        self.savePath = ''

# Setup #######################################################################
    def labelUI(self):
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
            self.ui.lb_Rrim_unit,
            self.ui.lb_Romax_unit,
            self.ui.lb_Ros_unit,
            self.ui.lb_Rp_unit,
            self.ui.lb_Rr_unit,
            self.ui.lb_Rrs_unit,
            self.ui.lb_Rs_unit,
            self.ui.lb_Rtip_unit,
            self.ui.lb_Rtipmax_unit,
            self.ui.lb_bkl_unit,
            self.ui.lb_bkl2_unit,
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

        # helper tab
        self.N3_label_list = [
                                self.ui.lb_N3_1,
                                self.ui.lb_N3_2,
                                self.ui.lb_N3_3,
                                self.ui.lb_N3_4,
                                self.ui.lb_N3_5
                                ]
        self.N2_label_list = [
                                self.ui.lb_N2_1,
                                self.ui.lb_N2_2,
                                self.ui.lb_N2_3,
                                self.ui.lb_N2_4,
                                self.ui.lb_N2_5
                                ]
        self.GR_label_list = [
                                self.ui.lb_GR1,
                                self.ui.lb_GR2,
                                self.ui.lb_GR3,
                                self.ui.lb_GR4,
                                self.ui.lb_GR5
                                ]
        self.CD_label_list = [
                                self.ui.lb_CD1,
                                self.ui.lb_CD2,
                                self.ui.lb_CD3,
                                self.ui.lb_CD4,
                                self.ui.lb_CD5
                                ]
        self.width_label_list = [
                                self.ui.lb_width1,
                                self.ui.lb_width2,
                                self.ui.lb_width3,
                                self.ui.lb_width4,
                                self.ui.lb_width5
                                ]
        self.icon_label_list = [
                                self.ui.lb_icon1,
                                self.ui.lb_icon2,
                                self.ui.lb_icon3,
                                self.ui.lb_icon4,
                                self.ui.lb_icon5
                                ]
        self.radio_button_list = [
                                   self.ui.rb_1,
                                   self.ui.rb_2,
                                   self.ui.rb_3,
                                   self.ui.rb_4,
                                   self.ui.rb_5
                                   ]
        self.planets_label_list = [
                                   self.ui.lb_planet1,
                                   self.ui.lb_planet2,
                                   self.ui.lb_planet3,
                                   self.ui.lb_planet4,
                                   self.ui.lb_planet5
                                   ]
        self.planets_icon_list = [
                                   self.ui.lb_p_icon1,
                                   self.ui.lb_p_icon2,
                                   self.ui.lb_p_icon3,
                                   self.ui.lb_p_icon4,
                                   self.ui.lb_p_icon5
                                   ]
        self.rb_planets_list = [
                                   self.ui.rb_p1,
                                   self.ui.rb_p2,
                                   self.ui.rb_p3,
                                   self.ui.rb_p4,
                                   self.ui.rb_p5
                                   ]

        # planetary-only
        self.G3LabelList = [
            # common
            self.ui.lb_bkl2_text,
            self.ui.lb_bkl2_unit,
            self.ui.le_bkl2,
            self.ui.lb_NPlanets_text,
            self.ui.le_NPlanets,
            self.ui.lb_max_planets_text,
            self.ui.lb_max_planets,
            self.ui.lb_spacing_text,
            self.ui.lb_icon_spacing,
            # gear 3
            self.ui.lb_G3,
            self.ui.lb_N3,
            self.ui.le_x3,
            self.ui.lb_Rs3,
            self.ui.lb_Rp3,
            self.ui.lb_tts3,
            self.ui.lb_tt3,
            self.ui.le_Ro3,
            self.ui.lb_Ros3,
            self.ui.lb_Romax3,
            self.ui.le_Rtip3,
            self.ui.lb_Rtipmax3,
            self.ui.lb_Roe3,
            self.ui.le_rtcl3,
            self.ui.lb_Rrs3,
            self.ui.lb_Rr3,
            self.ui.le_Rf3,
            self.ui.lb_Rff3,
            self.ui.lb_CR2,
            self.ui.lb_undercut3,
            # mesh buttons
            self.ui.rb_sp,
            self.ui.rb_pr,
            # stress
            self.ui.lb_stressG3,
            self.ui.le_FW3,
            self.ui.le_E3,
            self.ui.le_nu3,
            self.ui.lb_stressB3,
            self.ui.lb_stressC3
        ]

    def createMenu(self):
        # create menu bar
        menuBar = QMenuBar(self)

        # File Menu
        menuFile = menuBar.addMenu('&File')

        actOpen = menuFile.addAction('Open')
        actOpen.setShortcut(QKeySequence("Ctrl+O"))
        actOpen.triggered.connect(lambda: openJSON(self))

        actSave = menuFile.addAction('Save')
        actSave.setShortcut(QKeySequence("Ctrl+S"))
        actSave.triggered.connect(lambda: saveJSON(self))

        actSaveAs = menuFile.addAction('Save As')
        actSaveAs.setShortcut(QKeySequence("Ctrl+Shift+S"))
        actSaveAs.triggered.connect(lambda: saveAsJSON(self))

        actExportDXF = menuFile.addAction('Export DXF')
        actExportDXF.triggered.connect(lambda: exportDXF(self))

        menuFile.addSeparator()

        actExit = menuFile.addAction('Exit')
        actExit.setShortcut(QKeySequence("Ctrl+Q"))
        actExit.triggered.connect(lambda: sys.exit())

        # Options Menu
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

    def setupCanvases(self):
        ## layout helper tab
        self.canvasHelper = MplCanvas(self)
        helper_layout = QVBoxLayout(self.ui.f_helper_layout)
        helper_layout.addWidget(self.canvasHelper)

        ## gear designer tabs
        palette = QPalette(self.defaultPalette)
        palette.setColor(QPalette.WindowText, Qt.red)
        self.ui.lb_undercut1.setPalette(palette)
        self.ui.lb_undercut2.setPalette(palette)
        self.ui.lb_undercut3.setPalette(palette)

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
        # gear 3
        self.canvasG3 = MplCanvas(self)
        self.ui.vLayout_canvasG3.insertWidget(0,self.canvasG3)
        toolbarG3 = NavigationToolbar2QT(self.canvasG3, self)
        self.ui.hLayout_toolbarG3.insertWidget(0, toolbarG3)
        # mesh
        self.canvasMesh = MplCanvas(self)
        self.ui.vLayout_canvasMesh.insertWidget(0,self.canvasMesh)
        toolbarMesh = NavigationToolbar2QT(self.canvasMesh, self)
        self.ui.hLayout_toolbarMesh.insertWidget(0, toolbarMesh)

        # stress
        self.canvasStress1 = [MplCanvas(self), MplCanvas(self)]
        self.ui.vl_tab_stress1.addWidget(self.canvasStress1[0])
        self.ui.vl_tab_stress1.addWidget(self.canvasStress1[1])

        self.canvasStress2 = [MplCanvas(self), MplCanvas(self)]
        self.ui.vl_tab_stress2.addWidget(self.canvasStress2[0])
        self.ui.vl_tab_stress2.addWidget(self.canvasStress2[1])

    def connectUI(self):
        # create validators
        self.intVal = QIntValidator()
        self.intVal.setBottom(1)

        self.posDoubleVal = QDoubleValidator()
        self.posDoubleVal.setBottom(0)

        self.negDoubleVal = QDoubleValidator()

        # First tab
        #################
        self.ui.cb_type_helper.currentIndexChanged.connect(lambda: self.setType(self.ui.cb_type_helper.currentIndex()))

        self.ui.cb_input_helper.currentIndexChanged.connect(lambda: self.updatePlanetaryInput(self.ui.cb_input_helper, self.ui.cb_output_helper))
        self.ui.cb_output_helper.currentIndexChanged.connect(lambda: self.updatePlanetaryInput(self.ui.cb_input_helper, self.ui.cb_output_helper))

        self.ui.le_targetMod.setValidator(self.posDoubleVal)
        self.ui.le_targetMod.editingFinished.connect(lambda: self.updateHelper())
        self.ui.le_targetGR.setValidator(self.posDoubleVal)
        self.ui.le_targetGR.editingFinished.connect(lambda: self.updateHelper())
        self.ui.le_targetSize.setValidator(self.posDoubleVal)
        self.ui.le_targetSize.editingFinished.connect(lambda: self.updateHelper())
        self.ui.le_N1_layout.setValidator(self.intVal)
        self.ui.le_N1_layout.editingFinished.connect(lambda: self.updateHelper(self.ui.le_N1_layout.text()))
        self.ui.le_planets.setValidator(self.intVal)
        self.ui.le_planets.editingFinished.connect(lambda: self.updateHelper(self.ui.le_N1_layout.text()))

        self.ui.pb_calcGearSizes.clicked.connect(lambda: self.updateHelper())

        # list of layout options
        rb_list = self.ui.bg_layout.buttons()
        for button in rb_list:
            button.clicked.connect(lambda: self.updateHelper(self.ui.le_N1_layout.text()))
        # number of planets
        planet_list = self.ui.bg_planets.buttons()
        for button in planet_list:
            button.clicked.connect(lambda: self.updateHelper(self.ui.le_N1_layout.text()))
        # use layout button
        self.ui.pb_useLayout.clicked.connect(lambda: self.useLayout())

        # Second tab
        #################
        self.ui.cb_type_design.currentIndexChanged.connect(lambda: self.setType(self.ui.cb_type_design.currentIndex()))
        self.ui.cb_input_GD.currentIndexChanged.connect(lambda: self.updatePlanetaryInput(self.ui.cb_input_GD, self.ui.cb_output_GD))
        self.ui.cb_output_GD.currentIndexChanged.connect(lambda: self.updatePlanetaryInput(self.ui.cb_input_GD, self.ui.cb_output_GD))

        self.ui.le_mod.setValidator(self.posDoubleVal)
        self.ui.le_mod.editingFinished.connect(lambda: self.updateGears())

        self.ui.le_PA_deg.setValidator(self.posDoubleVal)
        self.ui.le_PA_deg.editingFinished.connect(lambda: self.updateGears())

        self.ui.cb_CD_bkl.currentIndexChanged.connect(lambda: self.swapBklandCD())
        self.ui.le_CD_bkl1.editingFinished.connect(lambda: self.updateGears())

        self.ui.le_bkl2.setValidator(self.posDoubleVal)
        self.ui.le_bkl2.editingFinished.connect(lambda: self.updateGears())

        self.ui.le_NPlanets.setValidator(self.intVal)
        self.ui.le_NPlanets.editingFinished.connect(lambda: self.updateGears())

        self.ui.le_N1.setValidator(self.intVal)
        self.ui.le_N1.editingFinished.connect(lambda: self.updateGears())
        self.ui.le_N2.setValidator(self.intVal)
        self.ui.le_N2.editingFinished.connect(lambda: self.updateGears())

        self.ui.le_x1.setValidator(self.negDoubleVal)
        self.ui.le_x1.editingFinished.connect(lambda: self.updateGears())
        self.ui.le_x2.setValidator(self.negDoubleVal)
        self.ui.le_x2.editingFinished.connect(lambda: self.updateGears())
        self.ui.le_x3.setValidator(self.negDoubleVal)
        self.ui.le_x3.editingFinished.connect(lambda: self.updateGears())

        self.ui.le_Ro1.setValidator(self.posDoubleVal)
        self.ui.le_Ro1.editingFinished.connect(lambda: self.updateGears())
        self.ui.le_Ro2.setValidator(self.posDoubleVal)
        self.ui.le_Ro2.editingFinished.connect(lambda: self.updateGears())
        self.ui.le_Ro3.setValidator(self.posDoubleVal)
        self.ui.le_Ro3.editingFinished.connect(lambda: self.updateGears())

        self.ui.le_Rtip1.setValidator(self.posDoubleVal)
        self.ui.le_Rtip1.editingFinished.connect(lambda: self.updateGears())
        self.ui.le_Rtip2.setValidator(self.posDoubleVal)
        self.ui.le_Rtip2.editingFinished.connect(lambda: self.updateGears())
        self.ui.le_Rtip3.setValidator(self.posDoubleVal)
        self.ui.le_Rtip3.editingFinished.connect(lambda: self.updateGears())

        self.ui.le_Rr2.setValidator(self.posDoubleVal)
        self.ui.le_Rr2.editingFinished.connect(lambda: self.updateGears())
        self.ui.le_Rrim.setValidator(self.posDoubleVal)
        self.ui.le_Rrim.editingFinished.connect(lambda: self.updateGears())

        self.ui.le_rtcl1.setValidator(self.posDoubleVal)
        self.ui.le_rtcl1.editingFinished.connect(lambda: self.updateGears())
        self.ui.le_rtcl2.setValidator(self.posDoubleVal)
        self.ui.le_rtcl2.editingFinished.connect(lambda: self.updateGears())
        self.ui.le_rtcl3.setValidator(self.posDoubleVal)
        self.ui.le_rtcl3.editingFinished.connect(lambda: self.updateGears())

        self.ui.le_Rf1.setValidator(self.posDoubleVal)
        self.ui.le_Rf1.editingFinished.connect(lambda: self.updateGears())
        self.ui.le_Rf2.setValidator(self.posDoubleVal)
        self.ui.le_Rf2.editingFinished.connect(lambda: self.updateGears())
        self.ui.le_Rf3.setValidator(self.posDoubleVal)
        self.ui.le_Rf3.editingFinished.connect(lambda: self.updateGears())

        # draw gear button
        self.ui.pb_drawGear.clicked.connect(lambda: draw.drawAllGears(self, _updateAxes=True))

        # single tooth view checkboxes
        self.ui.cb_singleViewG1.checkStateChanged.connect(lambda: draw.drawGear(self, self.G1, _updateAxes=True))
        self.ui.cb_singleViewG2.checkStateChanged.connect(lambda: draw.drawGear(self, self.G2, _updateAxes=True))
        self.ui.cb_singleViewG3.checkStateChanged.connect(lambda: draw.drawGear(self, self.G3, _updateAxes=True))
        self.ui.cb_singleViewMesh.checkStateChanged.connect(lambda: self.toggleMeshView(self.ui.cb_singleViewMesh.isChecked()))
        self.ui.rb_sp.toggled.connect(lambda: draw.drawMesh(self, _updateAxes=True))
        self.ui.rb_pr.toggled.connect(lambda: draw.drawMesh(self, _updateAxes=True))

        # circles checkboxes
        self.ui.cb_circlesG1.checkStateChanged.connect(lambda: draw.drawGear(self, self.G1, _updateAxes=False))
        self.ui.cb_circlesG2.checkStateChanged.connect(lambda: draw.drawGear(self, self.G2, _updateAxes=False))
        self.ui.cb_circlesG3.checkStateChanged.connect(lambda: draw.drawGear(self, self.G3, _updateAxes=False))
        self.ui.cb_circlesMesh.checkStateChanged.connect(lambda: draw.drawMesh(self, _updateAxes=False))

        # LoC checkbox
        self.ui.cb_LoC.checkStateChanged.connect(lambda: draw.drawMesh(self, _updateAxes=False))

        # mesh slider
        self.ui.hSlider_Mesh.valueChanged.connect(lambda: draw.drawMesh(self, _updateAxes=False))

        # animate button
        self.ui.pb_animate.clicked.connect(lambda: draw.createAnimWindow(self))

        # Stress tab
        #################
        self.ui.le_FW1.setValidator(self.posDoubleVal)
        self.ui.le_FW2.setValidator(self.posDoubleVal)
        self.ui.le_RPM.setValidator(self.posDoubleVal)
        self.ui.le_torque.setValidator(self.posDoubleVal)
        self.ui.le_E1.setValidator(self.posDoubleVal)
        self.ui.le_E2.setValidator(self.posDoubleVal)
        self.ui.le_nu1.setValidator(self.posDoubleVal)
        self.ui.le_nu2.setValidator(self.posDoubleVal)

        # stress button
        self.ui.pb_stress.clicked.connect(lambda: self.updateStress())

    def toggleMeshView(self, _checked):
        if _checked:
            self.ui.rb_sp.setEnabled(True)
            self.ui.rb_pr.setEnabled(True)
        else:
            self.ui.rb_sp.setEnabled(False)
            self.ui.rb_pr.setEnabled(False)
        draw.drawMesh(self, _updateAxes=True)

    def setupShortcuts(self):
        # cycle tabs
        self.SC_cycleTabFW = QShortcut(QKeySequence("PgDown"), self)
        self.SC_cycleTabFW.activated.connect(lambda: self.cycleTab(dir='forward'))
        self.SC_cycleTabRV = QShortcut(QKeySequence("PgUp"), self)
        self.SC_cycleTabRV.activated.connect(lambda: self.cycleTab(dir='backward'))
        # draw gears
        self.SC_drawGear = QShortcut(QKeySequence("Ctrl+D"), self)
        self.SC_drawGear.activated.connect(lambda: draw.drawAllGears(self, _updateAxes=True))

    def cycleTab(self, dir='forward'):
        tabs = self.ui.tabW_main

        if dir=='forward':
            newIndex = (tabs.currentIndex()+1) % tabs.count()
            tabs.setCurrentIndex(newIndex)
        elif dir=='backward':
            newIndex = (tabs.currentIndex()-1) % tabs.count()
            tabs.setCurrentIndex(newIndex)

    def resetMeshParams(self):
        # mesh parameters
        self.mod = -1                   # module
        self.PA_deg = 20                # pressure angle, degrees
        self.PA = deg2rad(self.PA_deg)  # pressure angle, radians
        self.OPA1_deg = -1              # operating pressure angle, degrees
        self.OPA1 = -1                  # operating pressure angle, radians
        self.OPA2_deg = -1              # operating pressure angle, degrees
        self.OPA2 = -1                  # operating pressure angle, radians
        self.bkl1 = 0                   # backlash
        self.bkl2 = 0
        self.rtcl1 = 0                  # root clearances
        self.rtcl2 = 0
        self.rtcl3 = 0
        self.CD = -1                    # center distance
        self.CR1 = 0                    # contact ratio
        self.CR2 = 0
        self.NPlanets = 1               # number of planets
        self.RPM = 1                    # pinion speed
        self.torque = 1                 # pinion torque

    def initGearDesignFields(self):
        # Called on startup and whenever a file is loaded

        # gear design tab
        if self.mod > 0:
            if self.units.modMult == "M":
                setText(self.ui.le_mod, self.mod, 1, "{:.1f}")
            elif self.units.modMult == "T":
                setText(self.ui.le_mod, 25.4/self.mod, 1, "{:.1f}")

        setText(self.ui.le_PA_deg, self.PA_deg, 1, "{:.1f}")

        setText(self.ui.le_CD_bkl1, self.bkl1, self.units.lenMult, self.units.lenFormat)
        setText(self.ui.le_bkl2, self.bkl2, self.units.lenMult, self.units.lenFormat)
        self.swapBklandCD()

        setText(self.ui.le_NPlanets, self.NPlanets, 1, "{:.0f}")

        if self.G1.N > 0:
            setText(self.ui.le_N1, self.G1.N, 1, "{:.0f}")
        if self.G2.N > 0:
            setText(self.ui.le_N2, self.G2.N, 1, "{:.0f}")
        if self.G3.N > 0:
            setText(self.ui.lb_N3, self.G3.N, 1, "{:.0f}")

        setText(self.ui.le_x1, self.G1.x, 1, self.units.lenFormat)
        setText(self.ui.le_x2, self.G2.x, 1, self.units.lenFormat)
        setText(self.ui.le_x3, self.G3.x, 1, self.units.lenFormat)

        if self.G1.Ro >= 0:
            setText(self.ui.le_Ro1, self.G1.Ro, self.units.lenMult, self.units.lenFormat)
        if self.G2.Ro >= 0:
            setText(self.ui.le_Ro2, self.G2.Ro, self.units.lenMult, self.units.lenFormat)
        if self.G3.Ro >= 0:
            setText(self.ui.le_Ro3, self.G3.Ro, self.units.lenMult, self.units.lenFormat)

        setText(self.ui.le_Rtip1, self.G1.Rtip, self.units.lenMult, self.units.lenFormat)
        setText(self.ui.le_Rtip2, self.G2.Rtip, self.units.lenMult, self.units.lenFormat)
        setText(self.ui.le_Rtip3, self.G3.Rtip, self.units.lenMult, self.units.lenFormat)

        setText(self.ui.le_Rrim, self.G2.Rrim, self.units.lenMult, self.units.lenFormat)

        if self.rtcl1 >= 0:
            setText(self.ui.le_rtcl1, self.rtcl1, self.units.lenMult, self.units.lenFormat)
        if self.rtcl2 >= 0:
            setText(self.ui.le_rtcl2, self.rtcl2, self.units.lenMult, self.units.lenFormat)
        if self.rtcl3 >= 0:
            setText(self.ui.le_rtcl3, self.rtcl3, self.units.lenMult, self.units.lenFormat)

        setText(self.ui.le_Rf1, self.G1.Rf, self.units.lenMult, self.units.lenFormat)
        setText(self.ui.le_Rf2, self.G2.Rf, self.units.lenMult, self.units.lenFormat)
        setText(self.ui.le_Rf3, self.G3.Rf, self.units.lenMult, self.units.lenFormat)

        # mesh slider
        self.sliderScale = 100    # the slider can only handle ints, show scale up everthing
        self.ui.hSlider_Mesh.setMinimum(0)
        self.ui.hSlider_Mesh.setMaximum(2*self.sliderScale)
        self.ui.hSlider_Mesh.setSliderPosition(1*self.sliderScale)    # pitch point happens at slider = 1

        # stress tab
        setText(self.ui.le_FW1, self.G1.FW, self.units.lenMult, self.units.lenFormat)
        setText(self.ui.le_FW2, self.G2.FW, self.units.lenMult, self.units.lenFormat)
        setText(self.ui.le_FW3, self.G3.FW, self.units.lenMult, self.units.lenFormat)

        setText(self.ui.le_E1, self.G1.E, self.units.pressureMult, "{:.0f}")
        setText(self.ui.le_E2, self.G2.E, self.units.pressureMult, "{:.0f}")
        setText(self.ui.le_E3, self.G3.E, self.units.pressureMult, "{:.0f}")

        setText(self.ui.le_nu1, self.G1.nu, 1)
        setText(self.ui.le_nu2, self.G2.nu, 1)
        setText(self.ui.le_nu3, self.G3.nu, 1)

        setText(self.ui.le_RPM, self.RPM, 1, "{:.0f}")
        setText(self.ui.le_torque, self.torque, self.units.torqueMult, "{:.0f}")

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

    def setType(self, _type):
        self.type = Type(_type)

        # reset dimensions
        self.resetMeshParams()
        self.initGearDesignFields()

        # clear drawings
        self.canvasHelper.axes.cla()
        self.canvasG1.axes.cla()
        self.canvasG2.axes.cla()
        self.canvasG3.axes.cla()
        self.canvasMesh.axes.cla()
        self.canvasHelper.draw()
        self.canvasG1.draw()
        self.canvasG2.draw()
        self.canvasG3.draw()
        self.canvasMesh.draw()

        # update UI
        match self.type:
            case Type.external:
                self.G2.type = "external"
                if len(self.gearList) > 2:
                    self.gearList.pop()
                self.hidePlanets()

                # helper tab
                self.ui.cb_type_helper.setCurrentIndex(0)
                self.ui.lb_pinion.setText("Pinion")
                self.ui.lb_gear.setText("Gear")

                # design tab
                self.ui.cb_type_design.setCurrentIndex(0)
                self.ui.lb_G1.setText("Pinion")
                self.ui.lb_G2.setText("Gear")
                self.ui.lb_Rrim_text.hide()
                self.ui.lb_Rrim_unit.hide()
                self.ui.le_Rrim.hide()
                self.ui.le_Ro2.setEnabled(True)
                self.ui.le_Rr2.setEnabled(False)

                self.ui.tabW_GD.setTabText(0, "Pinion")
                self.ui.tabW_GD.setTabText(2, "Gear")

                # stress tab
                self.ui.lb_stressG1.setText("Pinion")
                self.ui.lb_stressG2.setText("Gear")

                self.ui.tabW_stress.setTabText(0, "Pinion / Gear")

            case Type.internal:
                self.G2.type = "internal"
                if len(self.gearList) > 2:
                    self.gearList.pop()
                self.hidePlanets()

                # helper tab
                self.ui.cb_type_helper.setCurrentIndex(1)
                self.ui.lb_pinion.setText("Pinion")
                self.ui.lb_gear.setText("Ring")

                # design tab
                self.ui.cb_type_design.setCurrentIndex(1)
                self.ui.lb_G1.setText("Pinion")
                self.ui.lb_G2.setText("Ring")
                self.ui.lb_Rrim_text.show()
                self.ui.lb_Rrim_unit.show()
                self.ui.le_Rrim.show()
                setText(self.ui.le_Rrim, self.G2.Rrim, self.units.lenMult, self.units.lenFormat)
                self.ui.le_Ro2.setEnabled(False)
                self.ui.le_Rr2.setEnabled(True)

                self.ui.tabW_GD.setTabText(0, "Pinion")
                self.ui.tabW_GD.setTabText(2, "Ring")

                # stress tab
                self.ui.lb_stressG1.setText("Pinion")
                self.ui.lb_stressG2.setText("Ring")

                self.ui.tabW_stress.setTabText(0, "Pinion / Ring")

            case Type.planetary:
                self.G2.type = "internal"
                self.G3.type = "external"
                if len(self.gearList) < 3:
                    self.gearList.append(self.G3)
                self.showPlanets()

                # helper tab
                self.ui.cb_type_helper.setCurrentIndex(2)
                self.ui.lb_pinion.setText("Sun")
                self.ui.lb_gear.setText("Ring")

                # design tab
                self.ui.cb_type_design.setCurrentIndex(2)
                self.ui.lb_G1.setText("Sun")
                self.ui.lb_G2.setText("Ring")
                self.ui.lb_G3.setText("Planet")
                self.ui.lb_Rrim_text.show()
                self.ui.lb_Rrim_unit.show()
                self.ui.le_Rrim.show()
                setText(self.ui.le_Rrim, self.G2.Rrim, self.units.lenMult, self.units.lenFormat)
                self.ui.le_Ro2.setEnabled(False)
                self.ui.le_Rr2.setEnabled(False)

                self.ui.tabW_GD.setTabText(0, "Sun")
                self.ui.tabW_GD.setTabText(1, "Planet")
                self.ui.tabW_GD.setTabText(2, "Ring")

                # stress tab
                self.ui.lb_stressG1.setText("Sun")
                self.ui.lb_stressG2.setText("Ring")
                self.ui.lb_stressG3.setText("Planet")

                self.ui.tabW_stress.setTabText(0, "Pinion / Planet")
                self.ui.tabW_stress.setTabText(1, "Planet / Ring")

        # if self.ui.tabW_main.currentIndex() == 0: # layout helper tab
        #     self.ui.cb_type_design.setCurrentIndex(self.type.value)

        # if self.ui.tabW_main.currentIndex() == 1: # design tab
        #     self.ui.cb_type_helper.setCurrentIndex(self.type.value)

    def hidePlanets(self):
        # layout tab
        self.ui.frame_planets.hide()
        self.ui.frame_pLayout_helper.hide()
        self.ui.frame_pLayout_GD.hide()

        self.ui.lb_planet.hide()
        for label in self.N3_label_list:
            label.hide()

        self.ui.cb_CD_width.view().setRowHidden(0, False)

        # designer tab
        for label in self.G3LabelList:
            label.hide()
        self.ui.cb_CD_bkl.setItemText(0, "Backlash")
        self.ui.le_x2.setEnabled(True)
        self.ui.tabW_GD.setTabVisible(1, False)

        # stress tab
        self.ui.tabW_stress.setTabVisible(1, False)

    def showPlanets(self):
        # layout tab
        self.ui.frame_planets.show()
        self.ui.frame_pLayout_helper.show()
        self.ui.frame_pLayout_GD.show()

        self.ui.lb_planet.show()
        for label in self.N3_label_list:
            label.show()

        self.ui.cb_input_helper.setCurrentIndex(-1)
        self.ui.cb_output_helper.setCurrentIndex(-1)
        self.ui.lb_stationGear1.setText("-")
        self.ui.lb_stationGear2.setText("-")
        self.ui.cb_CD_width.setCurrentIndex(1)
        self.ui.cb_CD_width.view().setRowHidden(0, True)

        # designer tab
        for label in self.G3LabelList:
            label.show()
        self.ui.cb_CD_bkl.setItemText(0, "Backlash, Sun-Planet")
        self.ui.le_x2.setEnabled(False)
        self.ui.tabW_GD.setTabVisible(1, True)

        # stress tab
        self.ui.tabW_stress.setTabVisible(1, True)

    def swapBklandCD(self):
        # input backlash
        if self.ui.cb_CD_bkl.currentIndex() == 0:
            setText(self.ui.le_CD_bkl1, self.bkl1, self.units.lenMult, self.units.lenFormat)

            self.ui.lb_bkl_text.hide()
            self.ui.lb_bkl_unit.hide()
            self.ui.lb_bkl_value.hide()

            self.ui.lb_CD_text.show()
            self.ui.lb_CD_unit.show()
            self.ui.lb_CD_value.show()

            if self.CD > 0:
                setText(self.ui.lb_CD_value, self.CD, self.units.lenMult, self.units.lenFormat)

        # input center distance
        elif self.ui.cb_CD_bkl.currentIndex() == 1:
            setText(self.ui.le_CD_bkl1, self.CD, self.units.lenMult, self.units.lenFormat)

            self.ui.lb_CD_text.hide()
            self.ui.lb_CD_unit.hide()
            self.ui.lb_CD_value.hide()

            self.ui.lb_bkl_text.show()
            self.ui.lb_bkl_unit.show()
            self.ui.lb_bkl_value.show()
            setText(self.ui.lb_bkl_value, self.bkl1, self.units.lenMult, self.units.lenFormat)

    def updatePlanetaryInput(self, _inputWidget, _outputWidget):
        inputIndex = _inputWidget.currentIndex()
        if inputIndex >=0:
            for i in range(_outputWidget.model().rowCount()):
                _outputWidget.model().item(i).setEnabled(True)
            _outputWidget.model().item(inputIndex).setEnabled(False)

        if _outputWidget.currentIndex() == inputIndex:
            _outputWidget.setCurrentIndex((inputIndex+1)%3)

        self.updatePlanetaryOutput(_inputWidget, _outputWidget)

    def updatePlanetaryOutput(self, _inputWidget, _outputWidget):
        inputIndex = _inputWidget.currentIndex()
        outputIndex = _outputWidget.currentIndex()
        if inputIndex >= 0 and outputIndex >= 0:
            text = ["Sun", "Planet Carrier", "Ring"]
            self.ui.lb_stationGear1.setText(text[3 - (inputIndex + outputIndex)])
            self.ui.lb_stationGear2.setText(text[3 - (inputIndex + outputIndex)])

        if self.ui.tabW_main.currentIndex() == 0:   # layout tab
            self.updateHelper()
        if self.ui.tabW_main.currentIndex() == 1:   # design tab
            self.updateGears()

# Helper Tab ##################################################################
    def maxPlanets(self, _N1, _N3):
        return int( ( pi / ( pi/2 - ( arccos((_N3+2)/(_N1+_N3)) ) ) ) )

    def findN1(self, _N2, _GR):
        # find number of teeth on sun gear for given gear ratio
        # and ring gear size where:
        # N1 = NS and N2 = NR
        input = self.ui.cb_input_helper.currentIndex()
        output = self.ui.cb_output_helper.currentIndex()
        if input < 0:
            showMessage(self.ui.cb_input_helper, _text='Choose an input', _palette=self.errorPalette)
            return
        if output < 0:
            showMessage(self.ui.cb_output_helper, _text='Choose an output', _palette=self.errorPalette)
            return

        match input:
            case 0:
                match output:
                    case 1: # sun - planet
                        N1 = _N2/(_GR-1)
                    case 2: # sun - ring
                        N1 = _N2/_GR
            case 1:
                match output:
                    case 0: # planet - sun
                        N1 = _N2*_GR/(1-_GR)
                    case 2: # planet - ring
                        N1 = _N2/_GR - _N2
            case 2:
                match output:
                    case 0: # ring - sun
                        N1 = _N2*_GR
                    case 1: # ring - planet
                        N1 = _N2*_GR - _N2
        return round(N1)

    def findN2(self, _N1, _GR):
        if self.type == Type.external or self.type == Type.internal:
            return round(_N1 * _GR)

        # find number of teeth on ring gear for given gear ratio
        # and sun gear size where:
        # N1 = NS and N2 = NR
        input = self.ui.cb_input_helper.currentIndex()
        output = self.ui.cb_output_helper.currentIndex()
        if input < 0:
            showMessage(self.ui.cb_input_helper, _text='Select an input', _palette=self.errorPalette)
            return
        if output < 0:
            showMessage(self.ui.cb_output_helper, _text='Select an output', _palette=self.errorPalette)
            return

        match input:
            case 0:
                match output:
                    case 1: # sun - planet
                        N2 = (_N1*_GR)-_N1
                    case 2: # sun - ring
                        N2 = _N1*_GR
            case 1:
                match output:
                    case 0: # planet - sun
                        N2 = (_N1/_GR)-_N1
                    case 2: # planet - ring
                        N2 = _N1/(1/_GR - 1)
            case 2:
                match output:
                    case 0: # ring - sun
                        N2 = _N1/_GR
                    case 1: # ring - planet
                        N2 = _N1/(_GR-1)
        return round(N2)

    def findGR(self, _N1, _N2):
        if self.type == Type.external or self.type == Type.internal:
            return _N2 / _N1

        # find gear ratio from given sun gear and ring gear where:
        # N1 = NS and N2 = NR

        """
        Input   output  ratio
        S       P       (S+R)/S
        S       R       R/S
        P       S       S/(S+R)
        P       R       R/(S+R)
        R       S       S/R
        R       P       (S+R)/R
        """
        if self.ui.tabW_main.currentIndex() == 0: # layout helper tab
            input = self.ui.cb_input_helper.currentIndex()
            output = self.ui.cb_output_helper.currentIndex()
        if self.ui.tabW_main.currentIndex() == 1: # design tab
            input = self.ui.cb_input_GD.currentIndex()
            output = self.ui.cb_output_GD.currentIndex()

        if input < 0 or output < 0:
            return

        match input:
            case 0:
                match output:
                    case 1: # sun - planet
                        GR = (_N1+_N2)/_N1
                    case 2: # sun - ring
                        GR = _N2/_N1
            case 1:
                match output:
                    case 0: # planet - sun
                        GR = _N1/(_N1+_N2)
                    case 2: # planet - ring
                        GR = _N2/(_N1+_N2)
            case 2:
                match output:
                    case 0: # ring - sun
                        GR = _N1/_N2
                    case 1: # ring - planet
                        GR = (_N1+_N2)/_N2
        return GR

    def updateHelper(self, _N1=None):
        if is_number(_N1):
            try:
                N1 = int(_N1)
                GR = float(self.ui.le_targetGR.text())
            except:
                # print("[updateHelper] bad N1 or GR")
                return
            N2 = self.findN2(N1, GR)
        else:
            N1, N2 = self.findGearSizes()

        if N2 is None:
            # print("[updateHelper] bad return from [findGearSizes]")
            return

        if self.populateChart(N1, N2): return

        N1, N2, N3 = self.getLayoutOption()

        p = 0
        if self.type == Type.planetary:
            self.populatePlanets(N1, N2)
            p = self.getPlanetsOption()

        for N in [N1, N2, N3, p]:
            if N is None:
                # print("[updateHelper] bad return from [getLayoutOption]")
                return

        draw.drawHelper(self, N1, N2, N3, p)

    def findGearSizes(self):
        try:
            if self.units.modMult == "M":
                mod = float(self.ui.le_targetMod.text())
            elif self.units.modMult == "T":
                mod = 25.4 / float(self.ui.le_targetMod.text())
            GR = float(self.ui.le_targetGR.text())
            size = float(self.ui.le_targetSize.text()) * self.units.lenMult
        except:
            # print("[findGearSizes] bad mod/GR/size")
            return None, None

        match self.type:
            case Type.external:
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

                    setText(self.ui.le_N1_layout, N1, 1, "{:.0f}")
                    setText(self.ui.lb_N2_3, N2, 1, "{:.0f}")

                    return N1, N2
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

                    setText(self.ui.le_N1_layout, N1, 1, "{:.0f}")
                    setText(self.ui.lb_N2_3, N2, 1, "{:.0f}")

                    return N1, N2

            case Type.internal:
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

                    setText(self.ui.le_N1_layout, N1, 1, "{:.0f}")
                    setText(self.ui.lb_N2_3, N2, 1, "{:.0f}")

                    return N1, N2
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

                    setText(self.ui.le_N1_layout, N1, 1, "{:.0f}")
                    setText(self.ui.lb_N2_3, N2, 1, "{:.0f}")

                    return N1, N2

            case Type.planetary:
                NR = round((size - 2*mod)/mod)
                NS = self.findN1(NR, GR)
                if NS:
                    setText(self.ui.le_N1_layout, NS, 1, "{:.0f}")
                    setText(self.ui.lb_N2_3, NR, 1, "{:.0f}")

                return NS, NR

            case _: # something went wrong, no type set
                return None, None

    def populateChart(self, _N1, _N2):
        try:
            if self.units.modMult == "M":
                mod = float(self.ui.le_targetMod.text())
            elif self.units.modMult == "T":
                mod = 25.4 / float(self.ui.le_targetMod.text())
        except:
            # print("[populateChart] bad mod")
            return 1

        # make sure planetary type is set
        if self.type == Type.planetary:
            if self.ui.cb_input_helper.currentIndex() < 0 or self.ui.cb_output_helper.currentIndex() < 0:
                # print("[populateChart] no planetary type set")
                return 1

        # display gear options
        N2_list = list(range(_N2-2, _N2+3))

        for N2, N2_label, N3_label, icon, rb in zip(N2_list, self.N2_label_list, self.N3_label_list, self.icon_label_list, self.radio_button_list):
            setText(N2_label, N2, 1, "{:.0f}")

            if self.type == Type.planetary:
                N3 = (N2 - _N1)/2

                format = "{:.0f}"
                palette = QPalette(self.defaultPalette)
                if N3 != int(N3):
                    format = "{:.1f}"
                    palette.setColor(QPalette.WindowText, Qt.red)
                    icon.setPixmap(self.bad_pixmap)

                else:
                    if np.gcd(_N1, int(N3)) == 1 and np.gcd(int(N3), N2) == 1:
                        icon.setPixmap(self.good_pixmap)
                    else:
                        icon.setPixmap(self.bad_pixmap)

                N3_label.setPalette(palette)
                setText(N3_label, N3, 1, format)

            else:   # external or internal
                if np.gcd(_N1, N2) == 1:
                    icon.setPixmap(self.good_pixmap)
                else:
                    icon.setPixmap(self.bad_pixmap)

        for N2, GR_label, CD_label, width_label in zip(N2_list, self.GR_label_list, self.CD_label_list, self.width_label_list):
            GR = self.findGR(_N1, N2)
            setText(GR_label, GR, 1, "{:.3f}")

            Ros1 = mod * (_N1 + 2)/2
            if self.type == Type.external:
                CD = mod * (_N1 + N2)/2
                Ros2 = mod * (N2 + 2)/2
                width = Ros1 + CD + Ros2
            elif self.type == Type.internal or self.type == Type.planetary:
                CD = mod * (N2 - _N1)/2
                Ros2 = mod * (N2 + 2 + 3)/2 # add an addition 3*mod for the rim thickness
                width = 2 * Ros2
            setText(CD_label, CD, self.units.lenMult, self.units.lenFormat)
            setText(width_label, width, self.units.lenMult, self.units.lenFormat)

    def populatePlanets(self, _N1, _N2):
        try:
            planets = int(self.ui.le_planets.text())
        except:
            planets = 4
            setText(self.ui.le_planets, planets, 1, "{:.0f}")

        N3 = (_N2 - _N1)/2
        max = self.maxPlanets(_N1, N3)
        if planets > max:
            planets = max
            setText(self.ui.le_planets, planets, 1, "{:.0f}")

        planets_list = list(range(planets-2, planets+3))

        for NP, label, icon in zip(planets_list, self.planets_label_list, self.planets_icon_list):
            # non-integer number of planet teeth
            if N3 != int(N3):
                setText(label, None, 1, "{:.0f}")
                icon.clear()
                continue
            # don't divide by zero
            if NP < 1:
                setText(label, '-')
                icon.clear()
                continue
            if NP > max:
                setText(label, '-')
                icon.clear()
                continue
            if (_N1+_N2)/NP == int((_N1+_N2)/NP):
                setText(label, NP, 1, "{:.0f}")
                icon.setPixmap(self.good_pixmap)
            else:
                setText(label, NP, 1, "{:.0f}")
                icon.setPixmap(self.bad_pixmap)

    def getLayoutOption(self):
        for R, P, radioButton in zip(self.N2_label_list, self.N3_label_list, self.radio_button_list):
            if radioButton.isChecked():
                N2 = R.text()
                N3 = P.text()
                break

        try:
            N1 = int(self.ui.le_N1_layout.text())
        except:
            # print("bad N1")
            N1 = None
        try:
            N2 = int(N2)
        except:
            # print("bad N2")
            N2 = None
        if self.type == Type.planetary:
            try:
                N3 = int(N3)
            except:
                # print("bad N3")
                N3 = None
        else:
            N3 = 0

        return N1, N2, N3

    def getPlanetsOption(self):
        NP = None
        for label, radioButton in zip(self.planets_label_list, self.rb_planets_list):
            if radioButton.isChecked():
                NP = label.text()
                break

        try:
            NP = int(NP)
        except:
            # print("bad NP")
            NP = None

        return NP

    def useLayout(self):
        mod = self.ui.le_targetMod.text()
        if is_number(mod):
            self.ui.le_mod.setText(mod)
        else:
            showMessage(self.ui.le_targetMod, _text='Enter a module', _palette=self.errorPalette)
            return

        N1 = self.ui.le_N1_layout.text()
        if is_number(N1):
            self.ui.le_N1.setText(N1)
        else:
            showMessage(self.ui.pb_calcGearSizes, _text='Choose gear sizes', _palette=self.errorPalette)
            return

        N2 = ''
        for N, radioButton in zip(self.N2_label_list, self.radio_button_list):
            if radioButton.isChecked():
                N2 = int(N.text())
                break

        if is_number(N2):
            self.ui.le_N2.setText(str(N2))
        else:
            showMessage(self.ui.pb_calcGearSizes, _text='Choose gear sizes', _palette=self.errorPalette)
            return

        if self.type == Type.planetary:
            if self.ui.cb_input_helper.currentIndex() == -1:
                showMessage(self.ui.cb_input_helper, _text='Choose an input', _palette=self.errorPalette)
                return
            else:
                self.ui.cb_input_GD.setCurrentIndex(self.ui.cb_input_helper.currentIndex())

            if self.ui.cb_output_helper.currentIndex() == -1:
                showMessage(self.ui.cb_output_helper, _text='Choose an output', _palette=self.errorPalette)
                return
            else:
                self.ui.cb_output_GD.setCurrentIndex(self.ui.cb_output_helper.currentIndex())

            for N3_label, radioButton in zip(self.N3_label_list, self.radio_button_list):
                if radioButton.isChecked():
                    N3 = N3_label.text()
                    break
            try:
                N3 = int(N3)
            except:
                showMessage(N3_label, _text='Choose integer planet size', _palette=self.errorPalette)
                return

            NP = self.getPlanetsOption()
            # print("NP:", NP)
            if is_number(NP):
                self.ui.le_NPlanets.setText(str(NP))
            else:
                showMessage(self.ui.rb_p3, _text='Choose number of planets', _palette=self.errorPalette)
                return

        self.ui.tabW_main.setCurrentIndex(1)
        self.updateGears()

# Gear Design Tab #############################################################
    def updateGears(self):
        if self.get_N(): return 1
        if self.get_mod(): return 1
        if self.get_PA(): return 1
        if self.get_x(): return 1

        # calculate standard values
        self.updateBaseAndPitch()
        self.updateStandardToothThickness()
        self.calcStandardRtcl()

        # outer geometry
        if self.get_Ro(): return 1
        self.updateRomax()
        if self.get_Rtip(): return 1
        self.updateMaxTipRadius()
        self.updateRoe()

        if self.updateCenterDistance(): return 1

        # root geometry
        if self.get_rtcl(): return 1
        if self.get_Rr(): return 1
        if self.get_Rrim(): return 1
        self.updateRootRadius()
        if self.get_Rf(): return 1
        self.updateMaxRootFillet()

        self.checkUndercut()
        self.updateJFI()

        self.updateContactRatio()

    def get_N(self):
        N1 = getValue(self.ui.le_N1, _type=int)
        if N1:
            self.G1.N = N1
        else:
            # print("no N1")
            return 1
        N2 = getValue(self.ui.le_N2, _type=int)
        if N2:
            self.G2.N = N2
        else:
            # print("no N2")
            return 1
        if self.type == Type.planetary:
            N3 = (N2 - N1)/2
            if N3 != int(N3):
                palette = QPalette(self.defaultPalette)
                palette.setColor(QPalette.WindowText, Qt.red)
                self.ui.lb_N3.setPalette(palette)
                setText(self.ui.lb_N3, N3, 1, _format = "{:.1f}")
                # print("non-int N3")
                return 1
            else:
                self.G3.N = int(N3)
                self.ui.lb_N3.setPalette(self.defaultPalette)
                setText(self.ui.lb_N3, N3, 1, _format = "{:.0f}")

            maxP = self.maxPlanets(N1, N3)
            setText(self.ui.lb_max_planets, maxP, _format = "{:.0f}")

            NP = getValue(self.ui.le_NPlanets, _type=int)
            if NP:
                if NP > maxP:
                    NP = maxP
                self.NPlanets = NP
                setText(self.ui.le_NPlanets, NP, _format = "{:.0f}")

                # check for even spacing
                if (N1+N2)/NP == int((N1+N2)/NP):
                    self.ui.lb_icon_spacing.setPixmap(self.good_pixmap)
                else:
                    self.ui.lb_icon_spacing.setPixmap(self.bad_pixmap)

            else:
                # print("no NPlanets")
                return 1

        if self.G1.N < 1 or self.G2.N < 1:
            # print("N1 < 1 or N2 < 1")
            return 1

        # gear ratio
        GR = self.findGR(self.G1.N, self.G2.N)
        if GR:
            setText(self.ui.lb_GR, GR)

    def get_mod(self):
        mod = getValue(self.ui.le_mod)
        if mod:
            match self.units.modMult:
                case "M":
                    self.mod = mod
                case "T":
                    self.mod = 25.4 / mod
        else:
            # print("no mod")
            return 1

    def get_PA(self):
        PA_deg = getValue(self.ui.le_PA_deg)
        if PA_deg:
            self.PA_deg = PA_deg
            self.PA = deg2rad(self.PA_deg)
        else:
            # print("no PA")
            return 1

    def get_x(self):
        x1 = getValue(self.ui.le_x1)
        if x1 is not None:
            self.G1.x = x1
        else:
            # print("no x1")
            return 1
        x2 = getValue(self.ui.le_x2)
        if x2 is not None:
            self.G2.x = x2
        else:
            # print("no x2")
            return 1
        if self.type == Type.planetary:
            x3 = getValue(self.ui.le_x3)
            if x3 is not None:
                self.G3.x = x3
            else:
                # print("no x3")
                return 1

    def get_Ro(self):
        Ro1 = getValue(self.ui.le_Ro1, self.units.lenMult)
        if Ro1 is not None:
            self.G1.Ro = Ro1
        else:
            # print("no Ro1")
            return 1
        Ro2 = getValue(self.ui.le_Ro2, self.units.lenMult)
        if Ro2 is not None:
            self.G2.Ro = Ro2
        else:
            # print("no Ro2")
            return 1
        if self.type == Type.planetary:
            Ro3 = getValue(self.ui.le_Ro3, self.units.lenMult)
            if Ro3 is not None:
                self.G3.Ro = Ro3
            else:
                # print("no Ro3")
                return 1

    def get_Rtip(self):
        Rtip1 = getValue(self.ui.le_Rtip1, self.units.lenMult)
        if Rtip1 is not None:
            self.G1.Rtip = Rtip1
        else:
            # print("no Rtip1")
            return 1
        Rtip2 = getValue(self.ui.le_Rtip2, self.units.lenMult)
        if Rtip2 is not None:
            self.G2.Rtip = Rtip2
        else:
            # print("no Rtip2")
            return 1
        if self.type == Type.planetary:
            Rtip3 = getValue(self.ui.le_Rtip3, self.units.lenMult)
            if Rtip3 is not None:
                self.G3.Rtip = Rtip3
            else:
                # print("no Rtip3")
                return 1

    def get_rtcl(self):
        rtcl1 = getValue(self.ui.le_rtcl1, self.units.lenMult)
        if rtcl1 is not None:
            self.rtcl1 = rtcl1
        else:
            # print("no rtcl1")
            return 1
        rtcl2 = getValue(self.ui.le_rtcl2, self.units.lenMult)
        if rtcl2 is not None:
            self.rtcl2 = rtcl2
        else:
            # print("no rtcl2")
            return 1
        if self.type == Type.planetary:
            rtcl3 = getValue(self.ui.le_rtcl3, self.units.lenMult)
            if rtcl3 is not None:
                self.rtcl3 = rtcl3
            else:
                # print("no rtcl3")
                return 1

    def get_Rr(self):
        if self.type == Type.external:
            return

        Rr = getValue(self.ui.le_Rr2, self.units.lenMult)
        if Rr:
            self.G2.Rr = Rr
        else:
            self.G2.Rr = self.G2.Rrs
            setText(self.ui.le_Rr2, self.G2.Rr, self.units.lenMult, self.units.lenFormat)
            # print("setting standard Rr")

    def get_Rf(self):
        Rf1 = getValue(self.ui.le_Rf1, self.units.lenMult)
        if Rf1 is not None:
            self.G1.Rf = Rf1
        else:
            # print("no Rf1")
            return 1

        Rf2 = getValue(self.ui.le_Rf2, self.units.lenMult)
        if Rf2 is not None:
            self.G2.Rf = Rf2
        else:
            # print("no Rf2")
            return 1

        if self.type == Type.planetary:
            Rf3 = getValue(self.ui.le_Rf3, self.units.lenMult)
            if Rf3 is not None:
                self.G3.Rf = Rf3
            else:
                # print("no Rf3")
                return 1

    def get_Rrim(self):
        if self.type == Type.external:
            return

        Rrim = getValue(self.ui.le_Rrim, self.units.lenMult)
        if Rrim:
            self.G2.Rrim = Rrim
        else:
            self.G2.Rrim = (self.mod * (self.G2.N+5)) / 2
            setText(self.ui.le_Rrim, self.G2.Rrim, self.units.lenMult, self.units.lenFormat)
            # print("setting default Rrim")

    def updateBaseAndPitch(self):
        for gear in self.gearList:
            gear.Rs = (self.mod * gear.N) / 2
            gear.Rb = gear.Rs * cos(self.PA)
            gear.Pb = tau * gear.Rb / gear.N
            gear.Ps = tau * gear.Rs / gear.N

            if gear.type == "external":
                gear.Ros = (self.mod * (gear.N+2)) / 2
            elif gear.type == "internal":
                gear.Ros = (self.mod * (gear.N+2.5)) / 2

            # update UI
            if gear.ID == 1:
                setText(self.ui.lb_Rs1, self.G1.Rs, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_Ros1, self.G1.Ros, self.units.lenMult, self.units.lenFormat)
            elif gear.ID == 2:
                setText(self.ui.lb_Rs2, self.G2.Rs, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_Ros2, self.G2.Ros, self.units.lenMult, self.units.lenFormat)
            elif gear.ID == 3:
                setText(self.ui.lb_Rs3, self.G3.Rs, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_Ros3, self.G3.Ros, self.units.lenMult, self.units.lenFormat)

    def updateStandardToothThickness(self):
        for gear in self.gearList:
            # GOIG 6.11
            gear.tts = self.mod * (pi/2 + 2*gear.x*tan(self.PA))
            if gear.ID == 1:
                setText(self.ui.lb_tts1, self.G1.tts, self.units.lenMult, self.units.lenFormat)
            elif gear.ID == 2:
                if gear.type == "external":
                    setText(self.ui.lb_tts2, self.G2.tts, self.units.lenMult, self.units.lenFormat)
                if gear.type == "internal":
                    setText(self.ui.lb_tts2, self.G2.Ps - self.G2.tts, self.units.lenMult, self.units.lenFormat)
            elif gear.ID == 3:
                setText(self.ui.lb_tts3, self.G3.tts, self.units.lenMult, self.units.lenFormat)

    def calcStandardRtcl(self):
        for gear in self.gearList:
            # standard root clearance
            addendum = self.mod
            rtcl = (0.25 * addendum)
            # standard root radius
            Rrs_ext = gear.Rs - addendum - rtcl
            Rrs_int = gear.Rs - addendum

            # bounds check
            if gear.type == "external":
                gear.Rrs = Rrs_ext
                if gear.Rr < 0 or gear.Rr > gear.Rs:
                    gear.Rr = gear.Rrs
            elif gear.type == "internal":
                gear.Rrs = Rrs_int
                if gear.Rr < gear.Rb:
                    gear.Rr = gear.Rrs

            # update UI
            if gear.ID == 1:
                setText(self.ui.lb_Rrs1, self.G1.Rrs, self.units.lenMult, self.units.lenFormat)
            elif gear.ID == 2:
                setText(self.ui.lb_Rrs2, self.G2.Rrs, self.units.lenMult, self.units.lenFormat)
            elif gear.ID == 3:
                setText(self.ui.lb_Rrs3, self.G3.Rrs, self.units.lenMult, self.units.lenFormat)

    def updateRomax(self):
        for gear in self.gearList:
            # max OD is when theta_A is 0, i.e. the involute hits the tooth centerline
            # theta_A = (gear.tts / (2*gear.Rs)) + invF(gear.PA) - invF(phi_A)
            # 0 = (gear.tts / (2*gear.Rs)) + invF(gear.PA) - invF(phi_A)
            # invF(phi_A) = (gear.tts / (2*gear.Rs)) + invF(gear.PA)
            phi_A = revInvF((gear.tts / (2*gear.Rs)) + invF(self.PA))
            gear.Romax = gear.Rb / cos(phi_A)

            # bounds check
            if gear.Ro > gear.Romax:
                gear.Ro = gear.Romax

            if gear.Ro < gear.Rs:
                gear.Ro = gear.Ros

            if gear.ID == 1:
                setText(self.ui.lb_Romax1, self.G1.Romax, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.le_Ro1, self.G1.Ro, self.units.lenMult, self.units.lenFormat)
            elif gear.ID == 2:
                setText(self.ui.lb_Romax2, self.G2.Romax, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.le_Ro2, self.G2.Ro, self.units.lenMult, self.units.lenFormat)
            elif gear.ID == 3:
                setText(self.ui.lb_Romax3, self.G3.Romax, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.le_Ro3, self.G3.Ro, self.units.lenMult, self.units.lenFormat)

    def updateMaxTipRadius(self):
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

        for gear in self.gearList:
            Ro = gear.Ro
            Rb = gear.Rb
            Rs = gear.Rs
            tts = gear.tts
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
            gear.Rtip_max = float(RTip1(phi_A_solved))
            if gear.Rtip > gear.Rtip_max:
                gear.Rtip = gear.Rtip_max

            # update UI
            if gear.ID == 1:
                setText(self.ui.le_Rtip1, self.G1.Rtip, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_Rtipmax1, self.G1.Rtip_max, self.units.lenMult, self.units.lenFormat)
            elif gear.ID == 2:
                setText(self.ui.le_Rtip2, self.G2.Rtip, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_Rtipmax2, self.G2.Rtip_max, self.units.lenMult, self.units.lenFormat)
            elif gear.ID == 3:
                setText(self.ui.le_Rtip3, self.G3.Rtip, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_Rtipmax3, self.G3.Rtip_max, self.units.lenMult, self.units.lenFormat)

    def updateRoe(self):
        for gear in self.gearList:
            gear.Roe = sqrt( gear.Rb**2 + ( sqrt((gear.Ro-gear.Rtip)**2 - gear.Rb**2) + gear.Rtip )**2 )

            if gear.ID == 1:
                setText(self.ui.lb_Roe1, self.G1.Roe, self.units.lenMult, self.units.lenFormat)
            elif gear.ID == 2:
                setText(self.ui.lb_Roe2, self.G2.Roe, self.units.lenMult, self.units.lenFormat)
            elif gear.ID == 3:
                setText(self.ui.lb_Roe3, self.G3.Roe, self.units.lenMult, self.units.lenFormat)

    def updateCenterDistance(self):
        # use backlash
        if self.ui.cb_CD_bkl.currentIndex() == 0:
            bkl = getValue(self.ui.le_CD_bkl1, self.units.lenMult)
            if bkl is not None:
                self.bkl1 = bkl
            else:
                # print("no bkl1")
                return 1

            if self.type == Type.planetary:
                bkl = getValue(self.ui.le_bkl2, self.units.lenMult)
                if bkl is not None:
                    self.bkl2 = bkl
                else:
                    # print("no bkl2")
                    return 1

        # use center distance
        elif self.ui.cb_CD_bkl.currentIndex() == 1:
            CD = getValue(self.ui.le_CD_bkl1, self.units.lenMult)
            if CD is not None:
                self.CD = CD
            else:
                # print("no CD1")
                return 1

        match self.type:
            case Type.external:
                self.updatePitchRadius(self.G1, self.G2)

                setText(self.ui.lb_Rp1, self.G1.Rp, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_Rp2, self.G2.Rp, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_tt1, self.G1.tt, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_tt2, self.G2.tt, self.units.lenMult, self.units.lenFormat)

                # use backlash, update center distance
                if self.ui.cb_CD_bkl.currentIndex() == 0:
                    self.CD = self.G1.Rp + self.G2.Rp
                    setText(self.ui.lb_CD_value, self.CD, self.units.lenMult, self.units.lenFormat)
                # use center distance, update backlash
                elif self.ui.cb_CD_bkl.currentIndex() == 1:
                    self.bkl1 = (tau*self.G1.Rp)/self.G1.N - self.G1.tt - self.G2.tt
                    setText(self.ui.lb_bkl_value, self.bkl1, self.units.lenMult, self.units.lenFormat)

                self.OPA1 = arccos((self.G1.Rb+self.G2.Rb) / self.CD)
                self.OPA1_deg = rad2deg(self.OPA1)

            case Type.internal:
                self.updatePitchRadius(self.G1, self.G2)

                setText(self.ui.lb_Rp1, self.G1.Rp, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_Rp2, self.G2.Rp, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_tt1, self.G1.tt, self.units.lenMult, self.units.lenFormat)
                pitch = tau*self.G2.Rp / self.G2.N
                setText(self.ui.lb_tt2, pitch - self.G2.tt, self.units.lenMult, self.units.lenFormat)

                # use backlash, update center distance
                if self.ui.cb_CD_bkl.currentIndex() == 0:
                    self.CD = self.G2.Rp - self.G1.Rp
                    setText(self.ui.lb_CD_value, self.CD, self.units.lenMult, self.units.lenFormat)
                # use center distance, update backlash
                elif self.ui.cb_CD_bkl.currentIndex() == 1:
                    self.bkl1 = (tau*self.G1.Rp)/self.G1.N - self.G1.tt - self.G2.tt
                    setText(self.ui.lb_bkl_value, self.bkl1, self.units.lenMult, self.units.lenFormat)

                self.OPA1 = arccos((self.G2.Rb-self.G1.Rb) / self.CD)
                self.OPA1_deg = rad2deg(self.OPA1)

            case Type.planetary:
                self.updatePitchRadius(self.G1, self.G3)

                setText(self.ui.lb_Rp1, self.G1.Rp, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_Rp3, self.G3.Rp, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_tt1, self.G1.tt, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_tt3, self.G3.tt, self.units.lenMult, self.units.lenFormat)

                # use backlash, update center distance
                if self.ui.cb_CD_bkl.currentIndex() == 0:
                    self.CD = self.G1.Rp + self.G3.Rp
                    setText(self.ui.lb_CD_value, self.CD, self.units.lenMult, self.units.lenFormat)
                # use center distance, update backlash
                elif self.ui.cb_CD_bkl.currentIndex() == 1:
                    self.bkl1 = (tau*self.G1.Rp)/self.G1.N - self.G1.tt - self.G3.tt
                    setText(self.ui.lb_bkl_value, self.bkl1, self.units.lenMult, self.units.lenFormat)

                self.OPA1 = arccos((self.G1.Rb+self.G3.Rb) / self.CD)
                self.OPA1_deg = rad2deg(self.OPA1)

                # manually update G2
                self.G2.Rp = self.G1.Rp + 2*self.G3.Rp
                setText(self.ui.lb_Rp2, self.G2.Rp, self.units.lenMult, self.units.lenFormat)
                # internal gear tooth thickness is external tooth thickness plus backlash
                self.G2.tt = self.G3.tt + self.bkl2
                pitch = tau*self.G2.Rp / self.G2.N
                setText(self.ui.lb_tt2, pitch - self.G2.tt, self.units.lenMult, self.units.lenFormat)
                # reverse calc x
                self.OPA2 = arccos((self.G2.Rb-self.G3.Rb) / self.CD)
                self.OPA2_deg = rad2deg(self.OPA2)
                # tt = Rp*( (tts/Rs) + 2*(invF(PA) - invF(acos(Rb/Rp)) ) )
                # tt/Rp - (2*(invF(PA) - invF(acos(Rb/Rp))) = (tts/Rs)
                # tts = Rs * ( tt/Rp - (2*(invF(PA) - invF(acos(Rb/Rp))) )
                self.G2.tts = self.G2.Rs * ( (self.G2.tt/self.G2.Rp) - (2 * (invF(self.PA) - invF(arccos(self.G2.Rb/self.G2.Rp))) ) )
                setText(self.ui.lb_tts2, self.G2.tts, self.units.lenMult, self.units.lenFormat)
                # gear.tts = self.mod * (pi/2 + 2*x*tan(self.PA))
                # gear.tts/self.mod = pi/2 + 2*x*tan(self.PA)
                # (gear.tts/self.mod) - pi/2 = 2*x*tan(self.PA)
                # x = ( (gear.tts/self.mod) - pi/2 ) / 2*tan(self.PA)
                self.G2.x = ( (self.G2.tts/self.mod) - pi/2 ) / (2*tan(self.PA))
                setText(self.ui.le_x2, self.G2.x, 1)

    def updatePitchRadius(self, _G1, _G2):
        """Finds pitch radius and effective tooth thickness"""
        N1 = _G1.N
        N2 = _G2.N
        # Precalculate involute function at standard pitch / PA
        invS = invF(self.PA)
        # Standard pitch radius
        Rs1 = _G1.Rs
        Rs2 = _G2.Rs
        # Base circle radius
        Rb1 = _G1.Rb
        Rb2 = _G2.Rb
        # Standard tooth thickness with profile shift
        mod = self.mod
        tts1 = _G1.tts
        tts2 = _G2.tts
        bkl = self.bkl1
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
                if _G2.type == "external":
                    # circular pitch is sum of each tooth thickness and backlash
                    # (tau*Rp1)/N1 = tt1 + tt2 + bkl [equivalently, (tau*Rp2)/N2 = tt1 + tt2 + bkl]
                    # => (tau*Rp1)/N1 - tt1 - tt2 - bkl = 0
                    F[3] = (tau*x[0])/N1 - x[2] - x[3] - bkl
                elif _G2.type == "internal":
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

        # update pitch radius
        _G1.Rp = root[0].item()
        _G2.Rp = root[1].item()
        # update tooth thickness at new pitch radius
        _G1.tt = root[2].item()
        _G2.tt = root[3].item()

    def updateRootRadius(self):
        match self.type:
            case Type.external:
                self.G1.Rr = self.CD - self.G2.Ro - self.rtcl1
                self.G2.Rr = self.CD - self.G1.Ro - self.rtcl2
                setText(self.ui.lb_Rr1, self.G1.Rr, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.le_Rr2, self.G2.Rr, self.units.lenMult, self.units.lenFormat)
            case Type.internal:
                self.G1.Rr = self.G2.Rr - self.CD - self.rtcl1
                self.G2.Ro = self.CD + self.G1.Ro + self.rtcl2
                if self.G2.Ro > self.G2.Romax:
                    self.G2.Ro = self.G2.Romax
                self.updateRoe()
                setText(self.ui.lb_Rr1, self.G1.Rr, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.le_Ro2, self.G2.Ro, self.units.lenMult, self.units.lenFormat)
            case Type.planetary:
                self.G1.Rr = self.CD - self.G3.Ro - self.rtcl1
                self.G3.Rr = self.CD - self.G1.Ro - self.rtcl3
                self.G2.Rr = self.CD + self.G3.Rr + self.rtcl3
                self.G2.Ro = self.CD + self.G3.Ro + self.rtcl2
                setText(self.ui.lb_Rr1, self.G1.Rr, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_Rr3, self.G3.Rr, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.le_Rr2, self.G2.Rr, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.le_Ro2, self.G2.Ro, self.units.lenMult, self.units.lenFormat)
                self.updateRoe()

    def updateMaxRootFillet(self):
        for gear in self.gearList:
            ###########################################################################
            #   Calculate fillet radius. This function computes two separate distances:
            #   1.) the distance from the fillet center to the involute curve, and
            #   2.) the distance from the fillet center to the root circle
            #   The function then finds the condition where these two distances are the
            #   same.

            N = gear.N
            tts = gear.tts
            Rs = gear.Rs
            Rb = gear.Rb
            Rr = gear.Rr
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
                gear.Rff = -(Rr*sin(alpha))/(sin(alpha) - 1)
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

                newRff = Rf1(phi_JFI)
                if newRff < 0:
                    gear.Rff = 0
                else:
                    gear.Rff = newRff

            if gear.Rf > gear.Rff:
                gear.Rf = gear.Rff

            if gear.Rf < 0:
                gear.Rf = 0

            # update UI
            if gear.ID == 1:
                setText(self.ui.le_Rf1, self.G1.Rf, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_Rff1, self.G1.Rff, self.units.lenMult, self.units.lenFormat)
            elif gear.ID == 2:
                setText(self.ui.le_Rf2, self.G2.Rf, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_Rff2, self.G2.Rff, self.units.lenMult, self.units.lenFormat)
            elif gear.ID == 3:
                setText(self.ui.le_Rf3, self.G3.Rf, self.units.lenMult, self.units.lenFormat)
                setText(self.ui.lb_Rff3, self.G3.Rff, self.units.lenMult, self.units.lenFormat)

    def checkUndercut(self):
        for gear in self.gearList:
            # distance from the gear center to the center point of the root fillet,
            # assuming the JFI is on the base circle
            # this forms a right triangle with Rb and Rf
            CF = sqrt(gear.Rb**2 + gear.Rf**2)
            # CF sets the minimum Rr for a given Rf
            Rrmin = CF - gear.Rf

            # get correct ui element
            if gear.ID == 1:
                label = self.ui.lb_undercut1
            elif gear.ID == 2:
                label = self.ui.lb_undercut2
            elif gear.ID == 3:
                label = self.ui.lb_undercut3

            # Undercut check
            if gear.Rr < Rrmin:
                gear.undercut = True
                label.setText("Undercut")
            else:
                gear.undercut = False
                label.setText("")

    def updateJFI(self):
        for gear in self.gearList:
            if gear.undercut == True:
                gear.phi_JFI = 0

                theta_A = (gear.tts/(2*gear.Rs)) + invF(self.PA)
                # angle between JFI and center of fillet circle
                alpha_F = arcsin(gear.Rf / (gear.Rr + gear.Rf))
                gear.theta_F = theta_A + alpha_F
            else:
                # profile angle through center of fillet circle
                phi_F = arccos(gear.Rb / (gear.Rr + gear.Rf))
                # line tangent to base circle through fillet center point
                EF = sqrt((gear.Rr+gear.Rf)**2 - gear.Rb**2)
                # line tangent to base circle to involute
                EA = EF - gear.Rf
                # profile angle at JFI
                phi_A = arctan(EA / gear.Rb)
                theta_A = (gear.tts/(2*gear.Rs)) + invF(self.PA) - invF(phi_A)
                theta_F = phi_F - phi_A + theta_A

                gear.phi_JFI = phi_A
                gear.theta_F = theta_F

            gear.Rjfi = gear.Rb/cos(gear.phi_JFI)

    def updateContactRatio(self):
        match self.type:
            case Type.external:
                self.updateCRExternal(self.G1, self.G2)
            case Type.internal:
                self.updateCRInternal(self.G1, self.G2, 1)
            case Type.planetary:
                self.updateCRExternal(self.G1, self.G3)
                self.updateCRInternal(self.G3, self.G2, 2)

    def updateCRExternal(self, _G1, _G2):
        # AGMA-908 Parameters
        # max line action, Rb to Rb
        C6 = self.CD * sin(self.OPA1)
        # start of line of contact, when G2 is at Roe
        C1 = C6 - sqrt(_G2.Roe**2 - _G2.Rb**2)
        # end of line of contact, when G1 is at Roe
        C5 = sqrt(_G1.Roe**2 - _G1.Rb**2)
        # [UNUSED] point where line of contact intersects center line
        #C3 = (_G1.N/(_G1.N+_G2.N)) * C6

        # Line of contact
        LoC = C5 - C1;
        # Contact ratio
        CR = LoC / _G1.Pb;

        if is_number(CR):
            self.CR1 = CR
            setText(self.ui.lb_CR1, self.CR1, 1)

            # minimum number of teeth engaged at any time
            n = int(self.CR1)

            # lowest point of single tooth contact for G1
            C2 = C5 - n*_G1.Pb
            # highest point of single tooth contact for G1
            C4 = C1 + n*_G1.Pb

            # Highest point of single tooth contact
            _G1.Rhp = sqrt(_G1.Rb**2 + C4**2)
            _G2.Rhp = sqrt(_G2.Rb**2 + (C6-C2)**2)

    def updateCRInternal(self, _G1, _G2, _mesh):
        if _mesh == 1:
            OPA = self.OPA1
        elif _mesh == 2:
            OPA = self.OPA2
        # GOIG 12.30
        E1P = _G1.Rb * tan(OPA)
        E2P = _G2.Rb * tan(OPA)
        E1T1 = sqrt(_G1.Roe**2 - _G1.Rb**2)
        # use Rjfi instead of Rr to take root fillet into account
        # E2T2 = sqrt(_G2.Rr**2 - _G2.Rb**2)
        Rjfi = _G2.Rb/cos(_G2.phi_JFI)
        E2T2 = sqrt(Rjfi**2 - _G2.Rb**2)
        E1T2 = E1P - (E2P - E2T2)

        # Line of contact
        LoC = (E2P - E2T2) + (E1T1 - E1P)

        # Contact ratio
        CR = LoC / _G1.Pb;
        if is_number(CR):
            if _mesh == 1:
                self.CR1 = CR
                setText(self.ui.lb_CR1, self.CR1, 1)
            elif _mesh == 2:
                self.CR2 = CR
                setText(self.ui.lb_CR2, self.CR2, 1)

            # minimum number of teeth engaged at any time
            n = int(CR)
            # Highest point of single tooth contact
            _G1.Rhp = sqrt(_G1.Rb**2 + (E1T2 + n*_G1.Pb)**2)
            _G2.Rhp = sqrt(_G2.Rb**2 + (E2T2 + n*_G2.Pb)**2)

# Stress ######################################################################
    def updateStress(self):
        if self.get_N(): return 1
        if self.get_FW(): return 1
        if self.get_RPM(): return 1
        if self.get_torque(): return 1
        if self.get_E(): return 1
        if self.get_nu(): return 1

        stress.calcPitchLineVelocity(self)
        self.updateContactStress()
        self.updateBendingStress()

    def get_FW(self):
        FW1 = getValue(self.ui.le_FW1)
        if FW1:
            self.G1.FW = FW1 * self.units.lenMult
        else:
            # print("no FW1")
            return 1
        FW2 = getValue(self.ui.le_FW2)
        if FW2:
            self.G2.FW = FW2 * self.units.lenMult
        else:
            # print("no FW2")
            return 1

        if self.type == Type.planetary:
            FW3 = getValue(self.ui.le_FW3)
            if FW3:
                self.G3.FW = FW3 * self.units.lenMult
            else:
                # print("no FW3")
                return 1

    def get_RPM(self):
        RPM = getValue(self.ui.le_RPM)
        if RPM is not None:
            self.RPM = RPM
        else:
            # print("no RPM")
            return 1

    def get_torque(self):
        torque = getValue(self.ui.le_torque)
        if torque is not None:
            self.torque = torque * self.units.torqueMult
        else:
            # print("no torque")
            return 1

    def get_E(self):
        E1 = getValue(self.ui.le_E1)
        if E1:
            self.G1.E = E1 * self.units.pressureMult
        else:
            # print("no E1")
            return 1
        E2 = getValue(self.ui.le_E2)
        if E2:
            self.G2.E = E2 * self.units.pressureMult
        else:
            # print("no E2")
            return 1

        if self.type == Type.planetary:
            E3 = getValue(self.ui.le_E3)
            if E3:
                self.G3.E = E3 * self.units.pressureMult
            else:
                # print("no E3")
                return 1

    def get_nu(self):
        nu1 = getValue(self.ui.le_nu1)
        if nu1:
            self.G1.nu = nu1
        else:
            # print("no nu1")
            return 1
        nu2 = getValue(self.ui.le_nu2)
        if nu2:
            self.G2.nu = nu2
        else:
            # print("no nu2")
            return 1

        if self.type == Type.planetary:
            nu3 = getValue(self.ui.le_nu3)
            if nu3:
                self.G3.nu = nu3
            else:
                # print("no nu3")
                return 1

    def updateContactStress(self):
        if self.type == Type.external or self.type == Type.internal:
            # use smallest face width
            FW = min(self.G1.FW, self.G2.FW)
            # convert torque to force through HPSTC tangent to base circle
            w = self.torque / (self.G1.Rb * FW)

            stressC = stress.calcContactStress(self.G1, self.G2, self.OPA1, w)
            setText(self.ui.lb_stressC1, stressC, self.units.pressureMult)
            setText(self.ui.lb_stressC2, stressC, self.units.pressureMult)

        elif self.type == Type.planetary:
            # use smallest face width
            FW = min(self.G1.FW, self.G3.FW)
            # convert torque to force through HPSTC tangent to base circle
            w = self.torque / (self.G1.Rb * FW)
            stressC1 = stress.calcContactStress(self.G1, self.G3, self.OPA1, w)
            setText(self.ui.lb_stressC1, stressC1, self.units.pressureMult)
            setText(self.ui.lb_stressC3, stressC1, self.units.pressureMult)

            FW = min(self.G2.FW, self.G3.FW)
            w = (self.torque * (self.G3.N/self.G1.N)) / (self.G3.Rb * FW)
            stressC2 = stress.calcContactStress(self.G3, self.G2, self.OPA2, w)
            setText(self.ui.lb_stressC2, stressC2, self.units.pressureMult)
            if stressC2 > stressC1:
                setText(self.ui.lb_stressC3, stressC2, self.units.pressureMult)

    def updateBendingStress(self):
        match self.type:
            case Type.external:
                force = self.torque / self.G1.Rb
                lewisParams = stress.lewisParabolaExternal(self, self.G1)
                stressB = stress.calcBendingStress(self, self.G1, force, lewisParams, 1)
                setText(self.ui.lb_stressB1, stressB, self.units.pressureMult)
                draw.drawStress(self, self.G1, self.canvasStress1[0], lewisParams)

                lewisParams = stress.lewisParabolaExternal(self, self.G2)
                stressB = stress.calcBendingStress(self, self.G2, force, lewisParams, 1)
                setText(self.ui.lb_stressB2, stressB, self.units.pressureMult)
                draw.drawStress(self, self.G2, self.canvasStress1[1], lewisParams)

            case Type.internal:
                force = self.torque / self.G1.Rb
                lewisParams = stress.lewisParabolaExternal(self, self.G1)
                stressB = stress.calcBendingStress(self, self.G1, force, lewisParams, 1)
                setText(self.ui.lb_stressB1, stressB, self.units.pressureMult)
                draw.drawStress(self, self.G1, self.canvasStress1[0], lewisParams)

                lewisParams = stress.lewisParabolaInternal(self, self.G2)
                stressB = stress.calcBendingStress(self, self.G2, force, lewisParams, 1)
                setText(self.ui.lb_stressB2, stressB, self.units.pressureMult)
                draw.drawStress(self, self.G2, self.canvasStress1[1], lewisParams)

            case Type.planetary:
                force = (self.torque / self.G1.Rb) / self.NPlanets
                lewisParams = stress.lewisParabolaExternal(self, self.G1)
                stressB = stress.calcBendingStress(self, self.G1, force, lewisParams, 1)
                setText(self.ui.lb_stressB1, stressB, self.units.pressureMult)
                draw.drawStress(self, self.G1, self.canvasStress1[0], lewisParams)

                lewisParams = stress.lewisParabolaExternal(self, self.G3)
                stressB = stress.calcBendingStress(self, self.G3, force, lewisParams, 1)
                setText(self.ui.lb_stressB3, stressB, self.units.pressureMult)
                draw.drawStress(self, self.G3, self.canvasStress1[1], lewisParams)

                force = (self.torque * (self.G3.N/self.G1.N) / self.G3.Rb) / self.NPlanets
                lewisParams = stress.lewisParabolaExternal(self, self.G3)
                stressB = stress.calcBendingStress(self, self.G3, force, lewisParams, 2)
                setText(self.ui.lb_stressB3, stressB, self.units.pressureMult)
                draw.drawStress(self, self.G3, self.canvasStress2[0], lewisParams)

                lewisParams = stress.lewisParabolaInternal(self, self.G2)
                stressB = stress.calcBendingStress(self, self.G2, force, lewisParams, 2)
                setText(self.ui.lb_stressB2, stressB, self.units.pressureMult)
                draw.drawStress(self, self.G2, self.canvasStress2[1], lewisParams)

# Main #######################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = jpgearqt()
    widget.show()
    sys.exit(app.exec())
