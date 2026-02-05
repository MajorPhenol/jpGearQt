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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QHBoxLayout,
    QLabel, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_PopupForm(object):
    def setupUi(self, PopupForm):
        if not PopupForm.objectName():
            PopupForm.setObjectName(u"PopupForm")
        PopupForm.resize(800, 600)
        self.vLayout_popup = QVBoxLayout(PopupForm)
        self.vLayout_popup.setObjectName(u"vLayout_popup")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(PopupForm)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.hSlider_Speed = QSlider(PopupForm)
        self.hSlider_Speed.setObjectName(u"hSlider_Speed")
        self.hSlider_Speed.setMinimum(-20)
        self.hSlider_Speed.setMaximum(20)
        self.hSlider_Speed.setValue(10)
        self.hSlider_Speed.setSliderPosition(10)
        self.hSlider_Speed.setOrientation(Qt.Orientation.Horizontal)
        self.hSlider_Speed.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.hSlider_Speed.setTickInterval(20)

        self.horizontalLayout.addWidget(self.hSlider_Speed)


        self.vLayout_popup.addLayout(self.horizontalLayout)

        self.hLayout_toolbarAnim = QHBoxLayout()
        self.hLayout_toolbarAnim.setObjectName(u"hLayout_toolbarAnim")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_toolbarAnim.addItem(self.horizontalSpacer_9)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.cb_singleViewAnim = QCheckBox(PopupForm)
        self.cb_singleViewAnim.setObjectName(u"cb_singleViewAnim")

        self.verticalLayout.addWidget(self.cb_singleViewAnim)

        self.rb_sp_anim = QRadioButton(PopupForm)
        self.bg_anim = QButtonGroup(PopupForm)
        self.bg_anim.setObjectName(u"bg_anim")
        self.bg_anim.addButton(self.rb_sp_anim)
        self.rb_sp_anim.setObjectName(u"rb_sp_anim")
        self.rb_sp_anim.setChecked(True)

        self.verticalLayout.addWidget(self.rb_sp_anim)

        self.rb_pr_anim = QRadioButton(PopupForm)
        self.bg_anim.addButton(self.rb_pr_anim)
        self.rb_pr_anim.setObjectName(u"rb_pr_anim")

        self.verticalLayout.addWidget(self.rb_pr_anim)


        self.hLayout_toolbarAnim.addLayout(self.verticalLayout)

        self.cb_circlesAnim = QCheckBox(PopupForm)
        self.cb_circlesAnim.setObjectName(u"cb_circlesAnim")
        self.cb_circlesAnim.setChecked(False)

        self.hLayout_toolbarAnim.addWidget(self.cb_circlesAnim)


        self.vLayout_popup.addLayout(self.hLayout_toolbarAnim)


        self.retranslateUi(PopupForm)

        QMetaObject.connectSlotsByName(PopupForm)
    # setupUi

    def retranslateUi(self, PopupForm):
        PopupForm.setWindowTitle(QCoreApplication.translate("PopupForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("PopupForm", u"Speed", None))
        self.cb_singleViewAnim.setText(QCoreApplication.translate("PopupForm", u"Mesh View", None))
        self.rb_sp_anim.setText(QCoreApplication.translate("PopupForm", u"Sun-Planet", None))
        self.rb_pr_anim.setText(QCoreApplication.translate("PopupForm", u"Planet-Ring", None))
        self.cb_circlesAnim.setText(QCoreApplication.translate("PopupForm", u"Show Circles", None))
    # retranslateUi

