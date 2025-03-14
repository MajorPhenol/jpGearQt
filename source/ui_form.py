# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_jpgearqt(object):
    def setupUi(self, jpgearqt):
        if not jpgearqt.objectName():
            jpgearqt.setObjectName(u"jpgearqt")
        jpgearqt.setWindowModality(Qt.WindowModality.NonModal)
        jpgearqt.resize(1200, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(jpgearqt.sizePolicy().hasHeightForWidth())
        jpgearqt.setSizePolicy(sizePolicy)
        self.actiontest = QAction(jpgearqt)
        self.actiontest.setObjectName(u"actiontest")
        self.topLayout = QVBoxLayout(jpgearqt)
        self.topLayout.setObjectName(u"topLayout")
        self.tabW_main = QTabWidget(jpgearqt)
        self.tabW_main.setObjectName(u"tabW_main")
        self.tab_layout = QWidget()
        self.tab_layout.setObjectName(u"tab_layout")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_layout)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(6, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lb_TargetModule = QLabel(self.tab_layout)
        self.lb_TargetModule.setObjectName(u"lb_TargetModule")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_TargetModule.sizePolicy().hasHeightForWidth())
        self.lb_TargetModule.setSizePolicy(sizePolicy1)
        self.lb_TargetModule.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_TargetModule)

        self.le_targetMod = QLineEdit(self.tab_layout)
        self.le_targetMod.setObjectName(u"le_targetMod")
        sizePolicy1.setHeightForWidth(self.le_targetMod.sizePolicy().hasHeightForWidth())
        self.le_targetMod.setSizePolicy(sizePolicy1)
        self.le_targetMod.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_targetMod)

        self.lb_TargetGearRatio = QLabel(self.tab_layout)
        self.lb_TargetGearRatio.setObjectName(u"lb_TargetGearRatio")
        sizePolicy1.setHeightForWidth(self.lb_TargetGearRatio.sizePolicy().hasHeightForWidth())
        self.lb_TargetGearRatio.setSizePolicy(sizePolicy1)
        self.lb_TargetGearRatio.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_TargetGearRatio)

        self.le_targetGR = QLineEdit(self.tab_layout)
        self.le_targetGR.setObjectName(u"le_targetGR")
        sizePolicy1.setHeightForWidth(self.le_targetGR.sizePolicy().hasHeightForWidth())
        self.le_targetGR.setSizePolicy(sizePolicy1)
        self.le_targetGR.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_targetGR)

        self.cb_CD_width = QComboBox(self.tab_layout)
        self.cb_CD_width.addItem("")
        self.cb_CD_width.addItem("")
        self.cb_CD_width.setObjectName(u"cb_CD_width")
        sizePolicy1.setHeightForWidth(self.cb_CD_width.sizePolicy().hasHeightForWidth())
        self.cb_CD_width.setSizePolicy(sizePolicy1)
        self.cb_CD_width.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.cb_CD_width)

        self.le_targetSize = QLineEdit(self.tab_layout)
        self.le_targetSize.setObjectName(u"le_targetSize")
        sizePolicy1.setHeightForWidth(self.le_targetSize.sizePolicy().hasHeightForWidth())
        self.le_targetSize.setSizePolicy(sizePolicy1)
        self.le_targetSize.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_targetSize)

        self.pb_calcGearSizes = QPushButton(self.tab_layout)
        self.pb_calcGearSizes.setObjectName(u"pb_calcGearSizes")
        sizePolicy1.setHeightForWidth(self.pb_calcGearSizes.sizePolicy().hasHeightForWidth())
        self.pb_calcGearSizes.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pb_calcGearSizes)


        self.horizontalLayout_3.addLayout(self.formLayout)

        self.horizontalSpacer_2 = QSpacerItem(240, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(6, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_CenterDistance = QLabel(self.tab_layout)
        self.lb_CenterDistance.setObjectName(u"lb_CenterDistance")
        self.lb_CenterDistance.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_CenterDistance, 1, 6, 1, 1)

        self.rb_2 = QRadioButton(self.tab_layout)
        self.buttonGroup = QButtonGroup(jpgearqt)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.rb_2)
        self.rb_2.setObjectName(u"rb_2")
        self.rb_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_2.addWidget(self.rb_2, 4, 10, 1, 1)

        self.rb_3 = QRadioButton(self.tab_layout)
        self.buttonGroup.addButton(self.rb_3)
        self.rb_3.setObjectName(u"rb_3")
        self.rb_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.rb_3.setChecked(True)

        self.gridLayout_2.addWidget(self.rb_3, 5, 10, 1, 1)

        self.lb_gN4 = QLabel(self.tab_layout)
        self.lb_gN4.setObjectName(u"lb_gN4")
        self.lb_gN4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_gN4, 6, 4, 1, 1)

        self.lb_gN1 = QLabel(self.tab_layout)
        self.lb_gN1.setObjectName(u"lb_gN1")
        self.lb_gN1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_gN1, 3, 4, 1, 1)

        self.lb_icon1 = QLabel(self.tab_layout)
        self.lb_icon1.setObjectName(u"lb_icon1")
        self.lb_icon1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_icon1, 3, 8, 1, 1)

        self.lb_GR1 = QLabel(self.tab_layout)
        self.lb_GR1.setObjectName(u"lb_GR1")
        self.lb_GR1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_GR1, 3, 5, 1, 1)

        self.line_5 = QFrame(self.tab_layout)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 0, 0, 1, 11)

        self.lb_width5 = QLabel(self.tab_layout)
        self.lb_width5.setObjectName(u"lb_width5")
        self.lb_width5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_width5, 7, 7, 1, 1)

        self.lb_gN2 = QLabel(self.tab_layout)
        self.lb_gN2.setObjectName(u"lb_gN2")
        self.lb_gN2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_gN2, 4, 4, 1, 1)

        self.lb_GearRatio = QLabel(self.tab_layout)
        self.lb_GearRatio.setObjectName(u"lb_GearRatio")
        self.lb_GearRatio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_GearRatio, 1, 5, 1, 1)

        self.lb_width1 = QLabel(self.tab_layout)
        self.lb_width1.setObjectName(u"lb_width1")
        self.lb_width1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_width1, 3, 7, 1, 1)

        self.lb_CD5 = QLabel(self.tab_layout)
        self.lb_CD5.setObjectName(u"lb_CD5")
        self.lb_CD5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_CD5, 7, 6, 1, 1)

        self.pb_useLayout = QPushButton(self.tab_layout)
        self.pb_useLayout.setObjectName(u"pb_useLayout")

        self.gridLayout_2.addWidget(self.pb_useLayout, 8, 7, 1, 4)

        self.lb_icon3 = QLabel(self.tab_layout)
        self.lb_icon3.setObjectName(u"lb_icon3")
        self.lb_icon3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_icon3, 5, 8, 1, 1)

        self.line_8 = QFrame(self.tab_layout)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_8, 3, 2, 5, 1)

        self.lb_GR4 = QLabel(self.tab_layout)
        self.lb_GR4.setObjectName(u"lb_GR4")
        self.lb_GR4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_GR4, 6, 5, 1, 1)

        self.rb_1 = QRadioButton(self.tab_layout)
        self.buttonGroup.addButton(self.rb_1)
        self.rb_1.setObjectName(u"rb_1")
        self.rb_1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_2.addWidget(self.rb_1, 3, 10, 1, 1)

        self.lb_CD2 = QLabel(self.tab_layout)
        self.lb_CD2.setObjectName(u"lb_CD2")
        self.lb_CD2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_CD2, 4, 6, 1, 1)

        self.lb_icon5 = QLabel(self.tab_layout)
        self.lb_icon5.setObjectName(u"lb_icon5")
        self.lb_icon5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_icon5, 7, 8, 1, 1)

        self.lb_width3 = QLabel(self.tab_layout)
        self.lb_width3.setObjectName(u"lb_width3")
        self.lb_width3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_width3, 5, 7, 1, 1)

        self.lb_width4 = QLabel(self.tab_layout)
        self.lb_width4.setObjectName(u"lb_width4")
        self.lb_width4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_width4, 6, 7, 1, 1)

        self.lb_teeth = QLabel(self.tab_layout)
        self.lb_teeth.setObjectName(u"lb_teeth")
        self.lb_teeth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_teeth, 1, 4, 1, 1)

        self.lb_teeth_2 = QLabel(self.tab_layout)
        self.lb_teeth_2.setObjectName(u"lb_teeth_2")
        self.lb_teeth_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_teeth_2, 1, 1, 1, 1)

        self.rb_4 = QRadioButton(self.tab_layout)
        self.buttonGroup.addButton(self.rb_4)
        self.rb_4.setObjectName(u"rb_4")
        self.rb_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_2.addWidget(self.rb_4, 6, 10, 1, 1)

        self.lb_icon2 = QLabel(self.tab_layout)
        self.lb_icon2.setObjectName(u"lb_icon2")
        self.lb_icon2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_icon2, 4, 8, 1, 1)

        self.lb_gN5 = QLabel(self.tab_layout)
        self.lb_gN5.setObjectName(u"lb_gN5")
        self.lb_gN5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_gN5, 7, 4, 1, 1)

        self.lb_OverallWidth = QLabel(self.tab_layout)
        self.lb_OverallWidth.setObjectName(u"lb_OverallWidth")
        self.lb_OverallWidth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_OverallWidth, 1, 7, 1, 1)

        self.rb_5 = QRadioButton(self.tab_layout)
        self.buttonGroup.addButton(self.rb_5)
        self.rb_5.setObjectName(u"rb_5")
        self.rb_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_2.addWidget(self.rb_5, 7, 10, 1, 1)

        self.lb_icon4 = QLabel(self.tab_layout)
        self.lb_icon4.setObjectName(u"lb_icon4")
        self.lb_icon4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_icon4, 6, 8, 1, 1)

        self.lb_GR5 = QLabel(self.tab_layout)
        self.lb_GR5.setObjectName(u"lb_GR5")
        self.lb_GR5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_GR5, 7, 5, 1, 1)

        self.lb_CD1 = QLabel(self.tab_layout)
        self.lb_CD1.setObjectName(u"lb_CD1")
        self.lb_CD1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_CD1, 3, 6, 1, 1)

        self.lb_width2 = QLabel(self.tab_layout)
        self.lb_width2.setObjectName(u"lb_width2")
        self.lb_width2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_width2, 4, 7, 1, 1)

        self.lb_CD4 = QLabel(self.tab_layout)
        self.lb_CD4.setObjectName(u"lb_CD4")
        self.lb_CD4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_CD4, 6, 6, 1, 1)

        self.le_pN = QLineEdit(self.tab_layout)
        self.le_pN.setObjectName(u"le_pN")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_pN.sizePolicy().hasHeightForWidth())
        self.le_pN.setSizePolicy(sizePolicy2)
        self.le_pN.setMaximumSize(QSize(60, 22))
        self.le_pN.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.le_pN, 5, 1, 1, 1)

        self.lb_gear = QLabel(self.tab_layout)
        self.lb_gear.setObjectName(u"lb_gear")
        self.lb_gear.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_gear, 3, 3, 5, 1)

        self.lb_CD3 = QLabel(self.tab_layout)
        self.lb_CD3.setObjectName(u"lb_CD3")
        self.lb_CD3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_CD3, 5, 6, 1, 1)

        self.line_6 = QFrame(self.tab_layout)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_6, 2, 0, 1, 11)

        self.lb_pinion = QLabel(self.tab_layout)
        self.lb_pinion.setObjectName(u"lb_pinion")
        self.lb_pinion.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_pinion, 3, 0, 5, 1)

        self.lb_GR3 = QLabel(self.tab_layout)
        self.lb_GR3.setObjectName(u"lb_GR3")
        self.lb_GR3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_GR3, 5, 5, 1, 1)

        self.lb_gN3 = QLabel(self.tab_layout)
        self.lb_gN3.setObjectName(u"lb_gN3")
        self.lb_gN3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_gN3, 5, 4, 1, 1)

        self.lb_GR2 = QLabel(self.tab_layout)
        self.lb_GR2.setObjectName(u"lb_GR2")
        self.lb_GR2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_GR2, 4, 5, 1, 1)

        self.line_7 = QFrame(self.tab_layout)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 3, 9, 5, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.f_helper_layout = QFrame(self.tab_layout)
        self.f_helper_layout.setObjectName(u"f_helper_layout")
        sizePolicy.setHeightForWidth(self.f_helper_layout.sizePolicy().hasHeightForWidth())
        self.f_helper_layout.setSizePolicy(sizePolicy)
        self.f_helper_layout.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_helper_layout.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.f_helper_layout)

        self.tabW_main.addTab(self.tab_layout, "")
        self.tab_GD = QWidget()
        self.tab_GD.setObjectName(u"tab_GD")
        self.horizontalLayout = QHBoxLayout(self.tab_GD)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_10 = QSpacerItem(6, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 6, -1, 6)
        self.lb_CD_value = QLabel(self.tab_GD)
        self.lb_CD_value.setObjectName(u"lb_CD_value")
        self.lb_CD_value.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.lb_CD_value.sizePolicy().hasHeightForWidth())
        self.lb_CD_value.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setItalic(True)
        self.lb_CD_value.setFont(font)
        self.lb_CD_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_CD_value, 27, 2, 1, 1)

        self.lb_bkl_units = QLabel(self.tab_GD)
        self.lb_bkl_units.setObjectName(u"lb_bkl_units")
        sizePolicy2.setHeightForWidth(self.lb_bkl_units.sizePolicy().hasHeightForWidth())
        self.lb_bkl_units.setSizePolicy(sizePolicy2)
        self.lb_bkl_units.setFont(font)
        self.lb_bkl_units.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_bkl_units, 28, 1, 1, 1)

        self.label_45 = QLabel(self.tab_GD)
        self.label_45.setObjectName(u"label_45")
        sizePolicy2.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy2)
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_45, 19, 1, 1, 1)

        self.label_57 = QLabel(self.tab_GD)
        self.label_57.setObjectName(u"label_57")
        sizePolicy2.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy2)
        self.label_57.setFont(font)
        self.label_57.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_57, 15, 1, 1, 1)

        self.label_16 = QLabel(self.tab_GD)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_16, 19, 0, 1, 1)

        self.line_11 = QFrame(self.tab_GD)
        self.line_11.setObjectName(u"line_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_11.sizePolicy().hasHeightForWidth())
        self.line_11.setSizePolicy(sizePolicy3)
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_11, 25, 0, 1, 4)

        self.label_65 = QLabel(self.tab_GD)
        self.label_65.setObjectName(u"label_65")
        sizePolicy2.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy2)
        self.label_65.setFont(font)
        self.label_65.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_65, 21, 1, 1, 1)

        self.le_x1 = QLineEdit(self.tab_GD)
        self.le_x1.setObjectName(u"le_x1")
        sizePolicy3.setHeightForWidth(self.le_x1.sizePolicy().hasHeightForWidth())
        self.le_x1.setSizePolicy(sizePolicy3)
        self.le_x1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_x1, 6, 2, 1, 1)

        self.lb_tts1 = QLabel(self.tab_GD)
        self.lb_tts1.setObjectName(u"lb_tts1")
        sizePolicy2.setHeightForWidth(self.lb_tts1.sizePolicy().hasHeightForWidth())
        self.lb_tts1.setSizePolicy(sizePolicy2)
        self.lb_tts1.setFont(font)
        self.lb_tts1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_tts1, 9, 2, 1, 1)

        self.le_Rtip2 = QLineEdit(self.tab_GD)
        self.le_Rtip2.setObjectName(u"le_Rtip2")
        sizePolicy3.setHeightForWidth(self.le_Rtip2.sizePolicy().hasHeightForWidth())
        self.le_Rtip2.setSizePolicy(sizePolicy3)
        self.le_Rtip2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Rtip2, 15, 3, 1, 1)

        self.lb_undercut2 = QLabel(self.tab_GD)
        self.lb_undercut2.setObjectName(u"lb_undercut2")
        sizePolicy2.setHeightForWidth(self.lb_undercut2.sizePolicy().hasHeightForWidth())
        self.lb_undercut2.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(True)
        self.lb_undercut2.setFont(font1)
        self.lb_undercut2.setTextFormat(Qt.TextFormat.AutoText)
        self.lb_undercut2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_undercut2, 30, 3, 1, 1)

        self.label_43 = QLabel(self.tab_GD)
        self.label_43.setObjectName(u"label_43")
        sizePolicy2.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy2)
        self.label_43.setFont(font)
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_43, 7, 0, 1, 1)

        self.label_54 = QLabel(self.tab_GD)
        self.label_54.setObjectName(u"label_54")
        sizePolicy2.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy2)
        self.label_54.setFont(font)
        self.label_54.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_54, 29, 0, 1, 1)

        self.lb_CR = QLabel(self.tab_GD)
        self.lb_CR.setObjectName(u"lb_CR")
        sizePolicy2.setHeightForWidth(self.lb_CR.sizePolicy().hasHeightForWidth())
        self.lb_CR.setSizePolicy(sizePolicy2)
        self.lb_CR.setFont(font)
        self.lb_CR.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_CR, 29, 2, 1, 1)

        self.lb_bkl_text = QLabel(self.tab_GD)
        self.lb_bkl_text.setObjectName(u"lb_bkl_text")
        sizePolicy2.setHeightForWidth(self.lb_bkl_text.sizePolicy().hasHeightForWidth())
        self.lb_bkl_text.setSizePolicy(sizePolicy2)
        self.lb_bkl_text.setFont(font)
        self.lb_bkl_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_bkl_text, 28, 0, 1, 1)

        self.le_Rtip1 = QLineEdit(self.tab_GD)
        self.le_Rtip1.setObjectName(u"le_Rtip1")
        sizePolicy3.setHeightForWidth(self.le_Rtip1.sizePolicy().hasHeightForWidth())
        self.le_Rtip1.setSizePolicy(sizePolicy3)
        self.le_Rtip1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Rtip1, 15, 2, 1, 1)

        self.le_rtcl2 = QLineEdit(self.tab_GD)
        self.le_rtcl2.setObjectName(u"le_rtcl2")
        sizePolicy3.setHeightForWidth(self.le_rtcl2.sizePolicy().hasHeightForWidth())
        self.le_rtcl2.setSizePolicy(sizePolicy3)
        self.le_rtcl2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_rtcl2, 19, 3, 1, 1)

        self.le_rtcl1 = QLineEdit(self.tab_GD)
        self.le_rtcl1.setObjectName(u"le_rtcl1")
        sizePolicy3.setHeightForWidth(self.le_rtcl1.sizePolicy().hasHeightForWidth())
        self.le_rtcl1.setSizePolicy(sizePolicy3)
        self.le_rtcl1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_rtcl1, 19, 2, 1, 1)

        self.lb_Roe1 = QLabel(self.tab_GD)
        self.lb_Roe1.setObjectName(u"lb_Roe1")
        sizePolicy2.setHeightForWidth(self.lb_Roe1.sizePolicy().hasHeightForWidth())
        self.lb_Roe1.setSizePolicy(sizePolicy2)
        self.lb_Roe1.setFont(font)
        self.lb_Roe1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Roe1, 17, 2, 1, 1)

        self.label_27 = QLabel(self.tab_GD)
        self.label_27.setObjectName(u"label_27")
        sizePolicy2.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy2)
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_27, 12, 1, 1, 1)

        self.label_30 = QLabel(self.tab_GD)
        self.label_30.setObjectName(u"label_30")
        sizePolicy2.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy2)
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_30, 12, 0, 1, 1)

        self.le_Ro2 = QLineEdit(self.tab_GD)
        self.le_Ro2.setObjectName(u"le_Ro2")
        sizePolicy3.setHeightForWidth(self.le_Ro2.sizePolicy().hasHeightForWidth())
        self.le_Ro2.setSizePolicy(sizePolicy3)
        self.le_Ro2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Ro2, 12, 3, 1, 1)

        self.label_31 = QLabel(self.tab_GD)
        self.label_31.setObjectName(u"label_31")
        sizePolicy2.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy2)
        self.label_31.setFont(font)
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_31, 13, 1, 1, 1)

        self.lb_tt2 = QLabel(self.tab_GD)
        self.lb_tt2.setObjectName(u"lb_tt2")
        sizePolicy2.setHeightForWidth(self.lb_tt2.sizePolicy().hasHeightForWidth())
        self.lb_tt2.setSizePolicy(sizePolicy2)
        self.lb_tt2.setFont(font)
        self.lb_tt2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_tt2, 10, 3, 1, 1)

        self.lb_Rtipmax2 = QLabel(self.tab_GD)
        self.lb_Rtipmax2.setObjectName(u"lb_Rtipmax2")
        sizePolicy2.setHeightForWidth(self.lb_Rtipmax2.sizePolicy().hasHeightForWidth())
        self.lb_Rtipmax2.setSizePolicy(sizePolicy2)
        self.lb_Rtipmax2.setFont(font)
        self.lb_Rtipmax2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rtipmax2, 16, 3, 1, 1)

        self.le_x2 = QLineEdit(self.tab_GD)
        self.le_x2.setObjectName(u"le_x2")
        sizePolicy3.setHeightForWidth(self.le_x2.sizePolicy().hasHeightForWidth())
        self.le_x2.setSizePolicy(sizePolicy3)
        self.le_x2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_x2, 6, 3, 1, 1)

        self.label_52 = QLabel(self.tab_GD)
        self.label_52.setObjectName(u"label_52")
        sizePolicy2.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy2)
        self.label_52.setFont(font)
        self.label_52.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_52, 9, 0, 1, 1)

        self.lb_bkl_value = QLabel(self.tab_GD)
        self.lb_bkl_value.setObjectName(u"lb_bkl_value")
        self.lb_bkl_value.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.lb_bkl_value.sizePolicy().hasHeightForWidth())
        self.lb_bkl_value.setSizePolicy(sizePolicy2)
        self.lb_bkl_value.setFont(font)
        self.lb_bkl_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_bkl_value, 28, 2, 1, 1)

        self.label_20 = QLabel(self.tab_GD)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_20, 1, 0, 1, 1)

        self.lb_undercut1 = QLabel(self.tab_GD)
        self.lb_undercut1.setObjectName(u"lb_undercut1")
        sizePolicy2.setHeightForWidth(self.lb_undercut1.sizePolicy().hasHeightForWidth())
        self.lb_undercut1.setSizePolicy(sizePolicy2)
        self.lb_undercut1.setFont(font1)
        self.lb_undercut1.setTextFormat(Qt.TextFormat.AutoText)
        self.lb_undercut1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_undercut1, 30, 2, 1, 1)

        self.label_49 = QLabel(self.tab_GD)
        self.label_49.setObjectName(u"label_49")
        sizePolicy2.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy2)
        self.label_49.setFont(font)
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_49, 17, 0, 1, 1)

        self.label_50 = QLabel(self.tab_GD)
        self.label_50.setObjectName(u"label_50")
        sizePolicy2.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy2)
        self.label_50.setFont(font)
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_50, 8, 0, 1, 1)

        self.label_53 = QLabel(self.tab_GD)
        self.label_53.setObjectName(u"label_53")
        sizePolicy2.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy2)
        self.label_53.setFont(font)
        self.label_53.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_53, 16, 1, 1, 1)

        self.label_58 = QLabel(self.tab_GD)
        self.label_58.setObjectName(u"label_58")
        sizePolicy2.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy2)
        self.label_58.setFont(font)
        self.label_58.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_58, 26, 0, 1, 1)

        self.label_24 = QLabel(self.tab_GD)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_24, 23, 1, 1, 1)

        self.cb_CD_bkl = QComboBox(self.tab_GD)
        self.cb_CD_bkl.addItem("")
        self.cb_CD_bkl.addItem("")
        self.cb_CD_bkl.setObjectName(u"cb_CD_bkl")
        self.cb_CD_bkl.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout.addWidget(self.cb_CD_bkl, 3, 0, 1, 1)

        self.label_29 = QLabel(self.tab_GD)
        self.label_29.setObjectName(u"label_29")
        sizePolicy2.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy2)
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_29, 2, 1, 1, 1)

        self.label_15 = QLabel(self.tab_GD)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_15, 23, 0, 1, 1)

        self.label_46 = QLabel(self.tab_GD)
        self.label_46.setObjectName(u"label_46")
        sizePolicy2.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy2)
        self.label_46.setFont(font)
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_46, 21, 0, 1, 1)

        self.lb_Rp1 = QLabel(self.tab_GD)
        self.lb_Rp1.setObjectName(u"lb_Rp1")
        sizePolicy2.setHeightForWidth(self.lb_Rp1.sizePolicy().hasHeightForWidth())
        self.lb_Rp1.setSizePolicy(sizePolicy2)
        self.lb_Rp1.setFont(font)
        self.lb_Rp1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rp1, 8, 2, 1, 1)

        self.label_39 = QLabel(self.tab_GD)
        self.label_39.setObjectName(u"label_39")
        sizePolicy2.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy2)
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_39, 1, 1, 1, 1)

        self.label_51 = QLabel(self.tab_GD)
        self.label_51.setObjectName(u"label_51")
        sizePolicy2.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy2)
        self.label_51.setFont(font)
        self.label_51.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_51, 24, 1, 1, 1)

        self.lb_tt1 = QLabel(self.tab_GD)
        self.lb_tt1.setObjectName(u"lb_tt1")
        sizePolicy2.setHeightForWidth(self.lb_tt1.sizePolicy().hasHeightForWidth())
        self.lb_tt1.setSizePolicy(sizePolicy2)
        self.lb_tt1.setFont(font)
        self.lb_tt1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_tt1, 10, 2, 1, 1)

        self.le_N1 = QLineEdit(self.tab_GD)
        self.le_N1.setObjectName(u"le_N1")
        sizePolicy3.setHeightForWidth(self.le_N1.sizePolicy().hasHeightForWidth())
        self.le_N1.setSizePolicy(sizePolicy3)
        self.le_N1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_N1, 5, 2, 1, 1)

        self.lb_Romax2 = QLabel(self.tab_GD)
        self.lb_Romax2.setObjectName(u"lb_Romax2")
        sizePolicy2.setHeightForWidth(self.lb_Romax2.sizePolicy().hasHeightForWidth())
        self.lb_Romax2.setSizePolicy(sizePolicy2)
        self.lb_Romax2.setFont(font)
        self.lb_Romax2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Romax2, 14, 3, 1, 1)

        self.label_13 = QLabel(self.tab_GD)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_13, 14, 0, 1, 1)

        self.label_32 = QLabel(self.tab_GD)
        self.label_32.setObjectName(u"label_32")
        sizePolicy2.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy2)
        self.label_32.setFont(font)
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_32, 13, 0, 1, 1)

        self.label_44 = QLabel(self.tab_GD)
        self.label_44.setObjectName(u"label_44")
        sizePolicy2.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy2)
        self.label_44.setFont(font)
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_44, 7, 1, 1, 1)

        self.lb_Rff2 = QLabel(self.tab_GD)
        self.lb_Rff2.setObjectName(u"lb_Rff2")
        sizePolicy2.setHeightForWidth(self.lb_Rff2.sizePolicy().hasHeightForWidth())
        self.lb_Rff2.setSizePolicy(sizePolicy2)
        self.lb_Rff2.setFont(font)
        self.lb_Rff2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rff2, 24, 3, 1, 1)

        self.lb_Ros2 = QLabel(self.tab_GD)
        self.lb_Ros2.setObjectName(u"lb_Ros2")
        sizePolicy2.setHeightForWidth(self.lb_Ros2.sizePolicy().hasHeightForWidth())
        self.lb_Ros2.setSizePolicy(sizePolicy2)
        self.lb_Ros2.setFont(font)
        self.lb_Ros2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Ros2, 13, 3, 1, 1)

        self.label_42 = QLabel(self.tab_GD)
        self.label_42.setObjectName(u"label_42")
        sizePolicy2.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy2)
        self.label_42.setFont(font)
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_42, 9, 1, 1, 1)

        self.label_59 = QLabel(self.tab_GD)
        self.label_59.setObjectName(u"label_59")
        sizePolicy2.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy2)
        self.label_59.setFont(font)
        self.label_59.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_59, 29, 1, 1, 1)

        self.lb_Rs2 = QLabel(self.tab_GD)
        self.lb_Rs2.setObjectName(u"lb_Rs2")
        sizePolicy2.setHeightForWidth(self.lb_Rs2.sizePolicy().hasHeightForWidth())
        self.lb_Rs2.setSizePolicy(sizePolicy2)
        self.lb_Rs2.setFont(font)
        self.lb_Rs2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rs2, 7, 3, 1, 1)

        self.le_mod = QLineEdit(self.tab_GD)
        self.le_mod.setObjectName(u"le_mod")
        sizePolicy3.setHeightForWidth(self.le_mod.sizePolicy().hasHeightForWidth())
        self.le_mod.setSizePolicy(sizePolicy3)
        self.le_mod.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_mod, 1, 2, 1, 1)

        self.label_48 = QLabel(self.tab_GD)
        self.label_48.setObjectName(u"label_48")
        sizePolicy2.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy2)
        self.label_48.setFont(font)
        self.label_48.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_48, 10, 1, 1, 1)

        self.lb_Rtipmax1 = QLabel(self.tab_GD)
        self.lb_Rtipmax1.setObjectName(u"lb_Rtipmax1")
        sizePolicy2.setHeightForWidth(self.lb_Rtipmax1.sizePolicy().hasHeightForWidth())
        self.lb_Rtipmax1.setSizePolicy(sizePolicy2)
        self.lb_Rtipmax1.setFont(font)
        self.lb_Rtipmax1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rtipmax1, 16, 2, 1, 1)

        self.lb_GR = QLabel(self.tab_GD)
        self.lb_GR.setObjectName(u"lb_GR")
        sizePolicy2.setHeightForWidth(self.lb_GR.sizePolicy().hasHeightForWidth())
        self.lb_GR.setSizePolicy(sizePolicy2)
        self.lb_GR.setFont(font)
        self.lb_GR.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_GR, 26, 2, 1, 1)

        self.le_CD_bkl = QLineEdit(self.tab_GD)
        self.le_CD_bkl.setObjectName(u"le_CD_bkl")
        sizePolicy3.setHeightForWidth(self.le_CD_bkl.sizePolicy().hasHeightForWidth())
        self.le_CD_bkl.setSizePolicy(sizePolicy3)
        self.le_CD_bkl.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_CD_bkl, 3, 2, 1, 1)

        self.label_40 = QLabel(self.tab_GD)
        self.label_40.setObjectName(u"label_40")
        sizePolicy2.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy2)
        self.label_40.setFont(font)
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_40, 24, 0, 1, 1)

        self.label_12 = QLabel(self.tab_GD)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)

        self.lb_Romax1 = QLabel(self.tab_GD)
        self.lb_Romax1.setObjectName(u"lb_Romax1")
        sizePolicy2.setHeightForWidth(self.lb_Romax1.sizePolicy().hasHeightForWidth())
        self.lb_Romax1.setSizePolicy(sizePolicy2)
        self.lb_Romax1.setFont(font)
        self.lb_Romax1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Romax1, 14, 2, 1, 1)

        self.lb_CD_text = QLabel(self.tab_GD)
        self.lb_CD_text.setObjectName(u"lb_CD_text")
        sizePolicy2.setHeightForWidth(self.lb_CD_text.sizePolicy().hasHeightForWidth())
        self.lb_CD_text.setSizePolicy(sizePolicy2)
        self.lb_CD_text.setFont(font)
        self.lb_CD_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_CD_text, 27, 0, 1, 1)

        self.lb_Rr1 = QLabel(self.tab_GD)
        self.lb_Rr1.setObjectName(u"lb_Rr1")
        sizePolicy2.setHeightForWidth(self.lb_Rr1.sizePolicy().hasHeightForWidth())
        self.lb_Rr1.setSizePolicy(sizePolicy2)
        self.lb_Rr1.setFont(font)
        self.lb_Rr1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rr1, 21, 2, 1, 1)

        self.label_14 = QLabel(self.tab_GD)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_14, 16, 0, 1, 1)

        self.label_18 = QLabel(self.tab_GD)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_18, 2, 0, 1, 1)

        self.line_10 = QFrame(self.tab_GD)
        self.line_10.setObjectName(u"line_10")
        sizePolicy3.setHeightForWidth(self.line_10.sizePolicy().hasHeightForWidth())
        self.line_10.setSizePolicy(sizePolicy3)
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_10, 18, 0, 1, 4)

        self.label_6 = QLabel(self.tab_GD)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)

        self.lb_Roe2 = QLabel(self.tab_GD)
        self.lb_Roe2.setObjectName(u"lb_Roe2")
        sizePolicy2.setHeightForWidth(self.lb_Roe2.sizePolicy().hasHeightForWidth())
        self.lb_Roe2.setSizePolicy(sizePolicy2)
        self.lb_Roe2.setFont(font)
        self.lb_Roe2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Roe2, 17, 3, 1, 1)

        self.lb_Rs1 = QLabel(self.tab_GD)
        self.lb_Rs1.setObjectName(u"lb_Rs1")
        sizePolicy2.setHeightForWidth(self.lb_Rs1.sizePolicy().hasHeightForWidth())
        self.lb_Rs1.setSizePolicy(sizePolicy2)
        self.lb_Rs1.setFont(font)
        self.lb_Rs1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rs1, 7, 2, 1, 1)

        self.label_35 = QLabel(self.tab_GD)
        self.label_35.setObjectName(u"label_35")
        sizePolicy2.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy2)
        self.label_35.setFont(font)
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_35, 14, 1, 1, 1)

        self.lb_Rr2 = QLabel(self.tab_GD)
        self.lb_Rr2.setObjectName(u"lb_Rr2")
        sizePolicy2.setHeightForWidth(self.lb_Rr2.sizePolicy().hasHeightForWidth())
        self.lb_Rr2.setSizePolicy(sizePolicy2)
        self.lb_Rr2.setFont(font)
        self.lb_Rr2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rr2, 21, 3, 1, 1)

        self.le_PA_deg = QLineEdit(self.tab_GD)
        self.le_PA_deg.setObjectName(u"le_PA_deg")
        sizePolicy3.setHeightForWidth(self.le_PA_deg.sizePolicy().hasHeightForWidth())
        self.le_PA_deg.setSizePolicy(sizePolicy3)
        self.le_PA_deg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_PA_deg, 2, 2, 1, 1)

        self.lb_Rff1 = QLabel(self.tab_GD)
        self.lb_Rff1.setObjectName(u"lb_Rff1")
        sizePolicy2.setHeightForWidth(self.lb_Rff1.sizePolicy().hasHeightForWidth())
        self.lb_Rff1.setSizePolicy(sizePolicy2)
        self.lb_Rff1.setFont(font)
        self.lb_Rff1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rff1, 24, 2, 1, 1)

        self.label_34 = QLabel(self.tab_GD)
        self.label_34.setObjectName(u"label_34")
        sizePolicy2.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy2)
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_34, 15, 0, 1, 1)

        self.lb_Ros1 = QLabel(self.tab_GD)
        self.lb_Ros1.setObjectName(u"lb_Ros1")
        sizePolicy2.setHeightForWidth(self.lb_Ros1.sizePolicy().hasHeightForWidth())
        self.lb_Ros1.setSizePolicy(sizePolicy2)
        self.lb_Ros1.setFont(font)
        self.lb_Ros1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Ros1, 13, 2, 1, 1)

        self.le_N2 = QLineEdit(self.tab_GD)
        self.le_N2.setObjectName(u"le_N2")
        sizePolicy3.setHeightForWidth(self.le_N2.sizePolicy().hasHeightForWidth())
        self.le_N2.setSizePolicy(sizePolicy3)
        self.le_N2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_N2, 5, 3, 1, 1)

        self.lb_CD_units = QLabel(self.tab_GD)
        self.lb_CD_units.setObjectName(u"lb_CD_units")
        sizePolicy2.setHeightForWidth(self.lb_CD_units.sizePolicy().hasHeightForWidth())
        self.lb_CD_units.setSizePolicy(sizePolicy2)
        self.lb_CD_units.setFont(font)
        self.lb_CD_units.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_CD_units, 27, 1, 1, 1)

        self.line_9 = QFrame(self.tab_GD)
        self.line_9.setObjectName(u"line_9")
        sizePolicy3.setHeightForWidth(self.line_9.sizePolicy().hasHeightForWidth())
        self.line_9.setSizePolicy(sizePolicy3)
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_9, 11, 0, 1, 4)

        self.label_47 = QLabel(self.tab_GD)
        self.label_47.setObjectName(u"label_47")
        sizePolicy2.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy2)
        self.label_47.setFont(font)
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_47, 10, 0, 1, 1)

        self.le_Ro1 = QLineEdit(self.tab_GD)
        self.le_Ro1.setObjectName(u"le_Ro1")
        sizePolicy3.setHeightForWidth(self.le_Ro1.sizePolicy().hasHeightForWidth())
        self.le_Ro1.setSizePolicy(sizePolicy3)
        self.le_Ro1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Ro1, 12, 2, 1, 1)

        self.line_2 = QFrame(self.tab_GD)
        self.line_2.setObjectName(u"line_2")
        sizePolicy3.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy3)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 31, 0, 1, 4)

        self.label_41 = QLabel(self.tab_GD)
        self.label_41.setObjectName(u"label_41")
        sizePolicy2.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy2)
        self.label_41.setFont(font)
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_41, 8, 1, 1, 1)

        self.label_22 = QLabel(self.tab_GD)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_22, 5, 0, 1, 1)

        self.label_17 = QLabel(self.tab_GD)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_17, 4, 2, 1, 1)

        self.label_19 = QLabel(self.tab_GD)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_19, 4, 3, 1, 1)

        self.lb_Rp2 = QLabel(self.tab_GD)
        self.lb_Rp2.setObjectName(u"lb_Rp2")
        sizePolicy2.setHeightForWidth(self.lb_Rp2.sizePolicy().hasHeightForWidth())
        self.lb_Rp2.setSizePolicy(sizePolicy2)
        self.lb_Rp2.setFont(font)
        self.lb_Rp2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rp2, 8, 3, 1, 1)

        self.label_60 = QLabel(self.tab_GD)
        self.label_60.setObjectName(u"label_60")
        sizePolicy2.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy2)
        self.label_60.setFont(font)
        self.label_60.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_60, 26, 1, 1, 1)

        self.label_25 = QLabel(self.tab_GD)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_25, 3, 1, 1, 1)

        self.le_Rf1 = QLineEdit(self.tab_GD)
        self.le_Rf1.setObjectName(u"le_Rf1")
        sizePolicy3.setHeightForWidth(self.le_Rf1.sizePolicy().hasHeightForWidth())
        self.le_Rf1.setSizePolicy(sizePolicy3)
        self.le_Rf1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Rf1, 23, 2, 1, 1)

        self.label_55 = QLabel(self.tab_GD)
        self.label_55.setObjectName(u"label_55")
        sizePolicy2.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy2)
        self.label_55.setFont(font)
        self.label_55.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_55, 6, 1, 1, 1)

        self.lb_tts2 = QLabel(self.tab_GD)
        self.lb_tts2.setObjectName(u"lb_tts2")
        sizePolicy2.setHeightForWidth(self.lb_tts2.sizePolicy().hasHeightForWidth())
        self.lb_tts2.setSizePolicy(sizePolicy2)
        self.lb_tts2.setFont(font)
        self.lb_tts2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_tts2, 9, 3, 1, 1)

        self.label_21 = QLabel(self.tab_GD)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_21, 0, 2, 1, 1)

        self.le_Rf2 = QLineEdit(self.tab_GD)
        self.le_Rf2.setObjectName(u"le_Rf2")
        sizePolicy3.setHeightForWidth(self.le_Rf2.sizePolicy().hasHeightForWidth())
        self.le_Rf2.setSizePolicy(sizePolicy3)
        self.le_Rf2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Rf2, 23, 3, 1, 1)

        self.label_28 = QLabel(self.tab_GD)
        self.label_28.setObjectName(u"label_28")
        sizePolicy2.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy2)
        self.label_28.setFont(font)
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_28, 17, 1, 1, 1)

        self.label_66 = QLabel(self.tab_GD)
        self.label_66.setObjectName(u"label_66")
        sizePolicy2.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy2)
        self.label_66.setFont(font)
        self.label_66.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_66, 20, 0, 1, 1)

        self.label_67 = QLabel(self.tab_GD)
        self.label_67.setObjectName(u"label_67")
        sizePolicy2.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy2)
        self.label_67.setFont(font)
        self.label_67.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_67, 20, 1, 1, 1)

        self.lb_Rrs1 = QLabel(self.tab_GD)
        self.lb_Rrs1.setObjectName(u"lb_Rrs1")
        sizePolicy2.setHeightForWidth(self.lb_Rrs1.sizePolicy().hasHeightForWidth())
        self.lb_Rrs1.setSizePolicy(sizePolicy2)
        self.lb_Rrs1.setFont(font)
        self.lb_Rrs1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rrs1, 20, 2, 1, 1)

        self.lb_Rrs2 = QLabel(self.tab_GD)
        self.lb_Rrs2.setObjectName(u"lb_Rrs2")
        sizePolicy2.setHeightForWidth(self.lb_Rrs2.sizePolicy().hasHeightForWidth())
        self.lb_Rrs2.setSizePolicy(sizePolicy2)
        self.lb_Rrs2.setFont(font)
        self.lb_Rrs2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rrs2, 20, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.pb_drawGear = QPushButton(self.tab_GD)
        self.pb_drawGear.setObjectName(u"pb_drawGear")

        self.verticalLayout.addWidget(self.pb_drawGear)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.tabW_GD = QTabWidget(self.tab_GD)
        self.tabW_GD.setObjectName(u"tabW_GD")
        self.tabW_GD.setTabPosition(QTabWidget.TabPosition.South)
        self.tab_G1 = QWidget()
        self.tab_G1.setObjectName(u"tab_G1")
        self.vLayout_canvasG1 = QVBoxLayout(self.tab_G1)
        self.vLayout_canvasG1.setObjectName(u"vLayout_canvasG1")
        self.hLayout_toolbarG1 = QHBoxLayout()
        self.hLayout_toolbarG1.setObjectName(u"hLayout_toolbarG1")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_toolbarG1.addItem(self.horizontalSpacer_7)

        self.cb_singleViewG1 = QCheckBox(self.tab_G1)
        self.cb_singleViewG1.setObjectName(u"cb_singleViewG1")

        self.hLayout_toolbarG1.addWidget(self.cb_singleViewG1)

        self.cb_circlesG1 = QCheckBox(self.tab_G1)
        self.cb_circlesG1.setObjectName(u"cb_circlesG1")

        self.hLayout_toolbarG1.addWidget(self.cb_circlesG1)


        self.vLayout_canvasG1.addLayout(self.hLayout_toolbarG1)

        self.tabW_GD.addTab(self.tab_G1, "")
        self.tab_G2 = QWidget()
        self.tab_G2.setObjectName(u"tab_G2")
        self.vLayout_canvasG2 = QVBoxLayout(self.tab_G2)
        self.vLayout_canvasG2.setObjectName(u"vLayout_canvasG2")
        self.hLayout_toolbarG2 = QHBoxLayout()
        self.hLayout_toolbarG2.setObjectName(u"hLayout_toolbarG2")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_toolbarG2.addItem(self.horizontalSpacer_8)

        self.cb_singleViewG2 = QCheckBox(self.tab_G2)
        self.cb_singleViewG2.setObjectName(u"cb_singleViewG2")

        self.hLayout_toolbarG2.addWidget(self.cb_singleViewG2)

        self.cb_circlesG2 = QCheckBox(self.tab_G2)
        self.cb_circlesG2.setObjectName(u"cb_circlesG2")

        self.hLayout_toolbarG2.addWidget(self.cb_circlesG2)


        self.vLayout_canvasG2.addLayout(self.hLayout_toolbarG2)

        self.tabW_GD.addTab(self.tab_G2, "")
        self.tab_Mesh = QWidget()
        self.tab_Mesh.setObjectName(u"tab_Mesh")
        self.vLayout_canvasMesh = QVBoxLayout(self.tab_Mesh)
        self.vLayout_canvasMesh.setObjectName(u"vLayout_canvasMesh")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.tab_Mesh)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.hSlider_Mesh = QSlider(self.tab_Mesh)
        self.hSlider_Mesh.setObjectName(u"hSlider_Mesh")
        self.hSlider_Mesh.setMaximum(200)
        self.hSlider_Mesh.setValue(100)
        self.hSlider_Mesh.setSliderPosition(100)
        self.hSlider_Mesh.setOrientation(Qt.Orientation.Horizontal)
        self.hSlider_Mesh.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.hSlider_Mesh.setTickInterval(100)

        self.horizontalLayout_2.addWidget(self.hSlider_Mesh)


        self.vLayout_canvasMesh.addLayout(self.horizontalLayout_2)

        self.hLayout_toolbarMesh = QHBoxLayout()
        self.hLayout_toolbarMesh.setObjectName(u"hLayout_toolbarMesh")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_toolbarMesh.addItem(self.horizontalSpacer_9)

        self.cb_singleViewMesh = QCheckBox(self.tab_Mesh)
        self.cb_singleViewMesh.setObjectName(u"cb_singleViewMesh")

        self.hLayout_toolbarMesh.addWidget(self.cb_singleViewMesh)

        self.cb_circlesMesh = QCheckBox(self.tab_Mesh)
        self.cb_circlesMesh.setObjectName(u"cb_circlesMesh")

        self.hLayout_toolbarMesh.addWidget(self.cb_circlesMesh)

        self.cb_LoC = QCheckBox(self.tab_Mesh)
        self.cb_LoC.setObjectName(u"cb_LoC")

        self.hLayout_toolbarMesh.addWidget(self.cb_LoC)

        self.pb_animate = QPushButton(self.tab_Mesh)
        self.pb_animate.setObjectName(u"pb_animate")

        self.hLayout_toolbarMesh.addWidget(self.pb_animate)


        self.vLayout_canvasMesh.addLayout(self.hLayout_toolbarMesh)

        self.tabW_GD.addTab(self.tab_Mesh, "")

        self.horizontalLayout.addWidget(self.tabW_GD)

        self.tabW_main.addTab(self.tab_GD, "")
        self.tab_stress = QWidget()
        self.tab_stress.setObjectName(u"tab_stress")
        self.horizontalLayout_6 = QHBoxLayout(self.tab_stress)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_11 = QSpacerItem(13, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(6, 6, -1, 6)
        self.label_86 = QLabel(self.tab_stress)
        self.label_86.setObjectName(u"label_86")
        sizePolicy2.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy2)
        self.label_86.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_86, 8, 0, 1, 1)

        self.label_83 = QLabel(self.tab_stress)
        self.label_83.setObjectName(u"label_83")
        sizePolicy2.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy2)
        self.label_83.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_83, 7, 0, 1, 1)

        self.le_E1 = QLineEdit(self.tab_stress)
        self.le_E1.setObjectName(u"le_E1")
        sizePolicy3.setHeightForWidth(self.le_E1.sizePolicy().hasHeightForWidth())
        self.le_E1.setSizePolicy(sizePolicy3)
        self.le_E1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_E1, 8, 2, 1, 1)

        self.le_torque = QLineEdit(self.tab_stress)
        self.le_torque.setObjectName(u"le_torque")
        sizePolicy3.setHeightForWidth(self.le_torque.sizePolicy().hasHeightForWidth())
        self.le_torque.setSizePolicy(sizePolicy3)
        self.le_torque.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_torque, 4, 2, 1, 1)

        self.label_77 = QLabel(self.tab_stress)
        self.label_77.setObjectName(u"label_77")
        sizePolicy2.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy2)
        self.label_77.setFont(font)
        self.label_77.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_77, 11, 1, 1, 1)

        self.label_84 = QLabel(self.tab_stress)
        self.label_84.setObjectName(u"label_84")
        sizePolicy2.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy2)
        self.label_84.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_84, 4, 0, 1, 1)

        self.lb_stressC2 = QLabel(self.tab_stress)
        self.lb_stressC2.setObjectName(u"lb_stressC2")
        sizePolicy2.setHeightForWidth(self.lb_stressC2.sizePolicy().hasHeightForWidth())
        self.lb_stressC2.setSizePolicy(sizePolicy2)
        self.lb_stressC2.setFont(font)
        self.lb_stressC2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_stressC2, 12, 3, 1, 1)

        self.le_E2 = QLineEdit(self.tab_stress)
        self.le_E2.setObjectName(u"le_E2")
        sizePolicy3.setHeightForWidth(self.le_E2.sizePolicy().hasHeightForWidth())
        self.le_E2.setSizePolicy(sizePolicy3)
        self.le_E2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_E2, 8, 3, 1, 1)

        self.label_85 = QLabel(self.tab_stress)
        self.label_85.setObjectName(u"label_85")
        sizePolicy2.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy2)
        self.label_85.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_85, 3, 0, 1, 1)

        self.le_FW1 = QLineEdit(self.tab_stress)
        self.le_FW1.setObjectName(u"le_FW1")
        sizePolicy3.setHeightForWidth(self.le_FW1.sizePolicy().hasHeightForWidth())
        self.le_FW1.setSizePolicy(sizePolicy3)
        self.le_FW1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_FW1, 7, 2, 1, 1)

        self.label_79 = QLabel(self.tab_stress)
        self.label_79.setObjectName(u"label_79")
        sizePolicy2.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy2)
        self.label_79.setFont(font)
        self.label_79.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_79, 12, 1, 1, 1)

        self.le_FW2 = QLineEdit(self.tab_stress)
        self.le_FW2.setObjectName(u"le_FW2")
        sizePolicy3.setHeightForWidth(self.le_FW2.sizePolicy().hasHeightForWidth())
        self.le_FW2.setSizePolicy(sizePolicy3)
        self.le_FW2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_FW2, 7, 3, 1, 1)

        self.line_15 = QFrame(self.tab_stress)
        self.line_15.setObjectName(u"line_15")
        sizePolicy3.setHeightForWidth(self.line_15.sizePolicy().hasHeightForWidth())
        self.line_15.setSizePolicy(sizePolicy3)
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_15, 10, 0, 1, 4)

        self.label_63 = QLabel(self.tab_stress)
        self.label_63.setObjectName(u"label_63")
        sizePolicy2.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy2)
        self.label_63.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_63, 8, 1, 1, 1)

        self.label_82 = QLabel(self.tab_stress)
        self.label_82.setObjectName(u"label_82")
        sizePolicy2.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy2)
        self.label_82.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_82, 6, 3, 1, 1)

        self.le_speed = QLineEdit(self.tab_stress)
        self.le_speed.setObjectName(u"le_speed")
        sizePolicy3.setHeightForWidth(self.le_speed.sizePolicy().hasHeightForWidth())
        self.le_speed.setSizePolicy(sizePolicy3)
        self.le_speed.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_speed, 3, 2, 1, 1)

        self.label_37 = QLabel(self.tab_stress)
        self.label_37.setObjectName(u"label_37")
        sizePolicy2.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy2)
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_37, 6, 2, 1, 1)

        self.label_87 = QLabel(self.tab_stress)
        self.label_87.setObjectName(u"label_87")
        sizePolicy2.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy2)
        self.label_87.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_87, 9, 0, 1, 1)

        self.label_56 = QLabel(self.tab_stress)
        self.label_56.setObjectName(u"label_56")
        sizePolicy2.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy2)
        self.label_56.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_56, 7, 1, 1, 1)

        self.lb_stressB1 = QLabel(self.tab_stress)
        self.lb_stressB1.setObjectName(u"lb_stressB1")
        sizePolicy2.setHeightForWidth(self.lb_stressB1.sizePolicy().hasHeightForWidth())
        self.lb_stressB1.setSizePolicy(sizePolicy2)
        self.lb_stressB1.setFont(font)
        self.lb_stressB1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_stressB1, 11, 2, 1, 1)

        self.label_64 = QLabel(self.tab_stress)
        self.label_64.setObjectName(u"label_64")
        sizePolicy2.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy2)
        self.label_64.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_64, 9, 1, 1, 1)

        self.lb_stressC1 = QLabel(self.tab_stress)
        self.lb_stressC1.setObjectName(u"lb_stressC1")
        sizePolicy2.setHeightForWidth(self.lb_stressC1.sizePolicy().hasHeightForWidth())
        self.lb_stressC1.setSizePolicy(sizePolicy2)
        self.lb_stressC1.setFont(font)
        self.lb_stressC1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_stressC1, 12, 2, 1, 1)

        self.label_78 = QLabel(self.tab_stress)
        self.label_78.setObjectName(u"label_78")
        sizePolicy2.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy2)
        self.label_78.setFont(font)
        self.label_78.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_78, 12, 0, 1, 1)

        self.le_nu2 = QLineEdit(self.tab_stress)
        self.le_nu2.setObjectName(u"le_nu2")
        sizePolicy3.setHeightForWidth(self.le_nu2.sizePolicy().hasHeightForWidth())
        self.le_nu2.setSizePolicy(sizePolicy3)
        self.le_nu2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_nu2, 9, 3, 1, 1)

        self.label_76 = QLabel(self.tab_stress)
        self.label_76.setObjectName(u"label_76")
        sizePolicy2.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy2)
        self.label_76.setFont(font)
        self.label_76.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_76, 11, 0, 1, 1)

        self.le_nu1 = QLineEdit(self.tab_stress)
        self.le_nu1.setObjectName(u"le_nu1")
        sizePolicy3.setHeightForWidth(self.le_nu1.sizePolicy().hasHeightForWidth())
        self.le_nu1.setSizePolicy(sizePolicy3)
        self.le_nu1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_nu1, 9, 2, 1, 1)

        self.label_61 = QLabel(self.tab_stress)
        self.label_61.setObjectName(u"label_61")
        sizePolicy2.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy2)
        self.label_61.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_61, 4, 1, 1, 1)

        self.line_14 = QFrame(self.tab_stress)
        self.line_14.setObjectName(u"line_14")
        sizePolicy3.setHeightForWidth(self.line_14.sizePolicy().hasHeightForWidth())
        self.line_14.setSizePolicy(sizePolicy3)
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_14, 14, 0, 1, 4)

        self.lb_stressB2 = QLabel(self.tab_stress)
        self.lb_stressB2.setObjectName(u"lb_stressB2")
        sizePolicy2.setHeightForWidth(self.lb_stressB2.sizePolicy().hasHeightForWidth())
        self.lb_stressB2.setSizePolicy(sizePolicy2)
        self.lb_stressB2.setFont(font)
        self.lb_stressB2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_stressB2, 11, 3, 1, 1)

        self.label_62 = QLabel(self.tab_stress)
        self.label_62.setObjectName(u"label_62")
        sizePolicy2.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy2)
        self.label_62.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_62, 3, 1, 1, 1)

        self.line_16 = QFrame(self.tab_stress)
        self.line_16.setObjectName(u"line_16")
        sizePolicy3.setHeightForWidth(self.line_16.sizePolicy().hasHeightForWidth())
        self.line_16.setSizePolicy(sizePolicy3)
        self.line_16.setFrameShape(QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_16, 5, 0, 1, 4)

        self.label_80 = QLabel(self.tab_stress)
        self.label_80.setObjectName(u"label_80")
        sizePolicy2.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy2)
        self.label_80.setFont(font)
        self.label_80.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_80, 13, 0, 1, 1)

        self.label_81 = QLabel(self.tab_stress)
        self.label_81.setObjectName(u"label_81")
        sizePolicy2.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy2)
        self.label_81.setFont(font)
        self.label_81.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_81, 13, 1, 1, 1)

        self.lb_pitchLineVel = QLabel(self.tab_stress)
        self.lb_pitchLineVel.setObjectName(u"lb_pitchLineVel")
        sizePolicy2.setHeightForWidth(self.lb_pitchLineVel.sizePolicy().hasHeightForWidth())
        self.lb_pitchLineVel.setSizePolicy(sizePolicy2)
        self.lb_pitchLineVel.setFont(font)
        self.lb_pitchLineVel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_pitchLineVel, 13, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.pb_stress = QPushButton(self.tab_stress)
        self.pb_stress.setObjectName(u"pb_stress")

        self.verticalLayout_4.addWidget(self.pb_stress)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(13, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.tabWidget = QTabWidget(self.tab_stress)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tab_stress1 = QWidget()
        self.tab_stress1.setObjectName(u"tab_stress1")
        self.tabWidget.addTab(self.tab_stress1, "")
        self.tab_stress2 = QWidget()
        self.tab_stress2.setObjectName(u"tab_stress2")
        self.tabWidget.addTab(self.tab_stress2, "")

        self.horizontalLayout_6.addWidget(self.tabWidget)

        self.tabW_main.addTab(self.tab_stress, "")

        self.topLayout.addWidget(self.tabW_main)

        QWidget.setTabOrder(self.le_targetMod, self.le_targetGR)
        QWidget.setTabOrder(self.le_targetGR, self.cb_CD_width)
        QWidget.setTabOrder(self.cb_CD_width, self.le_targetSize)
        QWidget.setTabOrder(self.le_targetSize, self.pb_calcGearSizes)
        QWidget.setTabOrder(self.pb_calcGearSizes, self.le_pN)
        QWidget.setTabOrder(self.le_pN, self.rb_1)
        QWidget.setTabOrder(self.rb_1, self.rb_2)
        QWidget.setTabOrder(self.rb_2, self.rb_3)
        QWidget.setTabOrder(self.rb_3, self.rb_4)
        QWidget.setTabOrder(self.rb_4, self.rb_5)
        QWidget.setTabOrder(self.rb_5, self.pb_useLayout)
        QWidget.setTabOrder(self.pb_useLayout, self.le_mod)
        QWidget.setTabOrder(self.le_mod, self.le_PA_deg)
        QWidget.setTabOrder(self.le_PA_deg, self.cb_CD_bkl)
        QWidget.setTabOrder(self.cb_CD_bkl, self.le_CD_bkl)
        QWidget.setTabOrder(self.le_CD_bkl, self.le_N1)
        QWidget.setTabOrder(self.le_N1, self.le_N2)
        QWidget.setTabOrder(self.le_N2, self.le_x1)
        QWidget.setTabOrder(self.le_x1, self.le_x2)
        QWidget.setTabOrder(self.le_x2, self.le_Ro1)
        QWidget.setTabOrder(self.le_Ro1, self.le_Ro2)
        QWidget.setTabOrder(self.le_Ro2, self.le_Rtip1)
        QWidget.setTabOrder(self.le_Rtip1, self.le_Rtip2)
        QWidget.setTabOrder(self.le_Rtip2, self.le_rtcl1)
        QWidget.setTabOrder(self.le_rtcl1, self.le_rtcl2)
        QWidget.setTabOrder(self.le_rtcl2, self.le_Rf1)
        QWidget.setTabOrder(self.le_Rf1, self.le_Rf2)
        QWidget.setTabOrder(self.le_Rf2, self.pb_drawGear)
        QWidget.setTabOrder(self.pb_drawGear, self.tabW_GD)
        QWidget.setTabOrder(self.tabW_GD, self.cb_singleViewG1)
        QWidget.setTabOrder(self.cb_singleViewG1, self.cb_circlesG1)
        QWidget.setTabOrder(self.cb_circlesG1, self.cb_singleViewG2)
        QWidget.setTabOrder(self.cb_singleViewG2, self.cb_circlesG2)
        QWidget.setTabOrder(self.cb_circlesG2, self.hSlider_Mesh)
        QWidget.setTabOrder(self.hSlider_Mesh, self.cb_singleViewMesh)
        QWidget.setTabOrder(self.cb_singleViewMesh, self.cb_circlesMesh)
        QWidget.setTabOrder(self.cb_circlesMesh, self.cb_LoC)
        QWidget.setTabOrder(self.cb_LoC, self.pb_animate)
        QWidget.setTabOrder(self.pb_animate, self.le_speed)
        QWidget.setTabOrder(self.le_speed, self.le_torque)
        QWidget.setTabOrder(self.le_torque, self.le_FW1)
        QWidget.setTabOrder(self.le_FW1, self.le_FW2)
        QWidget.setTabOrder(self.le_FW2, self.le_E1)
        QWidget.setTabOrder(self.le_E1, self.le_E2)
        QWidget.setTabOrder(self.le_E2, self.le_nu1)
        QWidget.setTabOrder(self.le_nu1, self.le_nu2)
        QWidget.setTabOrder(self.le_nu2, self.pb_stress)
        QWidget.setTabOrder(self.pb_stress, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.tabW_main)

        self.retranslateUi(jpgearqt)

        self.tabW_main.setCurrentIndex(0)
        self.cb_CD_bkl.setCurrentIndex(0)
        self.tabW_GD.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(jpgearqt)
    # setupUi

    def retranslateUi(self, jpgearqt):
        jpgearqt.setWindowTitle(QCoreApplication.translate("jpgearqt", u"jpGear", None))
        self.actiontest.setText(QCoreApplication.translate("jpgearqt", u"test", None))
        self.lb_TargetModule.setText(QCoreApplication.translate("jpgearqt", u"Target Module", None))
        self.lb_TargetGearRatio.setText(QCoreApplication.translate("jpgearqt", u"Target Gear Ratio", None))
        self.cb_CD_width.setItemText(0, QCoreApplication.translate("jpgearqt", u"Target Center Distance", None))
        self.cb_CD_width.setItemText(1, QCoreApplication.translate("jpgearqt", u"Target Overall Width", None))

        self.pb_calcGearSizes.setText(QCoreApplication.translate("jpgearqt", u"Find Gear Sizes", None))
        self.lb_CenterDistance.setText(QCoreApplication.translate("jpgearqt", u"Center Distance", None))
        self.rb_2.setText("")
        self.rb_3.setText("")
        self.lb_gN4.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_gN1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_icon1.setText("")
        self.lb_GR1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_width5.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_gN2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_GearRatio.setText(QCoreApplication.translate("jpgearqt", u"Gear Ratio", None))
        self.lb_width1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_CD5.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.pb_useLayout.setText(QCoreApplication.translate("jpgearqt", u"Use this Layout", None))
        self.lb_icon3.setText("")
        self.lb_GR4.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.rb_1.setText("")
        self.lb_CD2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_icon5.setText("")
        self.lb_width3.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_width4.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_teeth.setText(QCoreApplication.translate("jpgearqt", u"Teeth", None))
        self.lb_teeth_2.setText(QCoreApplication.translate("jpgearqt", u"Teeth", None))
        self.rb_4.setText("")
        self.lb_icon2.setText("")
        self.lb_gN5.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_OverallWidth.setText(QCoreApplication.translate("jpgearqt", u"Overall Width", None))
        self.rb_5.setText("")
        self.lb_icon4.setText("")
        self.lb_GR5.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_CD1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_width2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_CD4.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_gear.setText(QCoreApplication.translate("jpgearqt", u"Gear", None))
        self.lb_CD3.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_pinion.setText(QCoreApplication.translate("jpgearqt", u"Pinion", None))
        self.lb_GR3.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_gN3.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_GR2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.tabW_main.setTabText(self.tabW_main.indexOf(self.tab_layout), QCoreApplication.translate("jpgearqt", u"Layout Helper", None))
        self.lb_CD_value.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_bkl_units.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.label_45.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.label_57.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.label_16.setText(QCoreApplication.translate("jpgearqt", u"Root Clearance", None))
        self.label_65.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.lb_tts1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_undercut2.setText("")
        self.label_43.setText(QCoreApplication.translate("jpgearqt", u"Standard Pitch Radius", None))
        self.label_54.setText(QCoreApplication.translate("jpgearqt", u"Contact Ratio", None))
        self.lb_CR.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_bkl_text.setText(QCoreApplication.translate("jpgearqt", u"Backlash", None))
        self.lb_Roe1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_27.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.label_30.setText(QCoreApplication.translate("jpgearqt", u"Outer Radius", None))
        self.label_31.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.lb_tt2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_Rtipmax2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_52.setText(QCoreApplication.translate("jpgearqt", u"Standard Tooth Thickness", None))
        self.lb_bkl_value.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_20.setText(QCoreApplication.translate("jpgearqt", u"Module", None))
        self.lb_undercut1.setText("")
        self.label_49.setText(QCoreApplication.translate("jpgearqt", u"Effective Outer Radius", None))
        self.label_50.setText(QCoreApplication.translate("jpgearqt", u"Pitch Radius", None))
        self.label_53.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.label_58.setText(QCoreApplication.translate("jpgearqt", u"Gear Ratio", None))
        self.label_24.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.cb_CD_bkl.setItemText(0, QCoreApplication.translate("jpgearqt", u"Backlash", None))
        self.cb_CD_bkl.setItemText(1, QCoreApplication.translate("jpgearqt", u"Center Distance", None))

        self.cb_CD_bkl.setCurrentText(QCoreApplication.translate("jpgearqt", u"Backlash", None))
        self.label_29.setText(QCoreApplication.translate("jpgearqt", u"deg", None))
        self.label_15.setText(QCoreApplication.translate("jpgearqt", u"Root Fillet", None))
        self.label_46.setText(QCoreApplication.translate("jpgearqt", u"Root Radius", None))
        self.lb_Rp1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_39.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.label_51.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.lb_tt1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_Romax2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_13.setText(QCoreApplication.translate("jpgearqt", u"Max Outer Radius", None))
        self.label_32.setText(QCoreApplication.translate("jpgearqt", u"Standard Outer Radius", None))
        self.label_44.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.lb_Rff2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_Ros2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_42.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.label_59.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_Rs2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_48.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.lb_Rtipmax1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_GR.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_40.setText(QCoreApplication.translate("jpgearqt", u"Max Root Fillet", None))
        self.label_12.setText(QCoreApplication.translate("jpgearqt", u"Profile Shift Coefficient", None))
        self.lb_Romax1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_CD_text.setText(QCoreApplication.translate("jpgearqt", u"Center Distance", None))
        self.lb_Rr1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_14.setText(QCoreApplication.translate("jpgearqt", u"Max Tip Fillet", None))
        self.label_18.setText(QCoreApplication.translate("jpgearqt", u"Pressure Angle", None))
        self.label_6.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_Roe2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_Rs1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_35.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.lb_Rr2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_Rff1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_34.setText(QCoreApplication.translate("jpgearqt", u"Tip Fillet", None))
        self.lb_Ros1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_CD_units.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.label_47.setText(QCoreApplication.translate("jpgearqt", u"Tooth Thickness", None))
        self.label_41.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.label_22.setText(QCoreApplication.translate("jpgearqt", u"Teeth", None))
        self.label_17.setText(QCoreApplication.translate("jpgearqt", u"Gear 1", None))
        self.label_19.setText(QCoreApplication.translate("jpgearqt", u"Gear 2", None))
        self.lb_Rp2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_60.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_25.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.label_55.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_tts2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_21.setText(QCoreApplication.translate("jpgearqt", u"Common", None))
        self.label_28.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.label_66.setText(QCoreApplication.translate("jpgearqt", u"Standard Root Radius", None))
        self.label_67.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.lb_Rrs1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_Rrs2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.pb_drawGear.setText(QCoreApplication.translate("jpgearqt", u"Draw Gears", None))
        self.cb_singleViewG1.setText(QCoreApplication.translate("jpgearqt", u"Single Tooth View", None))
        self.cb_circlesG1.setText(QCoreApplication.translate("jpgearqt", u"Show Circles", None))
        self.tabW_GD.setTabText(self.tabW_GD.indexOf(self.tab_G1), QCoreApplication.translate("jpgearqt", u"Gear 1", None))
        self.cb_singleViewG2.setText(QCoreApplication.translate("jpgearqt", u"Single Tooth View", None))
        self.cb_circlesG2.setText(QCoreApplication.translate("jpgearqt", u"Show Circles", None))
        self.tabW_GD.setTabText(self.tabW_GD.indexOf(self.tab_G2), QCoreApplication.translate("jpgearqt", u"Gear 2", None))
        self.label.setText(QCoreApplication.translate("jpgearqt", u"Rotate", None))
        self.cb_singleViewMesh.setText(QCoreApplication.translate("jpgearqt", u"Mesh View", None))
        self.cb_circlesMesh.setText(QCoreApplication.translate("jpgearqt", u"Show Circles", None))
        self.cb_LoC.setText(QCoreApplication.translate("jpgearqt", u"Show Line of Contact", None))
        self.pb_animate.setText(QCoreApplication.translate("jpgearqt", u"Animate", None))
        self.tabW_GD.setTabText(self.tabW_GD.indexOf(self.tab_Mesh), QCoreApplication.translate("jpgearqt", u"Mesh", None))
        self.tabW_main.setTabText(self.tabW_main.indexOf(self.tab_GD), QCoreApplication.translate("jpgearqt", u"Gear Designer", None))
        self.label_86.setText(QCoreApplication.translate("jpgearqt", u"Young's Modulus", None))
        self.label_83.setText(QCoreApplication.translate("jpgearqt", u"Face Width", None))
        self.le_E1.setText("")
        self.le_torque.setText("")
        self.label_77.setText(QCoreApplication.translate("jpgearqt", u"Mpa", None))
        self.label_84.setText(QCoreApplication.translate("jpgearqt", u"Pinion Torque", None))
        self.lb_stressC2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.le_E2.setText("")
        self.label_85.setText(QCoreApplication.translate("jpgearqt", u"Pinion Speed", None))
        self.le_FW1.setText("")
        self.label_79.setText(QCoreApplication.translate("jpgearqt", u"Mpa", None))
        self.le_FW2.setText("")
        self.label_63.setText(QCoreApplication.translate("jpgearqt", u"MPa", None))
        self.label_82.setText(QCoreApplication.translate("jpgearqt", u"Gear 2", None))
        self.le_speed.setText("")
        self.label_37.setText(QCoreApplication.translate("jpgearqt", u"Gear 1", None))
        self.label_87.setText(QCoreApplication.translate("jpgearqt", u"Poisson's Ratio", None))
        self.label_56.setText(QCoreApplication.translate("jpgearqt", u"mm", None))
        self.lb_stressB1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_64.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.lb_stressC1.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_78.setText(QCoreApplication.translate("jpgearqt", u"Contact Stress", None))
        self.le_nu2.setText("")
        self.label_76.setText(QCoreApplication.translate("jpgearqt", u"Bending Stress", None))
        self.le_nu1.setText("")
        self.label_61.setText(QCoreApplication.translate("jpgearqt", u"Nmm", None))
        self.lb_stressB2.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.label_62.setText(QCoreApplication.translate("jpgearqt", u"RPM", None))
        self.label_80.setText(QCoreApplication.translate("jpgearqt", u"Pitch Line Velocity", None))
        self.label_81.setText(QCoreApplication.translate("jpgearqt", u"m/s", None))
        self.lb_pitchLineVel.setText(QCoreApplication.translate("jpgearqt", u"-", None))
        self.pb_stress.setText(QCoreApplication.translate("jpgearqt", u"Calculate Stress", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stress1), QCoreApplication.translate("jpgearqt", u"Gear 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stress2), QCoreApplication.translate("jpgearqt", u"Gear 2", None))
        self.tabW_main.setTabText(self.tabW_main.indexOf(self.tab_stress), QCoreApplication.translate("jpgearqt", u"Stress", None))
    # retranslateUi

