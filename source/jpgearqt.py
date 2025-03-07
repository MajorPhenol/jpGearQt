# Options for nuitka compilation:
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --onefile
# nuitka-project: --include-data-dir={MAIN_DIRECTORY}/resources=resources
# nuitka-project: --output-dir={MAIN_DIRECTORY}/../dist/{OS}/{Arch}
# nuitka-project: --remove-output
# nuitka-project-if: {OS} in ("Windows"):
#   nuitka-project: --onefile-windows-splash-screen-image={MAIN_DIRECTORY}/splash.png
## nuitka-project: --deployment

import sys
import os

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtWidgets import QMenuBar, QMenu
from PySide6.QtWidgets import QFileDialog, QDialog, QDialogButtonBox, QMessageBox

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QShortcut, QKeySequence, QCloseEvent, QAction

from ui_form import Ui_jpgearqt
from ui_popup import Ui_Popup

###############################################################################
from Gear import Gear

import numpy as np
from numpy import pi, sin, cos, tan, arcsin, arccos, arctan
from numpy import rad2deg, deg2rad
from numpy import sqrt, zeros, linspace, polyval, real

from scipy.optimize import fsolve, least_squares

from matplotlib.figure import Figure
import matplotlib.pyplot as pyplot
import matplotlib.path as mpath
import matplotlib.patches as mpatch
import matplotlib.collections as mcollections
import matplotlib.transforms as mtransforms
import matplotlib.animation as manimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT

import copy
import json

import ezdxf
from ezdxf.math import UCS
from ezdxf import zoom

###############################################################################
# why isn't this in numpy???
tau = 2*pi

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

# Involute Function
def invF(angle):
    """Computes the involute function of a given profile angle.

    All angles in radians.
    """

    return tan(angle) - angle

# Reverse Involute Function
def revInvF(angle):
    """Computes the reverse involute function, returning the profile angle.

    From "The Geometry of Involute Gears" by J.R. Colbourne
    Eqs. 2.16 - 2.17

    All angles in radians.
    """

    q = angle**(2/3)

    poly = [-0.00048, 0.00319, -0.00894, -0.00321, 0.32451, 1.04004, 1]
    x = polyval(poly, q)

    return arccos(1/x)

###############################################################################
# Use this code to signal the splash screen removal.
# if "NUITKA_ONEFILE_PARENT" in os.environ:
#    splash_filename = os.path.join(
#       tempfile.gettempdir(),
#       "onefile_%d_splash_feedback.tmp" % int(os.environ["NUITKA_ONEFILE_PARENT"]),
#    )

#    if os.path.exists(splash_filename):
#       os.unlink(splash_filename)

###############################################################################
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, _width=5, _height=4, _dpi=100):
        self.fig = Figure(figsize=(_width, _height), dpi=_dpi)
        self.axes = self.fig.add_subplot()
        super().__init__(self.fig)

class popupWindow(QWidget):
    def __init__(self, _jpgearqt):
        super().__init__()
        self.jpgearqt = _jpgearqt
        self.ui = Ui_Popup()
        self.ui.setupUi(self)
        self.connectUI()
        self.canvas = MplCanvas()

    def connectUI(self):
        self.ui.cb_circlesAnim.checkStateChanged.connect(lambda: self.updateCircles())
        self.ui.cb_singleViewAnim.checkStateChanged.connect(lambda: self.updateAnimAxes())

    def updateCircles(self):
        if self.ui.cb_circlesAnim.isChecked():
            circleCol1 = self.jpgearqt.addCircles(self.jpgearqt.G1, self.canvas, collection=True)
            circleCol2 = self.jpgearqt.addCircles(self.jpgearqt.G2, self.canvas, collection=True)
            circleCol2.set_transform(mtransforms.Affine2D().translate(self.jpgearqt.CD, 0) + self.canvas.axes.transData)

            circleCol1.set_label('circleCol1')
            circleCol2.set_label('circleCol2')

            self.canvas.axes.add_collection(circleCol1)
            self.canvas.axes.add_collection(circleCol2)

        else:
            collectionList = self.canvas.axes.collections
            for collection in collectionList:
                if collection.get_label() == 'circleCol1' or collection.get_label() == 'circleCol2':
                    collection.remove()

    def updateAnimAxes(self):
        canvas = self.canvas

        # tight view
        if self.ui.cb_singleViewAnim.isChecked():
            topLimit = self.jpgearqt.G1.Rp*sin(tau/self.jpgearqt.G1.N)
            bottomLimit = -topLimit
            leftLimit = self.jpgearqt.G1.Rp - topLimit
            rightLimit = self.jpgearqt.G1.Rp + topLimit
        # full view
        else:
            sizeBuffer = 1.1
            leftLimit = -self.jpgearqt.G1.Ro * sizeBuffer
            rightLimit = self.jpgearqt.CD + self.jpgearqt.G2.Ro * sizeBuffer
            topLimit = max(self.jpgearqt.G1.Ro, self.jpgearqt.G2.Ro) * sizeBuffer
            bottomLimit = -topLimit

        canvas.axes.set_xlim(left=leftLimit, right=rightLimit)
        canvas.axes.set_ylim(bottom=bottomLimit, top=topLimit)

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

        # gear objects
        self.G1 = Gear(1)
        self.G2 = Gear(2)

        # mesh parameters
        self.mod = -1                   # module
        self.PA_deg = 20                # pressure angle, degrees
        self.PA = deg2rad(self.PA_deg)  # pressure angle, radians
        self.OPA_deg = -1               # operating pressure angle, degrees
        self.OPA = -1                   # operating pressure angle, radians
        self.bkl = 0                    # backlash
        self.rtcl1 = 0                  # root clearances
        self.rtcl2 = 0
        self.CD = 0                     # center distance
        self.CR = 0                     # contact ratio
        self.speed = 1                    # pinion speed
        self.torque = 1                 # pinion torque

        self.savePath = ''              # for saving JSON

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

        # Help Menu
        menuHelp = menuBar.addMenu('&Help')
        actHelp = menuHelp.addAction('Help Menu')
        # actHelp.triggered.connect(lambda: )

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
        self.SC_drawGear.activated.connect(lambda: self.drawGear(self.G1, _updateAxes=True))
        self.SC_drawGear.activated.connect(lambda: self.drawGear(self.G2, _updateAxes=True))
        self.SC_drawGear.activated.connect(lambda: self.drawMesh(_updateAxes=True))

    def connectUI(self):
        # First tab
        self.ui.pb_calcGearSizes.clicked.connect(lambda: self.findGearSizes())
        self.ui.le_pN.editingFinished.connect(lambda: self.updatePinionN())

        rb_list = self.ui.buttonGroup.buttons()
        for button in rb_list:
            button.toggled.connect(lambda: self.drawLayout())
        # use layout button
        self.ui.pb_useLayout.clicked.connect(lambda: self.useLayout())

        # Second tab
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

        self.ui.le_Rtip1.editingFinished.connect(lambda: self.set_Rtip(self.G1, self.ui.le_Rtip1.text()))
        self.ui.le_Rtip2.editingFinished.connect(lambda: self.set_Rtip(self.G2, self.ui.le_Rtip2.text()))

        self.ui.le_rtcl1.editingFinished.connect(lambda: self.set_rtcl(1, self.ui.le_rtcl1.text()))
        self.ui.le_rtcl2.editingFinished.connect(lambda: self.set_rtcl(2, self.ui.le_rtcl2.text()))

        self.ui.le_Rf1.editingFinished.connect(lambda: self.set_Rf(self.G1, self.ui.le_Rf1.text()))
        self.ui.le_Rf2.editingFinished.connect(lambda: self.set_Rf(self.G2, self.ui.le_Rf2.text()))

        self.ui.le_FW1.editingFinished.connect(lambda: self.set_FW(self.G1, self.ui.le_FW1.text()))
        self.ui.le_FW2.editingFinished.connect(lambda: self.set_FW(self.G2, self.ui.le_FW2.text()))

        # draw gear button
        self.ui.pb_drawGear.clicked.connect(lambda: self.drawGear(self.G1, _updateAxes=True))
        self.ui.pb_drawGear.clicked.connect(lambda: self.drawGear(self.G2, _updateAxes=True))
        self.ui.pb_drawGear.clicked.connect(lambda: self.drawMesh(_updateAxes=True))
        # single tooth view checkboxes
        self.ui.cb_singleViewG1.checkStateChanged.connect(lambda: self.drawGear(self.G1, _updateAxes=True))
        self.ui.cb_singleViewG2.checkStateChanged.connect(lambda: self.drawGear(self.G2, _updateAxes=True))
        self.ui.cb_singleViewMesh.checkStateChanged.connect(lambda: self.drawMesh(_updateAxes=True))
        # circles checkboxes
        self.ui.cb_circlesG1.checkStateChanged.connect(lambda: self.drawGear(self.G1, _updateAxes=False))
        self.ui.cb_circlesG2.checkStateChanged.connect(lambda: self.drawGear(self.G2, _updateAxes=False))
        self.ui.cb_circlesMesh.checkStateChanged.connect(lambda: self.drawMesh(_updateAxes=False))
        # LoC checkbox
        self.ui.cb_LoC.checkStateChanged.connect(lambda: self.drawMesh(_updateAxes=False))
        # mesh slider
        self.ui.hSlider_Mesh.valueChanged.connect(lambda: self.drawMesh(_updateAxes=False))
        # animate button
        self.ui.pb_animate.clicked.connect(lambda: self.createAnimWindow())

        # Stress tab
        self.ui.le_speed.editingFinished.connect(lambda: self.set_speed(self.ui.le_speed.text()))
        self.ui.le_torque.editingFinished.connect(lambda: self.set_torque(self.ui.le_torque.text()))
        self.ui.le_E1.editingFinished.connect(lambda: self.set_E(self.G1, self.ui.le_E1.text()))
        self.ui.le_E2.editingFinished.connect(lambda: self.set_E(self.G2, self.ui.le_E2.text()))
        self.ui.le_nu1.editingFinished.connect(lambda: self.set_nu(self.G1, self.ui.le_nu1.text()))
        self.ui.le_nu2.editingFinished.connect(lambda: self.set_nu(self.G2, self.ui.le_nu2.text()))

        # stress button
        self.ui.pb_stress.clicked.connect(lambda: self.updateStress())


    def swapBklandCD(self):
        # input backlash
        if self.ui.cb_CD_bkl.currentIndex() == 0:
            self.ui.lb_bkl_text.hide()
            self.ui.lb_bkl_units.hide()
            self.ui.lb_bkl_value.hide()
            self.ui.le_CD_bkl.setText(str("{:.3f}".format(self.bkl)))

            self.ui.lb_CD_text.show()
            self.ui.lb_CD_units.show()
            self.ui.lb_CD_value.show()
            self.ui.lb_CD_value.setText(str("{:.3f}".format(self.CD)))

        # input center distance
        elif self.ui.cb_CD_bkl.currentIndex() == 1:
            self.ui.lb_CD_text.hide()
            self.ui.lb_CD_units.hide()
            self.ui.lb_CD_value.hide()
            self.ui.le_CD_bkl.setText(str("{:.3f}".format(self.CD)))

            self.ui.lb_bkl_text.show()
            self.ui.lb_bkl_units.show()
            self.ui.lb_bkl_value.show()
            self.ui.lb_bkl_value.setText(str("{:.3f}".format(self.bkl)))

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

    def initGearDesignFields(self):
        # gear design tab
        if self.mod > 0:
            self.ui.le_mod.setText(str("{:.2f}".format((self.mod))))

        self.ui.le_PA_deg.setText(str("{:.1f}".format((self.PA_deg))))

        if self.ui.cb_CD_bkl.currentIndex() == 0:
            self.ui.le_CD_bkl.setText(str("{:.3f}".format(self.bkl)))
            self.ui.lb_CD_text.hide()
            self.ui.lb_CD_units.hide()
            self.ui.lb_CD_value.hide()
        else:
            self.ui.le_CD_bkl.setText(str("{:.3f}".format(self.CD)))
            self.ui.lb_bkl_text.hide()
            self.ui.lb_bkl_units.hide()
            self.ui.lb_bkl_value.hide()

        self.ui.le_rtcl1.setText(str("{:.3f}".format(self.rtcl1)))
        self.ui.le_rtcl2.setText(str("{:.3f}".format(self.rtcl2)))

        if self.G1.N > 0:
            self.ui.le_N1.setText(str(self.G1.N))
        if self.G2.N > 0:
            self.ui.le_N2.setText(str(self.G2.N))

        self.ui.le_x1.setText(str("{:.3f}".format(self.G1.x)))
        self.ui.le_x2.setText(str("{:.3f}".format(self.G2.x)))

        if self.G1.Ro > 0:
            self.ui.le_Ro1.setText(str("{:.3f}".format(self.G1.Ro)))
        if self.G2.Ro > 0:
            self.ui.le_Ro2.setText(str("{:.3f}".format(self.G2.Ro)))

        self.ui.le_Rtip1.setText(str("{:.3f}".format(self.G1.Rtip)))
        self.ui.le_Rtip2.setText(str("{:.3f}".format(self.G2.Rtip)))
        self.ui.le_Rf1.setText(str("{:.3f}".format(self.G1.Rf)))
        self.ui.le_Rf2.setText(str("{:.3f}".format(self.G2.Rf)))
        self.ui.le_FW1.setText(str("{:.3f}".format(self.G1.FW)))
        self.ui.le_FW2.setText(str("{:.3f}".format(self.G2.FW)))
        self.ui.le_E1.setText(str("{:.3f}".format(self.G1.E)))
        self.ui.le_E2.setText(str("{:.3f}".format(self.G2.E)))
        self.ui.le_nu1.setText(str("{:.3f}".format(self.G1.nu)))
        self.ui.le_nu2.setText(str("{:.3f}".format(self.G2.nu)))

        # mesh slider
        self.sliderScale = 100    # the slider can only handle ints, show scale up everthing
        self.ui.hSlider_Mesh.setMinimum(0)
        self.ui.hSlider_Mesh.setMaximum(2*self.sliderScale)
        self.ui.hSlider_Mesh.setSliderPosition(1*self.sliderScale)    # pitch point happens at slider = 1

        # stress tab
        self.ui.le_FW1.setText(str("{:.0f}".format(self.G1.FW)))
        self.ui.le_FW2.setText(str("{:.0f}".format(self.G2.FW)))
        self.ui.le_E1.setText(str("{:.0f}".format(self.G1.E)))
        self.ui.le_E2.setText(str("{:.0f}".format(self.G2.E)))
        self.ui.le_nu1.setText(str("{:.2f}".format(self.G1.nu)))
        self.ui.le_nu2.setText(str("{:.2f}".format(self.G2.nu)))
        self.ui.le_speed.setText(str("{:.0f}".format(self.speed)))
        self.ui.le_torque.setText(str("{:.0f}".format(self.torque)))

    def exportDXF(self):
        for gear in [self.G1, self.G2]:
            if gear.Rb < 0 :
                messageBox = QMessageBox.critical(self, "Error exporting", "Could not export geometry for gear "+str(gear.ID))
            else:
                self.layoutGear(gear, save=True)


    def openJSON(self):
        loadPath, selectedFilter = QFileDialog.getOpenFileName(self, 'Load Design')

        if loadPath == '':
            return
        else:
            with open(loadPath, 'r', encoding='utf-8') as f:
                dictFull = json.load(f)

            dictG1 = dictFull["Gear1"]
            dictG2 = dictFull["Gear2"]
            dictM = dictFull["Mesh"]

            # set mesh parameters
            self.set_mod(dictM["mod"])
            self.set_PA_deg(dictM["PA_deg"])

            if dictM["set_CD_bkl"] == 0:
                # use backlash
                self.ui.cb_CD_bkl.setCurrentIndex(0)
                self.set_bkl(dictM["bkl"])
            else:
                # use center distance
                self.ui.cb_CD_bkl.setCurrentIndex(1)
                self.set_CD(dictM["CD"])

            self.set_rtcl(1, dictM["rtcl1"])
            self.set_rtcl(2, dictM["rtcl2"])

            self.set_speed(dictM["speed"])
            self.set_torque(dictM["torque"])

            # set gear parameters
            for gear, dict in zip([self.G1, self.G2], [dictG1, dictG2]):
                self.set_N(gear, dict["N"])
                self.set_x(gear, dict["x"])
                self.set_Ro(gear, dict["Ro"])
                self.set_Rtip(gear, dict["Rtip"])
            # split it up so that both N's are set before Rf
            for gear, dict in zip([self.G1, self.G2], [dictG1, dictG2]):
                self.set_Rf(gear, dict["Rf"])
                self.set_FW(gear, dict["FW"])
                self.set_E(gear, dict["E"])
                self.set_nu(gear, dict["nu"])

            self.initGearDesignFields()

    def saveAsJSON(self):
        defaultName = 'gear_design.json'
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
            "Ro" : _gear.Ro,
            "Rtip" : _gear.Rtip,
            "Rf" : _gear.Rf,
            "FW" : _gear.FW,
            "E" : _gear.E,
            "nu" : _gear.nu,
        }
    def createJSONMesh(self):
        return {
            "mod" : self.mod,
            "PA_deg" : self.PA_deg,
            "set_CD_bkl" : self.ui.cb_CD_bkl.currentIndex(),
            "bkl" : self.bkl,
            "CD" : self.CD,
            "rtcl1" : self.rtcl1,
            "rtcl2" : self.rtcl2,
            "speed" : self.speed,
            "torque" : self.torque
        }
# Helper Tab ##################################################################
    def findGearSizes(self):
        type = self.ui.cb_CD_width.currentIndex()

        if type == 0:
            """
            (N1*mod)/2 + (N2*mod)/2 = CD  →  (mod/2)*N1 + (mod/2)*N2 = CD
            N2 / N1 = GR  →  GR*N1 - N2 = 0

            | mod/2 mod/2 | | N1 | = | CD |
            | GR    -1    | | N2 |   | 0  |
            """

            try:
                mod = float(self.ui.le_targetMod.text())
                GR = float(self.ui.le_targetGR.text())
                CD = float(self.ui.le_targetSize.text())
            except:
                return

            matA = np.array([ [mod/2, mod/2], [GR, -1] ])
            matB = np.array([ [CD], [0] ])
            matX = np.matmul(np.linalg.inv(matA), matB)

            N1 = round(float(matX[0, 0]))
            N2 = round(N1*GR)
            # N2 = round(float(matX[1, 0]))

            self.ui.le_pN.setText(str("{:.0f}".format(N1)))
            self.ui.lb_gN3.setText(str("{:.0f}".format(N2)))

            self.populateChart(N2)
        else:
            """
            mod*N1/2 + mod*N2/2 + mod*(N1+2)/2 + mod*(N2+2)/2 = width  →  mod*N1 + mod*N2 = width - 2*mod
            N2 / N1 = GR  →  GR*N1 - N2 = 0

            | mod mod | | N1 | = | width - 2*mod |
            | GR  -1  | | N2 |   | 0             |
            """

            try:
                mod = float(self.ui.le_targetMod.text())
                GR = float(self.ui.le_targetGR.text())
                width = float(self.ui.le_targetSize.text())
            except:
                return

            matA = np.array([ [mod, mod], [GR, -1] ])
            matB = np.array([ [width - 2*mod], [0] ])
            matX = np.matmul(np.linalg.inv(matA), matB)

            N1 = round(float(matX[0, 0]))
            N2 = round(N1*GR)
            # N2 = round(float(matX[1, 0]))

            self.ui.le_pN.setText(str("{:.0f}".format(N1)))
            self.ui.lb_gN3.setText(str("{:.0f}".format(N2)))

            self.populateChart(N2)

    def updatePinionN(self):
        try:
            GR = float(self.ui.le_targetGR.text())
            N1 = int(self.ui.le_pN.text())
        except:
            return

        N2 = round(N1 * GR)

        self.populateChart(N2)

    def populateChart(self, _N2):
        try:
            mod = float(self.ui.le_targetMod.text())
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
            label.setText(str("{:.0f}".format(N2)))
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
            label.setText(str("{:.2f}".format(GR)))

        CD_label_list = [
                        self.ui.lb_CD1,
                        self.ui.lb_CD2,
                        self.ui.lb_CD3,
                        self.ui.lb_CD4,
                        self.ui.lb_CD5
                        ]

        for N2, label in zip(N2_list, CD_label_list):
            CD = mod * (N1 + N2)/2
            label.setText(str("{:.2f}".format(CD)))

        width_label_list = [
                        self.ui.lb_width1,
                        self.ui.lb_width2,
                        self.ui.lb_width3,
                        self.ui.lb_width4,
                        self.ui.lb_width5
                        ]

        for N2, label in zip(N2_list, width_label_list):
            CD = mod * (N1 + N2)/2
            Ros1 = mod * (N1 + 2)/2
            Ros2 = mod * (N2 + 2)/2
            width = Ros1 + CD + Ros2
            label.setText(str("{:.2f}".format(width)))

        self.drawLayout()

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

    def drawLayout(self):
        try:
            mod = float(self.ui.le_targetMod.text())
            N1 = int(self.ui.le_pN.text())
        except:
            return

        radio_button_list = [
                           self.ui.rb_1,
                           self.ui.rb_2,
                           self.ui.rb_3,
                           self.ui.rb_4,
                           self.ui.rb_5
                           ]
        N2_label_list = [
                        self.ui.lb_gN1,
                        self.ui.lb_gN2,
                        self.ui.lb_gN3,
                        self.ui.lb_gN4,
                        self.ui.lb_gN5
                        ]
        N2 = -1
        for N, radioButton in zip(N2_label_list, radio_button_list):
            if radioButton.isChecked():
                N2 = int(N.text())
                break

        Rs1 = (N1 * mod) / 2
        Rs2 = (N2 * mod) / 2

        Ro1 = ((N1 + 2) * mod) / 2
        Ro2 = ((N2 + 2) * mod) / 2

        CD = Rs1 + Rs2

        circleList = []
        # pitch circle
        circleList.append(pyplot.Circle((0, 0), Rs1, color='y', ls='--', fill=False))
        circleList.append(pyplot.Circle((CD, 0), Rs2, color='y', ls='--', fill=False))
        # outer circle
        circleList.append(pyplot.Circle((0, 0), Ro1, color='g', ls='--', fill=False))
        circleList.append(pyplot.Circle((CD, 0), Ro2, color='g', ls='--', fill=False))

        circleCol = mcollections.PatchCollection(circleList, match_original=True)

        self.canvasHelper.axes.cla()

        sizeBuffer = 1.1
        leftLimit = Ro1 * sizeBuffer
        rightLimit = CD + (Ro2 * sizeBuffer)
        yLimit = Ro2 * sizeBuffer
        self.canvasHelper.axes.set_xlim(left=-leftLimit, right=rightLimit)
        self.canvasHelper.axes.set_ylim(bottom=-yLimit, top=yLimit)
        self.canvasHelper.axes.set_aspect('equal')
        self.canvasHelper.axes.add_collection(circleCol)

        self.canvasHelper.draw()

# Gear Design Tab #############################################################
    def set_mod(self, _mod):
        if is_number(_mod):
            self.mod = float(_mod)
            self.updateStandardToothThickness(self.G1)
            self.updateStandardToothThickness(self.G2)

    def set_PA_deg(self, _PA_deg):
        if is_number(_PA_deg):
            self.PA_deg = float(_PA_deg)
            self.PA = deg2rad(self.PA_deg)
            self.updateStandardToothThickness(self.G1)
            self.updateStandardToothThickness(self.G2)

    def set_bkl(self, _bkl):
        if is_number(_bkl):
            self.bkl = float(_bkl)
            self.updateCenterDistance()

    def set_CD(self, _CD):
        if is_number(_CD):
            self.CD = float(_CD)
            self.updateCenterDistance()

    def set_N(self, _gear, _N):
        if is_number(_N):
            _gear.N = int(_N)
            self.set_x(_gear, _gear.x)

            if self.G1.N > 1 and self.G2.N > 1:
                self.ui.lb_GR.setText(str("{:.3f}".format(self.G2.N / self.G1.N)))

    def set_x(self, _gear, _x):
        if is_number(_x):
            _gear.x = float(_x)
            self.updateStandardToothThickness(_gear)

    def set_Ro(self, _gear, _Ro):
        if _gear.Romax < 0:
            return

        if is_number(_Ro):
            if float(_Ro) > _gear.Romax:
                _gear.Ro = _gear.Romax
                if _gear.ID == 1:
                    self.ui.le_Ro1.setText(str("{:.3f}".format(self.G1.Ro)))
                else:
                    self.ui.le_Ro2.setText(str("{:.3f}".format(self.G2.Ro)))
            else:
                _gear.Ro = float(_Ro)
            # check that Rtip is still valid, shrink if necessary
            self.updateMaxTipRadius(_gear)
            self.set_Rtip(_gear, _gear.Rtip)
            self.updateCenterDistance()

    def set_Rtip(self, _gear, _Rtip):
        if is_number(_Rtip):
            if float(_Rtip) > _gear.Rtip_max:
                _gear.Rtip = _gear.Rtip_max
                if _gear.ID == 1:
                    self.ui.le_Rtip1.setText(str("{:.3f}".format(_gear.Rtip)))
                else:
                    self.ui.le_Rtip2.setText(str("{:.3f}".format(_gear.Rtip)))
            else:
                _gear.Rtip = float(_Rtip)

            self.updateRoe(_gear)


    def set_rtcl(self, n, _rtcl):
        if is_number(_rtcl):
            if n == 1:
                self.rtcl1 = float(_rtcl)
                self.updateRootRadius(self.G1)
            else:
                self.rtcl2 = float(_rtcl)
                self.updateRootRadius(self.G2)

    def set_Rf(self, _gear, _Rf):
        if is_number(_Rf):
            if float(_Rf) > _gear.Rff:
                _gear.Rf = _gear.Rff
                if _gear.ID == 1:
                    self.ui.le_Rf1.setText(str("{:.3f}".format(_gear.Rf)))
                else:
                    self.ui.le_Rf2.setText(str("{:.3f}".format(_gear.Rf)))
            else:
                _gear.Rf = float(_Rf)

            self.checkUndercut(_gear)

    def set_FW(self, _gear, _FW):
        if is_number(_FW):
            _gear.FW = float(_FW)


    def updateBklandCD(self):
        # backlash
        if self.ui.cb_CD_bkl.currentIndex() == 0:
            self.set_bkl(float(self.ui.le_CD_bkl.text()))
        # center distance
        elif self.ui.cb_CD_bkl.currentIndex() == 1:
            self.set_CD(float(self.ui.le_CD_bkl.text()))

    def updateStandardToothThickness(self, _gear):
        if self.mod > 0 and self.PA > 0:
            # GOIG 6.11
            _gear.tts = self.mod * (pi/2 + 2*_gear.x*tan(self.PA))
            if _gear.ID == 1:
                self.ui.lb_tts1.setText(str("{:.3f}".format(self.G1.tts)))
            else:
                self.ui.lb_tts2.setText(str("{:.3f}".format(self.G2.tts)))

            self.updateBaseAndPitch(_gear)

    def updateBaseAndPitch(self, _gear):
        if _gear.N > 0 and self.mod > 0:
            _gear.Rs = 0.5 * _gear.N * self.mod
            _gear.Rb = _gear.Rs * cos(self.PA)
            _gear.Pb = tau * _gear.Rb / _gear.N
            _gear.Ros = (self.mod * (_gear.N+2) / 2)

            self.updateRomax(_gear)
            if _gear.Ro < _gear.Rb:
                self.set_Ro(_gear, _gear.Ros)
            else:
                self.set_Ro(_gear, _gear.Ro)

            if _gear.ID == 1:
                # self.ui.lb_Rb1.setText(str("{:.3f}".format(self.G1.Rb)))
                self.ui.lb_Rs1.setText(str("{:.3f}".format(self.G1.Rs)))
                self.ui.le_Ro1.setText(str("{:.3f}".format(self.G1.Ro)))
                self.ui.lb_Ros1.setText(str("{:.3f}".format(self.G1.Ros)))
            else:
                # self.ui.lb_Rb2.setText(str("{:.3f}".format(self.G2.Rb)))
                self.ui.lb_Rs2.setText(str("{:.3f}".format(self.G2.Rs)))
                self.ui.le_Ro2.setText(str("{:.3f}".format(self.G2.Ro)))
                self.ui.lb_Ros2.setText(str("{:.3f}".format(self.G2.Ros)))

    def updateRomax(self, _gear):
        if _gear.Rs > 0:
            # max OD is when theta_A is 0, i.e. the involute hits the tooth centerline
            # theta_A = (gear.tts / (2*gear.Rs)) + invF(gear.PA) - invF(phi_A)
            # 0 = (gear.tts / (2*gear.Rs)) + invF(gear.PA) - invF(phi_A)
            # invF(phi_A) = (gear.tts / (2*gear.Rs)) + invF(gear.PA)
            phi_A = revInvF((_gear.tts / (2*_gear.Rs)) + invF(self.PA))
            _gear.Romax = _gear.Rb / cos(phi_A)

            if _gear.ID == 1:
                self.ui.le_Ro1.setText(str("{:.3f}".format(self.G1.Ro)))
                self.ui.lb_Romax1.setText(str("{:.3f}".format(self.G1.Romax)))
            else:
                self.ui.le_Ro2.setText(str("{:.3f}".format(self.G2.Ro)))
                self.ui.lb_Romax2.setText(str("{:.3f}".format(self.G2.Romax)))

    def updateRoe(self, _gear):
        if _gear.Rb < 0:
            return

        if _gear.Ro < 0 and _gear.Ros > 0:
            _gear.Ro = _gear.Ros
            if _gear.ID == 1:
                self.ui.le_Ro1.setText(str("{:.3f}".format(_gear.Ro)))
            else:
                self.ui.le_Ro2.setText(str("{:.3f}".format(_gear.Ro)))

        _gear.Roe = sqrt( _gear.Rb**2 + ( sqrt((_gear.Ro-_gear.Rtip)**2 - _gear.Rb**2) + _gear.Rtip )**2 )

        if _gear.ID == 1:
            self.ui.lb_Roe1.setText(str("{:.3f}".format(_gear.Roe)))
        else:
            self.ui.lb_Roe2.setText(str("{:.3f}".format(_gear.Roe)))

        self.updateContactRatio()


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
            self.ui.lb_Rtipmax1.setText(str("{:.3f}".format(self.G1.Rtip_max)))
        else:
            self.ui.lb_Rtipmax2.setText(str("{:.3f}".format(self.G2.Rtip_max)))

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
            self.ui.le_Rf1.setText(str("{:.3f}".format(_gear.Rf)))
            self.ui.lb_Rff1.setText(str("{:.3f}".format(_gear.Rff)))
        else:
            self.ui.le_Rf2.setText(str("{:.3f}".format(_gear.Rf)))
            self.ui.lb_Rff2.setText(str("{:.3f}".format(_gear.Rff)))

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

        self.ui.lb_Rp1.setText(str("{:.3f}".format(self.G1.Rp)))
        self.ui.lb_Rp2.setText(str("{:.3f}".format(self.G2.Rp)))
        self.ui.lb_tt1.setText(str("{:.3f}".format(self.G1.tt)))
        self.ui.lb_tt2.setText(str("{:.3f}".format(self.G2.tt)))

        if self.ui.cb_CD_bkl.currentIndex() == 0:
            # update center distance
            self.CD = self.G1.Rp + self.G2.Rp
            self.ui.lb_CD_value.setText(str("{:.3f}".format(self.CD)))
        elif self.ui.cb_CD_bkl.currentIndex() == 1:
            # update backlash
            self.bkl = (tau*self.G1.Rp)/self.G1.N - self.G1.tt - self.G2.tt
            self.ui.lb_bkl_value.setText(str("{:.3f}".format(self.bkl)))

        # Operating pressure angle at updated center distance
        self.OPA = arccos((self.G1.Rb+self.G2.Rb) / self.CD)
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

        def func(x):
            # variables for function: Rp1, Rp2, tt1, tt2
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
                # circular pitch is sum of each tooth thickness and backlash
                # (tau*Rp1)/N1 = tt1 + tt2 + bkl [equivalently, (tau*Rp2)/N2 = tt1 + tt2 + bkl]
                # => (tau*Rp1)/N1 - tt1 - tt2 - bkl = 0
                F[3] = (tau*x[0])/N1 - x[2] - x[3] - bkl
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

        # AGMA-908 Parameters
        # max line action, Rb to Rb
        self.C6 = self.CD * sin(self.OPA)
        # start of line of contact, when G2 is at Roe
        self.C1 = self.C6 - sqrt(self.G2.Roe**2 - self.G2.Rb**2)
        # end of line of contact, when G1 is at Roe
        self.C5 = sqrt(self.G1.Roe**2 - self.G1.Rb**2)
        # point where line of contact intersects center line
        self.C3 = (self.G1.N/(self.G1.N+self.G2.N)) * self.C6
        # lowest point of single tooth contact for G1
        self.C2 = self.C5 - self.G1.Pb
        # highest point of single tooth contact for G1
        self.C4 = self.C1 + self.G1.Pb

        # Line of contact
        self.LoC = self.C5 - self.C1;

        # Contact ratio
        self.CR = self.LoC / self.G1.Pb;
        self.ui.lb_CR.setText(str("{:.3f}".format(self.CR)))

        # Highest point of single tooth contact
        self.G1.Rhp = sqrt(self.G1.Rb**2 + self.C4**2);
        self.G2.Rhp = sqrt(self.G2.Rb**2 + (self.C6-self.C2)**2);


    def updateRootRadius(self, _gear):
        if _gear.ID == 1:
            self.G1.Rr = self.CD - self.G2.Ro - self.rtcl1
            # self.ui.lb_Rr1.setText(str("{:.3f}".format(_gear.Rr)))
        else:
            self.G2.Rr = self.CD - self.G1.Ro - self.rtcl2
            # self.ui.lb_Rr2.setText(str("{:.3f}".format(_gear.Rr)))

        self.updateMaxRootFillet(_gear)
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


# Drawing #####################################################################
    def layoutGear(self, _gear, save=False):
        G = _gear

        if G.N < 1:
            return

        curveList = []
        curveColor = 'b'
        curveWidth = 2

        # Involute
        # find staring point of involute
        Rjfi = G.Rb/(cos(G.phi_JFI))
        theta_JFI = G.tts/(2*G.Rs) + invF(self.PA) - invF(G.phi_JFI)
        Rjfi_x = Rjfi*sin(theta_JFI)
        Rjfi_y = Rjfi*cos(theta_JFI)
        # create vectors of points along the involute
        RA = linspace(Rjfi, G.Roe, 20)
        phi_A = arccos(G.Rb/RA)
        theta_A = (G.tts/(2*G.Rs)) + invF(self.PA) - invF(phi_A)
        RAx = RA*sin(theta_A)
        RAy = RA*cos(theta_A)
        # add right side
        invPath = mpath.Path( list(map(list, zip(*[RAx, RAy]))) )
        invPatch = mpatch.PathPatch(invPath, color=curveColor, linewidth=curveWidth, fill=False)
        curveList.append(invPatch)
        # add left side
        invPath = mpath.Path( list(map(list, zip(*[-RAx, RAy]))) )
        invPatch = mpatch.PathPatch(invPath, color=curveColor, linewidth=curveWidth, fill=False)
        curveList.append(invPatch)

        # Root fillet radius
        if G.Rf > 0:
            # find center of fillet circle
            Fx = (G.Rr + G.Rf)*sin(G.theta_F)
            Fy = (G.Rr + G.Rf)*cos(G.theta_F)
            # find arc angles
            filletStartAngle = 180 + rad2deg(G.phi_JFI - theta_JFI);
            filletEndAngle = 360 - 90 - rad2deg(G.theta_F);
            curveList.append(mpatch.Arc(
                                        (Fx,Fy),
                                        G.Rf*2, G.Rf*2,
                                        theta1=filletStartAngle, theta2=filletEndAngle,
                                        color=curveColor,
                                        linewidth=curveWidth
                                        )
                            )
            curveList.append(mpatch.Arc(
                                        (-Fx,Fy),
                                        G.Rf*2, G.Rf*2,
                                        theta1=180-filletEndAngle, theta2=180-filletStartAngle,
                                        color=curveColor,
                                        linewidth=curveWidth
                                        )
                            )

        # add straight line segment if undercut
        if G.undercut == True:
            theta_A = G.tts/(2*G.Rs) + invF(self.PA)
            Rjfi = (G.Rr + G.Rf) * cos(G.theta_F - theta_A)
            Rjfi_x = Rjfi*sin(theta_A)
            Rjfi_y = Rjfi*cos(theta_A)

            Rb_x = G.Rb*sin(theta_A)
            Rb_y = G.Rb*cos(theta_A)

            line = mpath.Path([[Rjfi_x, Rjfi_y], [Rb_x, Rb_y]])
            linePatch = mpatch.PathPatch(line, color=curveColor, linewidth=curveWidth, fill=False)
            curveList.append(linePatch)
            line = mpath.Path([[-Rjfi_x, Rjfi_y], [-Rb_x, Rb_y]])
            linePatch = mpatch.PathPatch(line, color=curveColor, linewidth=curveWidth, fill=False)
            curveList.append(linePatch)

        # Root Radius
        if G.Rf < G.Rff:
            RRStartAngle1 = rad2deg(G.theta_F) + 90
            RREndAngle1 = rad2deg(pi/G.N) + 90
            RRStartAngle2 = -rad2deg(pi/G.N) + 90
            RREndAngle2 = -rad2deg(G.theta_F) + 90
            curveList.append(mpatch.Arc(
                                        (0, 0),
                                        G.Rr*2, G.Rr*2,
                                        theta1=RRStartAngle1, theta2=RREndAngle1,
                                        color=curveColor,
                                        linewidth=curveWidth
                                        )
                            )
            curveList.append(mpatch.Arc(
                                        (0, 0),
                                        G.Rr*2, G.Rr*2,
                                        theta1=RRStartAngle2, theta2=RREndAngle2,
                                        color=curveColor,
                                        linewidth=curveWidth
                                        )
                            )

        # Tip Radius
        if G.Rtip > 0:
            # point where tip touches involute
            phi_Atip = arccos(G.Rb/G.Roe);
            theta_Atip = (G.tts/(2*G.Rs)) + invF(self.PA) - invF(phi_Atip);
            # point where tip touches OD
            CF = G.Ro - G.Rtip; # distance from gear center to fillet center
            phi_Otip = arccos(G.Rb/CF);
            theta_Otip = theta_Atip - phi_Atip + phi_Otip;
            # Center point
            Rtip_x = CF*sin(theta_Otip);
            Rtip_y = CF*cos(theta_Otip);
            # find arc angles
            tipStartAngle = rad2deg(phi_Atip - theta_Atip);
            tipEndAngle = 90 - rad2deg(theta_Otip);
            curveList.append(mpatch.Arc(
                                        (Rtip_x,Rtip_y),
                                        G.Rtip*2, G.Rtip*2,
                                        theta1=tipStartAngle, theta2=tipEndAngle,
                                        color=curveColor,
                                        linewidth=curveWidth
                                        )
                            )
            curveList.append(mpatch.Arc(
                                        (-Rtip_x,Rtip_y),
                                        G.Rtip*2, G.Rtip*2,
                                        theta1=180-tipEndAngle, theta2=180-tipStartAngle,
                                        color=curveColor,
                                        linewidth=curveWidth
                                        )
                            )

        # Outer Radius
        if G.Rtip < G.Rtip_max:
            if 'theta_Otip' in locals():
                    theta_O = theta_Otip
            else:
                    phi_O = arccos(G.Rb/G.Roe);
                    theta_O = (G.tts/(2*G.Rs)) + invF(self.PA) - invF(phi_O);
            ODStartAngle = -rad2deg(theta_O) + 90
            ODEndAngle = rad2deg(theta_O) + 90
            curveList.append(mpatch.Arc(
                                        (0,0),
                                        G.Ro*2, G.Ro*2,
                                        #angle=90,
                                        theta1=ODStartAngle, theta2=ODEndAngle,
                                        color=curveColor,
                                        linewidth=curveWidth
                                        )
                            )

        if save == True:
            if G.ID == 1:
                defaultName = 'gear1.dxf'
            else:
                defaultName = 'gear2.dxf'

            savePath, selectedFilter = QFileDialog.getSaveFileName(self, 'Save Gear'+str(G.ID), defaultName)

            if savePath == '':
                return

            doc = ezdxf.new()
            msp = doc.modelspace()

            for n in range(G.N):
                    angle = (n/G.N)*tau
                    ucs = UCS(origin=(0,0,0)).rotate_local_z(angle)

                    # involute
                    msp.add_lwpolyline(list(zip(RAx, RAy))).transform(ucs.matrix)
                    msp.add_lwpolyline(list(zip(-RAx, RAy))).transform(ucs.matrix)

                    # root fillet
                    if G.Rf > 0:
                            msp.add_arc((Fx, Fy), radius=G.Rf, start_angle=filletStartAngle, end_angle=filletEndAngle).transform(ucs.matrix)
                            msp.add_arc((-Fx, Fy), radius=G.Rf, start_angle=180-filletEndAngle, end_angle=180-filletStartAngle).transform(ucs.matrix)

                    # add straight line segment if undercut
                    if G.undercut == True:
                            msp.add_line((Rjfi_x, Rjfi_y), (Rb_x, Rb_y)).transform(ucs.matrix)
                            msp.add_line((-Rjfi_x, Rjfi_y), (-Rb_x, Rb_y)).transform(ucs.matrix)

                    # root radius
                    if G.Rf < G.Rff :
                            msp.add_arc((0, 0), radius=G.Rr, start_angle=RRStartAngle1, end_angle=RREndAngle1).transform(ucs.matrix)
                            msp.add_arc((0, 0), radius=G.Rr, start_angle=RRStartAngle2, end_angle=RREndAngle2).transform(ucs.matrix)

                    # tip radius
                    if G.Rtip > 0:
                            msp.add_arc((Rtip_x,Rtip_y), radius=G.Rtip, start_angle=tipStartAngle, end_angle=tipEndAngle).transform(ucs.matrix)
                            msp.add_arc((-Rtip_x,Rtip_y), radius=G.Rtip, start_angle=180-tipEndAngle, end_angle=180-tipStartAngle).transform(ucs.matrix)

                    # outer radius
                    if G.Rtip < G.Rtip_max:
                            msp.add_arc((0, 0), radius=G.Ro, start_angle=ODStartAngle, end_angle=ODEndAngle).transform(ucs.matrix)

            zoom.extents(msp)
            doc.saveas(str(savePath))

        # save == False
        else:
            # make copies of all the teeth
            fullList = []
            for n in range(G.N):
                angle = (n/G.N)*tau
                for curve in curveList:
                    newCurve = copy.copy(curve)
                    newCurve.set_transform(mtransforms.Affine2D().rotate(angle))
                    fullList.append(newCurve)

            curveCollection = mcollections.PatchCollection(fullList, match_original=True)
            return curveCollection

    def addCircles(self, _gear, _canvas, collection=False):
        if _gear.Rb < 0:
            return None

        circleList = []
        # base circle
        circleList.append(pyplot.Circle((0, 0), _gear.Rb, color='c', ls='--', fill=False, label='Base Circle'))
        # # pitch circle
        circleList.append(pyplot.Circle((0, 0), _gear.Rp, color='y', ls='--', fill=False, label='Pitch Circle'))
        # # outer circle
        circleList.append(pyplot.Circle((0, 0), _gear.Roe, color='g', ls='--', fill=False, label='Outer Circle'))
        # # root cirlce
        circleList.append(pyplot.Circle((0, 0), _gear.Rr, color='r', ls='--', fill=False, label='Root Circle'))

        if collection == False:
            for circle in circleList:
                _canvas.axes.add_patch(circle)
            legendCircle = _canvas.axes.legend(loc='upper right', framealpha=1.0)
            _canvas.axes.add_artist(legendCircle)
        else:
            return mcollections.PatchCollection(circleList, match_original=True)

    def drawGear(self, _gear, _updateAxes = False):
        if _gear.Rb < 0:
            return

        if _gear.ID == 1:
            canvas = self.canvasG1
            cb_singleTooth = self.ui.cb_singleViewG1
            cb_circles = self.ui.cb_circlesG1
        else:
            canvas = self.canvasG2
            cb_singleTooth = self.ui.cb_singleViewG2
            cb_circles = self.ui.cb_circlesG2

        if _updateAxes == False:
            leftLimit, rightLimit, bottomLimit, topLimit = canvas.axes.axis()
        else:
            if cb_singleTooth.isChecked():
                rightLimit = _gear.Rp*sin(tau/_gear.N)
                leftLimit = -rightLimit
                topLimit = _gear.Rp + rightLimit
                bottomLimit = _gear.Rp - rightLimit
            else:
                rightLimit = _gear.Ro * 1.1
                leftLimit = -rightLimit
                topLimit = rightLimit
                bottomLimit = leftLimit

        canvas.axes.cla()

        canvas.axes.set_aspect('equal')
        canvas.axes.set_box_aspect(1)
        canvas.fig.tight_layout()

        canvas.axes.set_xlim(left=leftLimit, right=rightLimit)
        canvas.axes.set_ylim(bottom=bottomLimit, top=topLimit)

        curveCol = self.layoutGear(_gear)
        canvas.axes.add_collection(curveCol)

        if cb_circles.isChecked():
            self.addCircles(_gear, canvas)

        canvas.draw()

    def drawStress(self, _gear, _canvas, _lewisParams):
        # setup canvas
        rightLimit = _gear.Rp*sin(tau/_gear.N)
        leftLimit = -rightLimit
        topLimit = _gear.Rp + rightLimit
        bottomLimit = _gear.Rp - rightLimit

        _canvas.axes.cla()

        _canvas.axes.set_aspect('equal')
        _canvas.axes.set_box_aspect(1)
        _canvas.fig.tight_layout()

        _canvas.axes.set_xlim(left=leftLimit, right=rightLimit)
        _canvas.axes.set_ylim(bottom=bottomLimit, top=topLimit)

        # add teeth
        curveCol = self.layoutGear(_gear)
        if _gear.ID == 2:
            curveCol.set_edgecolor('r')
        _canvas.axes.add_collection(curveCol)
        # add parabola
        Rd, gamma, x_Lewis, y_Lewis, a_Lewis = _lewisParams
        x_span = linspace(-x_Lewis*1.1, x_Lewis*1.1, 25)
        y_span = a_Lewis*x_span**2 + Rd

        paraPath = mpath.Path( list(map(list, zip(*[x_span, y_span]))) )
        paraPatch = mpatch.PathPatch(paraPath, color='g', linestyle='--', linewidth=1, fill=False, label='Lewis Parabola')
        _canvas.axes.add_patch(paraPatch)
        # add fillet circle
        # Fx = (_gear.Rr + _gear.Rf)*sin(_gear.theta_F)   # center of fillet circle
        # Fy = (_gear.Rr + _gear.Rf)*cos(_gear.theta_F)
        # _canvas.axes.add_patch(pyplot.Circle((Fx, Fy), _gear.Rf, color='c', ls='--', fill=False))
        # add intersection points
        _canvas.axes.plot([x_Lewis], [y_Lewis], color='tab:orange', marker='o', linewidth=2)
        _canvas.axes.plot([-x_Lewis], [y_Lewis], color='tab:orange', marker='o', linewidth=2)
        # Highest point of single tooth contact
        phi_hp = arccos(_gear.Rb/_gear.Rhp)
        theta_hp = (_gear.tts/(2*_gear.Rs)) + invF(self.PA) - invF(phi_hp)
        Rhp_x = _gear.Rhp*sin(theta_hp)
        Rhp_y = _gear.Rhp*cos(theta_hp)
        _canvas.axes.plot([Rhp_x, 0], [Rhp_y, Rd], color='k', linestyle='--', linewidth=1)
        # _canvas.axes.plot([Rhp_x], [Rhp_y], color='r', marker='*', markersize=10, linestyle='', linewidth=3)
        # force vector arrow
        arrowSlope = (Rhp_y - Rd)/Rhp_x                 # rise over run
        tail_y = Rhp_y + (Rhp_y - Rd)*2                   # pick an arbitrary tail height
        tail_x = (tail_y - Rhp_y)/arrowSlope + Rhp_x    # calc tail_x to match slope
        dx = Rhp_x - tail_x
        dy = Rhp_y - tail_y
        arrowLength = sqrt(dx**2 + dy**2)
        tailWidth = arrowLength / 50
        arrow = mpatch.FancyArrow(tail_x, tail_y, dx, dy, width=tailWidth, length_includes_head=True, color='k')
        _canvas.axes.add_patch(arrow)

        _canvas.axes.legend(loc='upper right', framealpha=1.0)
        _canvas.draw()

    def drawMesh(self, _updateAxes = False):
        if self.G1.Rb < 0 or self.G2.Rb < 0:
            return

        canvas = self.canvasMesh
        cb_singleTooth = self.ui.cb_singleViewMesh
        cb_circles = self.ui.cb_circlesMesh

        if _updateAxes == False:
            leftLimit, rightLimit, bottomLimit, topLimit = canvas.axes.axis()
        else:
            if cb_singleTooth.isChecked():
                topLimit = self.G1.Rp*sin(tau/self.G1.N)
                bottomLimit = -topLimit
                leftLimit = self.G1.Rp - topLimit
                rightLimit = self.G1.Rp + topLimit
            else:
                sizeBuffer = 1.1
                leftLimit = -self.G1.Ro * sizeBuffer
                rightLimit = self.CD + self.G2.Ro * sizeBuffer
                topLimit = max(self.G1.Ro, self.G2.Ro) * sizeBuffer
                bottomLimit = -topLimit

        canvas.axes.cla()

        canvas.axes.set_aspect('equal')
        canvas.axes.set_box_aspect(1)
        canvas.fig.tight_layout()

        canvas.axes.set_xlim(left=leftLimit, right=rightLimit)
        canvas.axes.set_ylim(bottom=bottomLimit, top=topLimit)

        # Points for line of contact
        # pitch point
        x0 = self.G1.Rp
        y0 = 0
        # tangent to gear 1
        x1 = self.G1.Rb*cos(self.OPA)
        y1 = self.G1.Rb*sin(self.OPA)
        # tangent to gear 2
        x2 = self.CD - self.G2.Rb*cos(self.OPA)
        y2 = -self.G2.Rb*sin(self.OPA)
        # on LoC at Roe2
        # law of sines - A/sin(a) = B/sin(b)
        b = arcsin( (self.G2.Rp/self.G2.Roe) * sin(self.OPA + deg2rad(90)) )
        c = pi - b - self.OPA - deg2rad(90)
        x3 = self.CD - (self.G2.Roe * cos(c))
        y3 = self.G2.Roe * sin(c)
        b = arcsin( (self.G1.Rp/self.G1.Roe) * sin(self.OPA + deg2rad(90)) )
        c = pi - b - self.OPA - deg2rad(90)
        x4 = (self.G1.Roe * cos(c))
        y4 = -(self.G1.Roe * sin(c))

        # config slider
        slider = self.ui.hSlider_Mesh
        sliderMin = 0
        # pitch point happens at slider=1
        # find overshoot for gear two
        a = arctan(-y2/x2)
        overshoot = a / self.OPA
        sliderMax = 1 + overshoot

        slider.setMinimum(int(sliderMin * self.sliderScale))
        slider.setMaximum(int(sliderMax * self.sliderScale))

        # make the teeth mesh nicely
        ratio = self.G1.N / self.G2.N
        # profile angle at pitch circle
        phi_P1 = arccos(self.G1.Rb/self.G1.Rp)
        phi_P2 = arccos(self.G2.Rb/self.G2.Rp)
        # tooth thickness at pitch circle
        theta_P1 = self.G1.tt/(2*self.G1.Rp)
        theta_P2 = self.G2.tt/(2*self.G2.Rp)

        startAngle1 = -pi/2 + theta_P1
        startAngle2 = pi/2 + theta_P2

        curveStartAngle1 = startAngle1 + self.OPA + invF(self.OPA)
        curveStartAngle2 = startAngle2 - ratio * (self.OPA + invF(self.OPA))

        phi_A = float(slider.value() / self.sliderScale) * self.OPA
        updateAngle = phi_A + invF(phi_A)

        angle1 = curveStartAngle1 - (updateAngle)
        angle2 = curveStartAngle2 + (updateAngle * ratio)

        # draw everything
        curveCol1 = self.layoutGear(self.G1)
        curveCol2 = self.layoutGear(self.G2)
        curveCol2.set_edgecolor('r')

        curveCol1.set_transform(mtransforms.Affine2D().rotate(angle1) + canvas.axes.transData)
        curveCol2.set_transform(mtransforms.Affine2D().rotate(angle2).translate(self.CD, 0) + canvas.axes.transData)

        canvas.axes.add_collection(curveCol1)
        canvas.axes.add_collection(curveCol2)

        if cb_circles.isChecked():
            self.addCircles(self.G1, canvas, collection=False)

            circleCol2 = self.addCircles(self.G2, canvas, collection=True)
            circleCol2.set_transform(mtransforms.Affine2D().translate(self.CD, 0) + canvas.axes.transData)
            canvas.axes.add_collection(circleCol2)

        if self.ui.cb_LoC.isChecked():
            # line of contact
            canvas.axes.plot([x1,x2],[y1,y2], color='k', marker='x', linestyle='--', linewidth=1)
            loc, = canvas.axes.plot([x3,x4],[y3,y4], color='k', marker='x', linewidth=2, label='Line of Contact')
            # contact point
            traceAngle = self.OPA - phi_A
            R = self.G1.Rb/cos(phi_A)
            traceX = R*cos(traceAngle)
            traceY = R*sin(traceAngle)
            tracePoint, = canvas.axes.plot([traceX], [traceY], color='tab:orange', marker='o', linestyle='', linewidth=2, label='Point of Contact')
            legendPoint = canvas.axes.legend(handles=[loc, tracePoint], loc='lower left', framealpha=1.0)
            canvas.axes.add_artist(legendPoint)

        canvas.draw()

    def createAnimWindow(self):
        if self.G1.Rb < 0 or self.G2.Rb < 0:
            return

        window = popupWindow(self)
        window.setWindowTitle("Mesh Animation")

        window.ui.vLayout_popup.insertWidget(0, window.canvas)
        toolbar = NavigationToolbar2QT(window.canvas, self)
        window.ui.hLayout_toolbarAnim.insertWidget(0, toolbar)

        sizeBuffer = 1.1
        leftLimit = -self.G1.Ro * sizeBuffer
        rightLimit = self.CD + self.G2.Ro * sizeBuffer
        topLimit = max(self.G1.Ro, self.G2.Ro) * sizeBuffer
        bottomLimit = -topLimit

        window.canvas.axes.set_aspect('equal')
        window.canvas.axes.set_box_aspect(1)
        window.canvas.fig.tight_layout()

        window.canvas.axes.set_xlim(left=leftLimit, right=rightLimit)
        window.canvas.axes.set_ylim(bottom=bottomLimit, top=topLimit)

        curveCol1 = self.layoutGear(self.G1)
        curveCol2 = self.layoutGear(self.G2)
        curveCol2.set_edgecolor('r')

        window.canvas.axes.add_collection(curveCol1)
        curveCol2.set_transform(mtransforms.Affine2D().translate(self.CD, 0) + window.canvas.axes.transData)
        window.canvas.axes.add_collection(curveCol2)

        # animation specs
        slider = window.ui.hSlider_Speed
        maxSpeed = slider.maximum()             # RPM
        msPerRev = (60*1000)/maxSpeed           # milliseconds per revolution
        interval = 30                           # ms per frame
        framesPerRev = int(msPerRev / interval)	# frames for one rev
        ratio = self.G1.N / self.G2.N

        def animFunc(frame, _maxSpeed, _slider):
            speed = float(_slider.value())
            updateAngle = (speed/_maxSpeed) * (tau*frame)/framesPerRev

            angle1 = (-pi/2) - updateAngle
            angle2 = pi/2 + pi/self.G2.N - 0.5*self.bkl/self.G2.Rs + ratio*updateAngle

            curveCol1.set_transform(mtransforms.Affine2D().rotate(angle1) + window.canvas.axes.transData)
            curveCol2.set_transform(mtransforms.Affine2D().rotate((angle2)).translate(self.CD, 0) + window.canvas.axes.transData)

        self.anim = manimation.FuncAnimation(window.canvas.fig, animFunc, fargs=[maxSpeed, slider], frames=framesPerRev, interval=interval)

        window.canvas.draw()

        window.show()

# Stress ######################################################################
    def set_speed(self, _speed):
        if is_number(_speed):
            self.speed = float(_speed)

    def set_torque(self, _torque):
        if is_number(_torque):
            self.torque = float(_torque)

    def set_E(self, _gear, _E):
        if is_number(_E):
            _gear.E = float(_E)

    def set_nu(self, _gear, _nu):
        if is_number(_nu):
            _gear.nu = float(_nu)

    def updateStress(self):
        if self.G1.N < 1 or self.G2.N < 1:
            return
        if self.G1.FW < 0 or self.G2.FW < 0:
            return

        # use smallest face width
        FW = min(self.G1.FW, self.G2.FW)

        # convert torque to force through HPSTC tangent to base circle
        w = self.torque / (self.G1.Rb * FW)

        self.calcContactStress(w)
        self.calcBendingStress(w)

    def calcContactStress(self, _w):
        # elastic coefficient
        E1 = float(self.ui.le_E1.text())
        E2 = float(self.ui.le_E2.text())
        nu1 = float(self.ui.le_nu1.text())
        nu2 = float(self.ui.le_nu2.text())

        Cp = 1/sqrt( (pi*(1-nu1**2)/E1) + (pi*(1-nu2**2)/E2) )

        # max contact stress occurs at lowest point of single tooth contact
        rho1 = sqrt(self.G1.Roe**2 - self.G1.Rb**2) - self.G1.Pb    # AGMA C2
        rho2 = self.G1.Rb*self.G2.Rb*tan(self.OPA) - rho1           # AGMA C6 - C2

        stress = Cp * sqrt(_w*( (rho1+rho2)/(rho1*rho2) ))

        self.ui.lb_stressC1.setText(str("{:.3f}".format(stress)))
        self.ui.lb_stressC2.setText(str("{:.3f}".format(stress)))

    def calcBendingStress(self, _w):
        # Stress concentration factor Kf
        # from GOIG 11.24 - 11.26
        # Note that GOIG uses degrees while AGMA 908 uses radians
        k1 = 0.3054 - 0.00489*self.OPA_deg - 0.000069*self.OPA_deg**2
        k2 = 0.3620 - 0.01268*self.OPA_deg + 0.000104*self.OPA_deg**2
        k3 = 0.2934 + 0.00609*self.OPA_deg + 0.000087*self.OPA_deg**2

        for _gear, _canvas in zip([self.G1, self.G2], [self.canvasStress1, self.canvasStress2]):

            # Lewis parabola key points
            lewisParams = self.lewisParabola(_gear)
            Rd, gamma, x_Lewis, y_Lewis, a_Lewis = lewisParams

            # Lewis parabola dimensions
            tt_LP = 2*x_Lewis       # tooth thickness at critical section
            h_LP = Rd - y_Lewis     # height of Lewis parabola

            # please don't divide by zero
            if _gear.Rf < 0.001:
                self.set_Rf(_gear, 0.001)

            Kf = k1 + ( (tt_LP/_gear.Rf)**k2 ) * ( (tt_LP/h_LP)**k3 )

            stress = (_w/self.mod) * cos(gamma) * (Kf*( ((1.5*self.mod*h_LP)/ x_Lewis**2) -
                                    (0.5*self.mod*tan(gamma))/x_Lewis ) )

            if _gear.ID == 1:
                self.ui.lb_stressB1.setText(str("{:.3f}".format(stress)))
            else:
                self.ui.lb_stressB2.setText(str("{:.3f}".format(stress)))

            # draw tooth
            self.drawStress(_gear, _canvas, lewisParams)

    def lewisParabola(self, _gear):
        """
        # Find the intersection point of the Lewis parabola and the root fillet circle
        #
        # Parameters:
        # Fx, Fy - centerpoint of root fillet circle
        # Rf - root fillet radius
        # Rd - intersection of tooth centerline and force vector; the top of the Lewis
        #   parabola
        #
        # Output variables:
        # x, y - point of intersection between the Lewis parabola and the root fillet
        # a - scale of parabola, => y = ax^2 + bx + c
        #-------------------------------------------------------------------------------

        # Equation of a circle: (y-v)^2 + (x-h)^2 = r^2
        # Substitute values for fillet circle: (y-Fy)^2 + (x-Fx)^2 = Rf^2
        # Rearrange: y = +/-sqrt(Rf^2 - (x-Fx)^2) + Fy
        # We are only interested in the bottom half of the circle:
        # [1] y = -sqrt(Rf^2 - (x-Fx)^2) + Fy
        # Implicit differentiation of [1]:
        # [2] dy/dx = -(x-Fx)/(y-Fy)
        #
        # Equation of a parabola: y = ax^2 + bx + c
        # Substitute values of Lewis parabola, and note that the parabola is
        # centered on the y-axis, i.e. b=0:
        # [3] y = ax^2 + Rd
        # Differentiate [3]:
        # [4] dy/dx = 2ax
        #
        # At the tangent intersection of the parabola and circle, the derivatives
        # are equal:
        # [5] -(x-Fx)/(y-Fy) = 2ax
        # Rearrange [5]:
        # [6] a = -(x-Fx)/(2x)(y-Fy)
        # Substitute [6] into [3]:
        # y = -(x)(x-Fx)/(2)(y-Fy) + Rd
        # y^2 - Fy*y - Rd*y = (-x^2 + Fx*x)/2 - Rd*Fy
        # Complete the square:
        # [y^2 -(Fy+Rd)*y + (Fy+Rd)^2/4] - (Fy+Rd)^2/4 = (-x^2 + Fx*x)/2 - Rd*Fy
        # [y - (Fy+Rd)/2]^2  = (-x^2 + Fx*x)/2 - Rd*Fy + (Fy+Rd)^2/4
        # y - (Fy+Rd)/2 = +/-sqrt[(-x^2 + Fx*x)/2 - Rd*Fy + (Fy+Rd)^2/4]
        # [7] y = +/-sqrt[(-x^2 + Fx*x)/2 - Rd*Fy + (Fy+Rd)^2/4] + (Fy+Rd)/2
        # We are only interested in the bottom half of the circle:
        # [8] y = -sqrt[(-x^2 + Fx*x)/2 - Rd*Fy + (Fy+Rd)^2/4] + (Fy+Rd)/2
        # Eq [8] must intersect Eq [1]:
        # -sqrt[(-x^2 + Fx*x)/2 - Rd*Fy + (Fy+Rd)^2/4] + (Fy+Rd)/2 = -sqrt(Rf^2 - (x-Fx)^2) + Fy
        # Rearrange to find the zero:
        # [9] -sqrt[(-x^2 + Fx*x)/2 - Rd*Fy + (Fy+Rd)^2/4] + (Fy+Rd)/2 +
        #   sqrt(Rf^2 - (x-Fx)^2) - Fy = 0
        """

        # Highest point of single tooth contact
        phi_hp = arccos(_gear.Rb/_gear.Rhp)
        theta_hp = (_gear.tts/(2*_gear.Rs)) + invF(self.PA) - invF(phi_hp)
        Rhp_x = _gear.Rhp*sin(theta_hp)
        Rhp_y = _gear.Rhp*cos(theta_hp)

        # angle between force normal direction and
        # perpendicular to tooth centerline
        gamma = phi_hp - theta_hp

        # top of Lewis parabola
        Rd = _gear.Rb / cos(gamma)
        # alternately, Rd = Rhp_y - Rhp_x*tan(gamma) (GOIG 11.22)

        # find center of fillet circle
        Fx = (_gear.Rr + _gear.Rf)*sin(_gear.theta_F)
        Fy = (_gear.Rr + _gear.Rf)*cos(_gear.theta_F)

        if _gear.Rf == 0:
            x = Fx
            y = Fy
            a = (y-Rd)/(x**2)
        else:
            # Eq [9] above
            def func(x):
                return real(-sqrt( (-(x**2) + Fx*x)/2 - Rd*Fy + ((Fy+Rd)**2)/4) + (Fy+Rd)/2 +
                        sqrt(_gear.Rf**2 - (x-Fx)**2) - Fy)

            # starting point is between the JFI and fillet center
            initialGuess = Fx - _gear.Rf/2

            sol = least_squares(func, x0=initialGuess)
            x = sol.x.item()
            y = -sqrt(_gear.Rf**2 - (x-Fx)**2) + Fy 	# Eq [1] above
            a = (y-Rd)/(x**2)                               # Eq [3] above

        return [Rd, gamma, x, y, a]

# Main ########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = jpgearqt()
    widget.show()
    sys.exit(app.exec())
