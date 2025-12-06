from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, _width=5, _height=4, _dpi=100):
        self.fig = Figure(figsize=(_width, _height), dpi=_dpi)
        self.axes = self.fig.add_subplot()
        super().__init__(self.fig)
