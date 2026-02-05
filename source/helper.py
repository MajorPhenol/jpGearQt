from enum import IntEnum
from math import isnan
from numpy import pi, tan, arccos, polyval
# why isn't this in numpy???
tau = 2*pi

from PySide6.QtCore import Qt, QPoint, QTimer
from PySide6.QtWidgets import QFileDialog, QMessageBox, QLabel
from PySide6.QtGui import QPalette, QColor

import json

class Type(IntEnum):
    external = 0
    internal = 1
    planetary = 2

def is_number(n):
    if n is None:
        return False
    try:
        float(n)
    except:
        return False
    if isnan(float(n)):
        return False
    return True

def getLoadPath(_dir=''):
    loadPath, selectedFilter = QFileDialog.getOpenFileName(caption='Load Design', dir=_dir)
    return loadPath

def getValue(_widget, _units=1, _type=float):
    value = _widget.text()
    if is_number(value):
        return _type(float(value)) * _units
    else:
        return None

def setText(_label, _variable, _mult=1, _format="{:.3f}"):
    if is_number(_variable):
        _label.setText(str(_format.format(_variable/_mult)))
    else:
        _label.setText(_variable)

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

def errorBox(_error, _text=''):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Critical)
    msgBox.setWindowTitle("ERROR")
    msgBox.setText(_text)
    msgBox.setInformativeText(str(_error))
    msgBox.exec()

def showMessage(_widget, _text='', _palette=None, _delayms=3000):
    buffer = 6

    parent = _widget.parentWidget()
    if parent is None:
        lb = QLabel(_widget, f=Qt.ToolTip)
        lb.setText(_text)
        lb.adjustSize()

        pos = _widget.mapToGlobal(QPoint(0,0))
        pos.setX(pos.x() + _widget.size().width() - lb.size().width() - buffer)
        pos.setY(pos.y() + _widget.size().height() - lb.size().height() - buffer)

    else:
        lb = QLabel(_widget.parentWidget(), f=Qt.ToolTip)
        lb.setText(_text)

        pos = _widget.mapToGlobal(QPoint(0,0))
        pos.setX(pos.x() + _widget.size().width() + buffer)

    if _palette is not None:
        lb.setPalette(_palette)

    lb.move(pos)
    lb.show()
    QTimer.singleShot(_delayms, lb.hide)
