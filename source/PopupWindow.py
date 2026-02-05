from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from ui_popup import Ui_PopupForm

from os import path

from MplCanvas import MplCanvas
from helper import tau, Type
import draw

from numpy import pi, sin

import matplotlib.collections as mcollections
import matplotlib.transforms as mtransforms

class PopupWindow(QWidget):
    def __init__(self, _jpgear):
        super().__init__()
        self.setWindowIcon(QIcon(path.join(path.dirname(__file__), "resources/icon_main.png")))
        self.ui = Ui_PopupForm()
        self.ui.setupUi(self)

        self.jpgear = _jpgear
        self.canvas = MplCanvas()

        self.connectUI()
        self.toggleRadioButtons()

    def connectUI(self):
        self.ui.cb_circlesAnim.checkStateChanged.connect(lambda: self.updateCircles())
        self.ui.cb_singleViewAnim.checkStateChanged.connect(lambda: self.updateAnimAxes())
        self.ui.cb_singleViewAnim.checkStateChanged.connect(lambda: self.toggleRadioButtons())
        self.ui.rb_sp_anim.toggled.connect(lambda: self.updateAnimAxes())
        self.ui.rb_pr_anim.toggled.connect(lambda: self.updateAnimAxes())

        if self.jpgear.type == Type.planetary:
            self.ui.rb_sp_anim.show()
            self.ui.rb_pr_anim.show()
        else:
            self.ui.rb_sp_anim.hide()
            self.ui.rb_pr_anim.hide()

    def toggleRadioButtons(self):
        if self.ui.cb_singleViewAnim.isChecked():
            self.ui.rb_sp_anim.setEnabled(True)
            self.ui.rb_pr_anim.setEnabled(True)
        else:
            self.ui.rb_sp_anim.setEnabled(False)
            self.ui.rb_pr_anim.setEnabled(False)

    def updateCircles(self):
        if self.ui.cb_circlesAnim.isChecked():
            match self.jpgear.type:
                case Type.external:
                    circleCol1 = draw.addCircles(self.jpgear, self.jpgear.G1, self.canvas, _legend=False)
                    circleCol2 = draw.addCircles(self.jpgear, self.jpgear.G2, self.canvas, _legend=False)
                    circleCol2.set_transform(mtransforms.Affine2D().translate(self.jpgear.CD/self.jpgear.units.lenMult, 0) + self.canvas.axes.transData)
                    # add labels so we can delete them later
                    circleCol1.set_label('circleCol1')
                    circleCol2.set_label('circleCol2')

                    self.canvas.axes.add_collection(circleCol1)
                    self.canvas.axes.add_collection(circleCol2)

                case Type.internal:
                    circleCol1 = draw.addCircles(self.jpgear, self.jpgear.G1, self.canvas, _legend=False)
                    circleCol2 = draw.addCircles(self.jpgear, self.jpgear.G2, self.canvas, _legend=False)
                    circleCol2.set_transform(mtransforms.Affine2D().translate(-self.jpgear.CD/self.jpgear.units.lenMult, 0) + self.canvas.axes.transData)
                    # add labels so we can delete them later
                    circleCol1.set_label('circleCol1')
                    circleCol2.set_label('circleCol2')

                    self.canvas.axes.add_collection(circleCol1)
                    self.canvas.axes.add_collection(circleCol2)

                case Type.planetary:
                    circleCol1 = draw.addCircles(self.jpgear, self.jpgear.G1, self.canvas, _legend=False)
                    circleCol2 = draw.addCircles(self.jpgear, self.jpgear.G2, self.canvas, _legend=False)
                    # add labels so we can delete them later
                    circleCol1.set_label('circleCol1')
                    circleCol2.set_label('circleCol2')

                    self.canvas.axes.add_collection(circleCol1)
                    self.canvas.axes.add_collection(circleCol2)

                    NP = self.jpgear.NPlanets
                    for n in range(NP):
                        revAngle = (n/NP)*tau
                        circleCol3 = draw.addCircles(self.jpgear, self.jpgear.G3, self.canvas, _legend=False)
                        circleCol3.set_transform(mtransforms.Affine2D().translate(self.jpgear.CD/self.jpgear.units.lenMult, 0).rotate(revAngle) + self.canvas.axes.transData)
                        circleCol3.set_label('circleCol3')
                        self.canvas.axes.add_collection(circleCol3)

        else:
            collectionList = self.canvas.axes.collections
            for collection in collectionList:
                if collection.get_label() == 'circleCol1' or collection.get_label() == 'circleCol2' or collection.get_label() == 'circleCol2':
                    collection.remove()

    def updateAnimAxes(self):
        tightView = self.ui.cb_singleViewAnim.isChecked()

        mesh = None
        if self.jpgear.type == Type.planetary:
            mesh = 0 if self.ui.rb_sp_anim.isChecked() else 1

        leftLimit, rightLimit, bottomLimit, topLimit = draw.getMeshLimits(self.jpgear, tightView, mesh)

        self.canvas.axes.set_xlim(left=leftLimit, right=rightLimit)
        self.canvas.axes.set_ylim(bottom=bottomLimit, top=topLimit)

