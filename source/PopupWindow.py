from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from ui_popup import Ui_Popup

from os import path

from MplCanvas import MplCanvas
import draw

from numpy import pi, sin
# why isn't this in numpy???
tau = 2*pi

# import matplotlib.path as mpath
# import matplotlib.patches as mpatch
import matplotlib.collections as mcollections
import matplotlib.transforms as mtransforms

class PopupWindow(QWidget):
    def __init__(self, _jpgear):
        super().__init__()
        self.setWindowIcon(QIcon(path.join(path.dirname(__file__), "resources/icon_main.png")))
        self.ui = Ui_Popup()
        self.ui.setupUi(self)

        self.jpgear = _jpgear
        self.connectUI()
        self.canvas = MplCanvas()

    def connectUI(self):
        self.ui.cb_circlesAnim.checkStateChanged.connect(lambda: self.updateCircles())
        self.ui.cb_singleViewAnim.checkStateChanged.connect(lambda: self.updateAnimAxes())

    def updateCircles(self):
        if self.ui.cb_circlesAnim.isChecked():
            dir = 1 if self.jpgear.G2.type == "external" else -1
            circleCol1 = draw.addCircles(self.jpgear, self.jpgear.G1, self.canvas, _legend=False)
            circleCol2 = draw.addCircles(self.jpgear, self.jpgear.G2, self.canvas, _legend=False)
            circleCol2.set_transform(mtransforms.Affine2D().translate(dir*self.jpgear.CD/self.jpgear.units.lenMult, 0) + self.canvas.axes.transData)
            # add labels so we can delete them later
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
        G1 = self.jpgear.G1
        G2 = self.jpgear.G2
        lenMult = self.jpgear.units.lenMult
        canvas = self.canvas

        # tight view
        if self.ui.cb_singleViewAnim.isChecked():
            topLimit = (G1.Rp*sin(tau/G1.N)) / lenMult
            bottomLimit = -topLimit
            leftLimit = (G1.Rp / lenMult) - topLimit
            rightLimit = (G1.Rp / lenMult) + topLimit
        # full view
        else:
            if G2.type == "external":
                sizeBuffer = 0.1 * G2.Ro
                leftLimit = (-G1.Ro - sizeBuffer) / lenMult
                rightLimit = (self.jpgear.CD + G2.Ro + sizeBuffer) / lenMult
            elif G2.type == "internal":
                sizeBuffer = 0.1 * G2.Rrim
                leftLimit = (-self.jpgear.CD - G2.Rrim - sizeBuffer) / lenMult
                rightLimit = (G2.Rrim - self.jpgear.CD + sizeBuffer) / lenMult

            topLimit = (max(G1.Ro, G2.Ro) + sizeBuffer) / lenMult
            bottomLimit = -topLimit

        canvas.axes.set_xlim(left=leftLimit, right=rightLimit)
        canvas.axes.set_ylim(bottom=bottomLimit, top=topLimit)
