# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Popup(object):
    def setupUi(self, Popup):
        if not Popup.objectName():
            Popup.setObjectName(u"Popup")
        Popup.resize(800, 600)
        self.vLayout_popup = QVBoxLayout(Popup)
        self.vLayout_popup.setObjectName(u"vLayout_popup")
        self.hSlider_Speed = QSlider(Popup)
        self.hSlider_Speed.setObjectName(u"hSlider_Speed")
        self.hSlider_Speed.setMinimum(-20)
        self.hSlider_Speed.setMaximum(20)
        self.hSlider_Speed.setValue(10)
        self.hSlider_Speed.setSliderPosition(10)
        self.hSlider_Speed.setOrientation(Qt.Orientation.Horizontal)
        self.hSlider_Speed.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.hSlider_Speed.setTickInterval(100)

        self.vLayout_popup.addWidget(self.hSlider_Speed)

        self.hLayout_toolbarAnim = QHBoxLayout()
        self.hLayout_toolbarAnim.setObjectName(u"hLayout_toolbarAnim")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_toolbarAnim.addItem(self.horizontalSpacer_9)

        self.cb_singleViewAnim = QCheckBox(Popup)
        self.cb_singleViewAnim.setObjectName(u"cb_singleViewAnim")

        self.hLayout_toolbarAnim.addWidget(self.cb_singleViewAnim)

        self.cb_circlesAnim = QCheckBox(Popup)
        self.cb_circlesAnim.setObjectName(u"cb_circlesAnim")
        self.cb_circlesAnim.setChecked(True)

        self.hLayout_toolbarAnim.addWidget(self.cb_circlesAnim)


        self.vLayout_popup.addLayout(self.hLayout_toolbarAnim)


        self.retranslateUi(Popup)

        QMetaObject.connectSlotsByName(Popup)
    # setupUi

    def retranslateUi(self, Popup):
        Popup.setWindowTitle(QCoreApplication.translate("Popup", u"Form", None))
        self.cb_singleViewAnim.setText(QCoreApplication.translate("Popup", u"Mesh View", None))
        self.cb_circlesAnim.setText(QCoreApplication.translate("Popup", u"Show Circles", None))
    # retranslateUi

