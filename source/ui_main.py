# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.setWindowModality(Qt.WindowModality.NonModal)
        MainForm.resize(1400, 1015)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainForm.sizePolicy().hasHeightForWidth())
        MainForm.setSizePolicy(sizePolicy)
        MainForm.setMinimumSize(QSize(0, 0))
        self.topLayout = QVBoxLayout(MainForm)
        self.topLayout.setObjectName(u"topLayout")
        self.tabW_main = QTabWidget(MainForm)
        self.tabW_main.setObjectName(u"tabW_main")
        self.tabW_main.setTabPosition(QTabWidget.TabPosition.West)
        self.tab_layout = QWidget()
        self.tab_layout.setObjectName(u"tab_layout")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tab_layout.sizePolicy().hasHeightForWidth())
        self.tab_layout.setSizePolicy(sizePolicy1)
        self.horizontalLayout_5 = QHBoxLayout(self.tab_layout)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(6, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalSpacer_4 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.vl_style = QVBoxLayout()
        self.vl_style.setObjectName(u"vl_style")
        self.vl_style.setContentsMargins(6, -1, 6, 10)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 10)
        self.label_2 = QLabel(self.tab_layout)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.line_22 = QFrame(self.tab_layout)
        self.line_22.setObjectName(u"line_22")
        font1 = QFont()
        font1.setBold(False)
        self.line_22.setFont(font1)
        self.line_22.setFrameShadow(QFrame.Shadow.Raised)
        self.line_22.setLineWidth(5)
        self.line_22.setFrameShape(QFrame.Shape.HLine)

        self.horizontalLayout_7.addWidget(self.line_22)


        self.vl_style.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.cb_type_helper = QComboBox(self.tab_layout)
        self.cb_type_helper.addItem("")
        self.cb_type_helper.addItem("")
        self.cb_type_helper.addItem("")
        self.cb_type_helper.setObjectName(u"cb_type_helper")

        self.horizontalLayout_10.addWidget(self.cb_type_helper)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)

        self.frame_pLayout_helper = QFrame(self.tab_layout)
        self.frame_pLayout_helper.setObjectName(u"frame_pLayout_helper")
        sizePolicy.setHeightForWidth(self.frame_pLayout_helper.sizePolicy().hasHeightForWidth())
        self.frame_pLayout_helper.setSizePolicy(sizePolicy)
        self.frame_pLayout_helper.setMinimumSize(QSize(0, 0))
        self.frame_pLayout_helper.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_pLayout_helper.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_pLayout_helper)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.glayout_planet_helper = QGridLayout()
        self.glayout_planet_helper.setObjectName(u"glayout_planet_helper")
        self.glayout_planet_helper.setHorizontalSpacing(10)
        self.glayout_planet_helper.setVerticalSpacing(6)
        self.glayout_planet_helper.setContentsMargins(0, 0, 0, 0)
        self.cb_output_helper = QComboBox(self.frame_pLayout_helper)
        self.cb_output_helper.addItem("")
        self.cb_output_helper.addItem("")
        self.cb_output_helper.addItem("")
        self.cb_output_helper.setObjectName(u"cb_output_helper")
        sizePolicy1.setHeightForWidth(self.cb_output_helper.sizePolicy().hasHeightForWidth())
        self.cb_output_helper.setSizePolicy(sizePolicy1)

        self.glayout_planet_helper.addWidget(self.cb_output_helper, 1, 1, 1, 1)

        self.lb_input = QLabel(self.frame_pLayout_helper)
        self.lb_input.setObjectName(u"lb_input")
        self.lb_input.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lb_input.setWordWrap(True)

        self.glayout_planet_helper.addWidget(self.lb_input, 0, 0, 1, 1)

        self.lb_stationary = QLabel(self.frame_pLayout_helper)
        self.lb_stationary.setObjectName(u"lb_stationary")
        self.lb_stationary.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lb_stationary.setWordWrap(True)

        self.glayout_planet_helper.addWidget(self.lb_stationary, 2, 0, 1, 1)

        self.lb_stationGear1 = QLabel(self.frame_pLayout_helper)
        self.lb_stationGear1.setObjectName(u"lb_stationGear1")
        self.lb_stationGear1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.glayout_planet_helper.addWidget(self.lb_stationGear1, 2, 1, 1, 1)

        self.lb_output = QLabel(self.frame_pLayout_helper)
        self.lb_output.setObjectName(u"lb_output")
        self.lb_output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lb_output.setWordWrap(True)

        self.glayout_planet_helper.addWidget(self.lb_output, 1, 0, 1, 1)

        self.cb_input_helper = QComboBox(self.frame_pLayout_helper)
        self.cb_input_helper.addItem("")
        self.cb_input_helper.addItem("")
        self.cb_input_helper.addItem("")
        self.cb_input_helper.setObjectName(u"cb_input_helper")
        sizePolicy1.setHeightForWidth(self.cb_input_helper.sizePolicy().hasHeightForWidth())
        self.cb_input_helper.setSizePolicy(sizePolicy1)
        self.cb_input_helper.setEditable(False)

        self.glayout_planet_helper.addWidget(self.cb_input_helper, 0, 1, 1, 1)


        self.horizontalLayout_11.addLayout(self.glayout_planet_helper)


        self.horizontalLayout_10.addWidget(self.frame_pLayout_helper)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.vl_style.addLayout(self.horizontalLayout_10)


        self.verticalLayout_3.addLayout(self.vl_style)

        self.vl_size = QVBoxLayout()
        self.vl_size.setObjectName(u"vl_size")
        self.vl_size.setContentsMargins(6, -1, 6, 15)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 10)
        self.label_3 = QLabel(self.tab_layout)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.line_12 = QFrame(self.tab_layout)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShadow(QFrame.Shadow.Raised)
        self.line_12.setLineWidth(5)
        self.line_12.setFrameShape(QFrame.Shape.HLine)

        self.horizontalLayout_3.addWidget(self.line_12)


        self.vl_size.addLayout(self.horizontalLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.lb_targetCD_unit = QLabel(self.tab_layout)
        self.lb_targetCD_unit.setObjectName(u"lb_targetCD_unit")
        sizePolicy2.setHeightForWidth(self.lb_targetCD_unit.sizePolicy().hasHeightForWidth())
        self.lb_targetCD_unit.setSizePolicy(sizePolicy2)
        self.lb_targetCD_unit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.lb_targetCD_unit, 5, 2, 1, 1)

        self.cb_CD_width = QComboBox(self.tab_layout)
        self.cb_CD_width.addItem("")
        self.cb_CD_width.addItem("")
        self.cb_CD_width.setObjectName(u"cb_CD_width")
        sizePolicy2.setHeightForWidth(self.cb_CD_width.sizePolicy().hasHeightForWidth())
        self.cb_CD_width.setSizePolicy(sizePolicy2)
        self.cb_CD_width.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_4.addWidget(self.cb_CD_width, 5, 0, 1, 1)

        self.le_targetGR = QLineEdit(self.tab_layout)
        self.le_targetGR.setObjectName(u"le_targetGR")
        sizePolicy2.setHeightForWidth(self.le_targetGR.sizePolicy().hasHeightForWidth())
        self.le_targetGR.setSizePolicy(sizePolicy2)
        self.le_targetGR.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.le_targetGR, 3, 1, 1, 1)

        self.le_targetSize = QLineEdit(self.tab_layout)
        self.le_targetSize.setObjectName(u"le_targetSize")
        sizePolicy2.setHeightForWidth(self.le_targetSize.sizePolicy().hasHeightForWidth())
        self.le_targetSize.setSizePolicy(sizePolicy2)
        self.le_targetSize.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.le_targetSize, 5, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 3, 3, 1, 1)

        self.pb_calcGearSizes = QPushButton(self.tab_layout)
        self.pb_calcGearSizes.setObjectName(u"pb_calcGearSizes")
        sizePolicy.setHeightForWidth(self.pb_calcGearSizes.sizePolicy().hasHeightForWidth())
        self.pb_calcGearSizes.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.pb_calcGearSizes, 6, 1, 1, 1)

        self.lb_TargetGearRatio = QLabel(self.tab_layout)
        self.lb_TargetGearRatio.setObjectName(u"lb_TargetGearRatio")
        sizePolicy2.setHeightForWidth(self.lb_TargetGearRatio.sizePolicy().hasHeightForWidth())
        self.lb_TargetGearRatio.setSizePolicy(sizePolicy2)
        self.lb_TargetGearRatio.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.lb_TargetGearRatio, 3, 0, 1, 1)

        self.lb_targetMod_unit = QLabel(self.tab_layout)
        self.lb_targetMod_unit.setObjectName(u"lb_targetMod_unit")
        sizePolicy2.setHeightForWidth(self.lb_targetMod_unit.sizePolicy().hasHeightForWidth())
        self.lb_targetMod_unit.setSizePolicy(sizePolicy2)
        self.lb_targetMod_unit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.lb_targetMod_unit, 1, 2, 1, 1)

        self.lb_TargetModule = QLabel(self.tab_layout)
        self.lb_TargetModule.setObjectName(u"lb_TargetModule")
        sizePolicy2.setHeightForWidth(self.lb_TargetModule.sizePolicy().hasHeightForWidth())
        self.lb_TargetModule.setSizePolicy(sizePolicy2)
        self.lb_TargetModule.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.lb_TargetModule, 1, 0, 1, 1)

        self.lb_TargetModule_3 = QLabel(self.tab_layout)
        self.lb_TargetModule_3.setObjectName(u"lb_TargetModule_3")
        sizePolicy2.setHeightForWidth(self.lb_TargetModule_3.sizePolicy().hasHeightForWidth())
        self.lb_TargetModule_3.setSizePolicy(sizePolicy2)
        self.lb_TargetModule_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.lb_TargetModule_3, 3, 2, 1, 1)

        self.le_targetMod = QLineEdit(self.tab_layout)
        self.le_targetMod.setObjectName(u"le_targetMod")
        sizePolicy2.setHeightForWidth(self.le_targetMod.sizePolicy().hasHeightForWidth())
        self.le_targetMod.setSizePolicy(sizePolicy2)
        self.le_targetMod.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.le_targetMod, 1, 1, 1, 1)


        self.vl_size.addLayout(self.gridLayout_4)


        self.verticalLayout_3.addLayout(self.vl_size)

        self.vl_teeth = QVBoxLayout()
        self.vl_teeth.setSpacing(6)
        self.vl_teeth.setObjectName(u"vl_teeth")
        self.vl_teeth.setContentsMargins(6, 0, 6, 15)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 10)
        self.label_7 = QLabel(self.tab_layout)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.line_26 = QFrame(self.tab_layout)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShadow(QFrame.Shadow.Raised)
        self.line_26.setLineWidth(5)
        self.line_26.setFrameShape(QFrame.Shape.HLine)

        self.horizontalLayout_9.addWidget(self.line_26)


        self.vl_teeth.addLayout(self.horizontalLayout_9)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(6)
        self.lb_planet = QLabel(self.tab_layout)
        self.lb_planet.setObjectName(u"lb_planet")
        self.lb_planet.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_planet, 0, 3, 1, 1)

        self.lb_width2 = QLabel(self.tab_layout)
        self.lb_width2.setObjectName(u"lb_width2")
        self.lb_width2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_width2, 3, 7, 1, 1)

        self.lb_N3_4 = QLabel(self.tab_layout)
        self.lb_N3_4.setObjectName(u"lb_N3_4")
        self.lb_N3_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_N3_4, 5, 3, 1, 1)

        self.lb_GearRatio = QLabel(self.tab_layout)
        self.lb_GearRatio.setObjectName(u"lb_GearRatio")
        self.lb_GearRatio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_GearRatio, 0, 5, 1, 1)

        self.lb_width1 = QLabel(self.tab_layout)
        self.lb_width1.setObjectName(u"lb_width1")
        self.lb_width1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_width1, 2, 7, 1, 1)

        self.lb_CD5 = QLabel(self.tab_layout)
        self.lb_CD5.setObjectName(u"lb_CD5")
        self.lb_CD5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_CD5, 6, 6, 1, 1)

        self.lb_CD3 = QLabel(self.tab_layout)
        self.lb_CD3.setObjectName(u"lb_CD3")
        self.lb_CD3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_CD3, 4, 6, 1, 1)

        self.le_N1_layout = QLineEdit(self.tab_layout)
        self.le_N1_layout.setObjectName(u"le_N1_layout")
        sizePolicy1.setHeightForWidth(self.le_N1_layout.sizePolicy().hasHeightForWidth())
        self.le_N1_layout.setSizePolicy(sizePolicy1)
        self.le_N1_layout.setMaximumSize(QSize(60, 22))
        self.le_N1_layout.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.le_N1_layout, 4, 1, 1, 1)

        self.rb_3 = QRadioButton(self.tab_layout)
        self.bg_layout = QButtonGroup(MainForm)
        self.bg_layout.setObjectName(u"bg_layout")
        self.bg_layout.addButton(self.rb_3)
        self.rb_3.setObjectName(u"rb_3")
        self.rb_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.rb_3.setChecked(True)

        self.gridLayout_2.addWidget(self.rb_3, 4, 10, 1, 1)

        self.lb_width3 = QLabel(self.tab_layout)
        self.lb_width3.setObjectName(u"lb_width3")
        self.lb_width3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_width3, 4, 7, 1, 1)

        self.lb_icon4 = QLabel(self.tab_layout)
        self.lb_icon4.setObjectName(u"lb_icon4")
        self.lb_icon4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_icon4, 5, 8, 1, 1)

        self.rb_4 = QRadioButton(self.tab_layout)
        self.bg_layout.addButton(self.rb_4)
        self.rb_4.setObjectName(u"rb_4")
        self.rb_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_2.addWidget(self.rb_4, 5, 10, 1, 1)

        self.lb_N3_5 = QLabel(self.tab_layout)
        self.lb_N3_5.setObjectName(u"lb_N3_5")
        self.lb_N3_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_N3_5, 6, 3, 1, 1)

        self.lb_width4 = QLabel(self.tab_layout)
        self.lb_width4.setObjectName(u"lb_width4")
        self.lb_width4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_width4, 5, 7, 1, 1)

        self.lb_GR5 = QLabel(self.tab_layout)
        self.lb_GR5.setObjectName(u"lb_GR5")
        self.lb_GR5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_GR5, 6, 5, 1, 1)

        self.lb_N3_3 = QLabel(self.tab_layout)
        self.lb_N3_3.setObjectName(u"lb_N3_3")
        self.lb_N3_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_N3_3, 4, 3, 1, 1)

        self.lb_CD2 = QLabel(self.tab_layout)
        self.lb_CD2.setObjectName(u"lb_CD2")
        self.lb_CD2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_CD2, 3, 6, 1, 1)

        self.rb_5 = QRadioButton(self.tab_layout)
        self.bg_layout.addButton(self.rb_5)
        self.rb_5.setObjectName(u"rb_5")
        self.rb_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_2.addWidget(self.rb_5, 6, 10, 1, 1)

        self.lb_GR3 = QLabel(self.tab_layout)
        self.lb_GR3.setObjectName(u"lb_GR3")
        self.lb_GR3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_GR3, 4, 5, 1, 1)

        self.lb_GR4 = QLabel(self.tab_layout)
        self.lb_GR4.setObjectName(u"lb_GR4")
        self.lb_GR4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_GR4, 5, 5, 1, 1)

        self.lb_N3_2 = QLabel(self.tab_layout)
        self.lb_N3_2.setObjectName(u"lb_N3_2")
        self.lb_N3_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_N3_2, 3, 3, 1, 1)

        self.lb_CD4 = QLabel(self.tab_layout)
        self.lb_CD4.setObjectName(u"lb_CD4")
        self.lb_CD4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_CD4, 5, 6, 1, 1)

        self.lb_width5 = QLabel(self.tab_layout)
        self.lb_width5.setObjectName(u"lb_width5")
        self.lb_width5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_width5, 6, 7, 1, 1)

        self.lb_icon5 = QLabel(self.tab_layout)
        self.lb_icon5.setObjectName(u"lb_icon5")
        self.lb_icon5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_icon5, 6, 8, 1, 1)

        self.lb_N2_1 = QLabel(self.tab_layout)
        self.lb_N2_1.setObjectName(u"lb_N2_1")
        self.lb_N2_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_N2_1, 2, 4, 1, 1)

        self.lb_N2_4 = QLabel(self.tab_layout)
        self.lb_N2_4.setObjectName(u"lb_N2_4")
        self.lb_N2_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_N2_4, 5, 4, 1, 1)

        self.lb_N2_2 = QLabel(self.tab_layout)
        self.lb_N2_2.setObjectName(u"lb_N2_2")
        self.lb_N2_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_N2_2, 3, 4, 1, 1)

        self.lb_OverallWidth = QLabel(self.tab_layout)
        self.lb_OverallWidth.setObjectName(u"lb_OverallWidth")
        self.lb_OverallWidth.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_OverallWidth.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_OverallWidth, 0, 7, 1, 1)

        self.lb_GR2 = QLabel(self.tab_layout)
        self.lb_GR2.setObjectName(u"lb_GR2")
        self.lb_GR2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_GR2, 3, 5, 1, 1)

        self.line_7 = QFrame(self.tab_layout)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 2, 9, 5, 1)

        self.lb_icon1 = QLabel(self.tab_layout)
        self.lb_icon1.setObjectName(u"lb_icon1")
        self.lb_icon1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_icon1, 2, 8, 1, 1)

        self.lb_gear = QLabel(self.tab_layout)
        self.lb_gear.setObjectName(u"lb_gear")
        self.lb_gear.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_gear, 0, 4, 1, 1)

        self.lb_CD1 = QLabel(self.tab_layout)
        self.lb_CD1.setObjectName(u"lb_CD1")
        self.lb_CD1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_CD1, 2, 6, 1, 1)

        self.lb_GR1 = QLabel(self.tab_layout)
        self.lb_GR1.setObjectName(u"lb_GR1")
        self.lb_GR1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_GR1, 2, 5, 1, 1)

        self.rb_2 = QRadioButton(self.tab_layout)
        self.bg_layout.addButton(self.rb_2)
        self.rb_2.setObjectName(u"rb_2")
        self.rb_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_2.addWidget(self.rb_2, 3, 10, 1, 1)

        self.lb_N2_3 = QLabel(self.tab_layout)
        self.lb_N2_3.setObjectName(u"lb_N2_3")
        self.lb_N2_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_N2_3, 4, 4, 1, 1)

        self.rb_1 = QRadioButton(self.tab_layout)
        self.bg_layout.addButton(self.rb_1)
        self.rb_1.setObjectName(u"rb_1")
        self.rb_1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_2.addWidget(self.rb_1, 2, 10, 1, 1)

        self.lb_icon3 = QLabel(self.tab_layout)
        self.lb_icon3.setObjectName(u"lb_icon3")
        self.lb_icon3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_icon3, 4, 8, 1, 1)

        self.lb_N2_5 = QLabel(self.tab_layout)
        self.lb_N2_5.setObjectName(u"lb_N2_5")
        self.lb_N2_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_N2_5, 6, 4, 1, 1)

        self.lb_icon2 = QLabel(self.tab_layout)
        self.lb_icon2.setObjectName(u"lb_icon2")
        self.lb_icon2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_icon2, 3, 8, 1, 1)

        self.lb_N3_1 = QLabel(self.tab_layout)
        self.lb_N3_1.setObjectName(u"lb_N3_1")
        self.lb_N3_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_N3_1, 2, 3, 1, 1)

        self.lb_pinion = QLabel(self.tab_layout)
        self.lb_pinion.setObjectName(u"lb_pinion")
        self.lb_pinion.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_pinion, 2, 0, 5, 1)

        self.line_8 = QFrame(self.tab_layout)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_8, 2, 2, 5, 1)

        self.lb_CenterDistance = QLabel(self.tab_layout)
        self.lb_CenterDistance.setObjectName(u"lb_CenterDistance")
        self.lb_CenterDistance.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_CenterDistance.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_CenterDistance, 0, 6, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_14, 4, 11, 1, 1)

        self.lb_OverallWidth_2 = QLabel(self.tab_layout)
        self.lb_OverallWidth_2.setObjectName(u"lb_OverallWidth_2")
        self.lb_OverallWidth_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_OverallWidth_2, 0, 8, 1, 1)

        self.line_6 = QFrame(self.tab_layout)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_6, 1, 2, 1, 9)


        self.vl_teeth.addLayout(self.gridLayout_2)


        self.verticalLayout_3.addLayout(self.vl_teeth)

        self.frame_planets = QFrame(self.tab_layout)
        self.frame_planets.setObjectName(u"frame_planets")
        self.verticalLayout_6 = QVBoxLayout(self.frame_planets)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(6, 0, 6, 15)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 3, -1, 6)
        self.label_4 = QLabel(self.frame_planets)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.line_18 = QFrame(self.frame_planets)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShadow(QFrame.Shadow.Raised)
        self.line_18.setLineWidth(5)
        self.line_18.setFrameShape(QFrame.Shape.HLine)

        self.horizontalLayout_4.addWidget(self.line_18)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(6)
        self.lb_p_icon3 = QLabel(self.frame_planets)
        self.lb_p_icon3.setObjectName(u"lb_p_icon3")
        self.lb_p_icon3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_p_icon3, 6, 5, 1, 1)

        self.lb_p_icon5 = QLabel(self.frame_planets)
        self.lb_p_icon5.setObjectName(u"lb_p_icon5")
        self.lb_p_icon5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_p_icon5, 8, 5, 1, 1)

        self.lb_planet1 = QLabel(self.frame_planets)
        self.lb_planet1.setObjectName(u"lb_planet1")
        self.lb_planet1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_planet1, 4, 4, 1, 1)

        self.lb_planet3 = QLabel(self.frame_planets)
        self.lb_planet3.setObjectName(u"lb_planet3")
        self.lb_planet3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_planet3, 6, 4, 1, 1)

        self.rb_p4 = QRadioButton(self.frame_planets)
        self.bg_planets = QButtonGroup(MainForm)
        self.bg_planets.setObjectName(u"bg_planets")
        self.bg_planets.addButton(self.rb_p4)
        self.rb_p4.setObjectName(u"rb_p4")
        self.rb_p4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_5.addWidget(self.rb_p4, 7, 7, 1, 1)

        self.line_13 = QFrame(self.frame_planets)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_13, 4, 6, 5, 1)

        self.le_planets = QLineEdit(self.frame_planets)
        self.le_planets.setObjectName(u"le_planets")
        sizePolicy1.setHeightForWidth(self.le_planets.sizePolicy().hasHeightForWidth())
        self.le_planets.setSizePolicy(sizePolicy1)
        self.le_planets.setMaximumSize(QSize(60, 22))
        self.le_planets.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.le_planets, 6, 2, 1, 1)

        self.lb_planet5 = QLabel(self.frame_planets)
        self.lb_planet5.setObjectName(u"lb_planet5")
        self.lb_planet5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_planet5, 8, 4, 1, 1)

        self.lb_planet4 = QLabel(self.frame_planets)
        self.lb_planet4.setObjectName(u"lb_planet4")
        self.lb_planet4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_planet4, 7, 4, 1, 1)

        self.rb_p3 = QRadioButton(self.frame_planets)
        self.bg_planets.addButton(self.rb_p3)
        self.rb_p3.setObjectName(u"rb_p3")
        self.rb_p3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.rb_p3.setChecked(True)

        self.gridLayout_5.addWidget(self.rb_p3, 6, 7, 1, 1)

        self.lb_planets = QLabel(self.frame_planets)
        self.lb_planets.setObjectName(u"lb_planets")
        self.lb_planets.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lb_planets.setWordWrap(True)

        self.gridLayout_5.addWidget(self.lb_planets, 4, 1, 5, 1)

        self.rb_p2 = QRadioButton(self.frame_planets)
        self.bg_planets.addButton(self.rb_p2)
        self.rb_p2.setObjectName(u"rb_p2")
        self.rb_p2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_5.addWidget(self.rb_p2, 5, 7, 1, 1)

        self.rb_p1 = QRadioButton(self.frame_planets)
        self.bg_planets.addButton(self.rb_p1)
        self.rb_p1.setObjectName(u"rb_p1")
        self.rb_p1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_5.addWidget(self.rb_p1, 4, 7, 1, 1)

        self.rb_p5 = QRadioButton(self.frame_planets)
        self.bg_planets.addButton(self.rb_p5)
        self.rb_p5.setObjectName(u"rb_p5")
        self.rb_p5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_5.addWidget(self.rb_p5, 8, 7, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_13, 6, 8, 1, 1)

        self.line_10 = QFrame(self.frame_planets)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_10, 4, 3, 5, 1)

        self.lb_p_icon2 = QLabel(self.frame_planets)
        self.lb_p_icon2.setObjectName(u"lb_p_icon2")
        self.lb_p_icon2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_p_icon2, 5, 5, 1, 1)

        self.lb_p_icon1 = QLabel(self.frame_planets)
        self.lb_p_icon1.setObjectName(u"lb_p_icon1")
        self.lb_p_icon1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_p_icon1, 4, 5, 1, 1)

        self.lb_planet2 = QLabel(self.frame_planets)
        self.lb_planet2.setObjectName(u"lb_planet2")
        self.lb_planet2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_planet2, 5, 4, 1, 1)

        self.lb_p_icon4 = QLabel(self.frame_planets)
        self.lb_p_icon4.setObjectName(u"lb_p_icon4")
        self.lb_p_icon4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_p_icon4, 7, 5, 1, 1)

        self.lb_even = QLabel(self.frame_planets)
        self.lb_even.setObjectName(u"lb_even")
        self.lb_even.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_even.setWordWrap(True)

        self.gridLayout_5.addWidget(self.lb_even, 2, 5, 1, 1)

        self.line_11 = QFrame(self.frame_planets)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_11, 3, 3, 1, 5)


        self.verticalLayout_6.addLayout(self.gridLayout_5)


        self.verticalLayout_3.addWidget(self.frame_planets)

        self.vl_button_helper = QVBoxLayout()
        self.vl_button_helper.setObjectName(u"vl_button_helper")
        self.vl_button_helper.setContentsMargins(6, 0, 6, 0)
        self.line_24 = QFrame(self.tab_layout)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFont(font1)
        self.line_24.setFrameShadow(QFrame.Shadow.Raised)
        self.line_24.setLineWidth(5)
        self.line_24.setFrameShape(QFrame.Shape.HLine)

        self.vl_button_helper.addWidget(self.line_24)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 6, -1, 0)
        self.pb_useLayout = QPushButton(self.tab_layout)
        self.pb_useLayout.setObjectName(u"pb_useLayout")

        self.horizontalLayout_15.addWidget(self.pb_useLayout)


        self.vl_button_helper.addLayout(self.horizontalLayout_15)


        self.verticalLayout_3.addLayout(self.vl_button_helper)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.f_helper_layout = QFrame(self.tab_layout)
        self.f_helper_layout.setObjectName(u"f_helper_layout")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(100)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.f_helper_layout.sizePolicy().hasHeightForWidth())
        self.f_helper_layout.setSizePolicy(sizePolicy3)
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
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_8 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.vl_style_GD = QVBoxLayout()
        self.vl_style_GD.setObjectName(u"vl_style_GD")
        self.vl_style_GD.setContentsMargins(6, -1, 6, 10)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 10)
        self.label_5 = QLabel(self.tab_GD)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.line_23 = QFrame(self.tab_GD)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFont(font1)
        self.line_23.setFrameShadow(QFrame.Shadow.Raised)
        self.line_23.setLineWidth(5)
        self.line_23.setFrameShape(QFrame.Shape.HLine)

        self.horizontalLayout_8.addWidget(self.line_23)


        self.vl_style_GD.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, 0, 0)
        self.cb_type_design = QComboBox(self.tab_GD)
        self.cb_type_design.addItem("")
        self.cb_type_design.addItem("")
        self.cb_type_design.addItem("")
        self.cb_type_design.setObjectName(u"cb_type_design")

        self.horizontalLayout_14.addWidget(self.cb_type_design)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)

        self.frame_pLayout_GD = QFrame(self.tab_GD)
        self.frame_pLayout_GD.setObjectName(u"frame_pLayout_GD")
        sizePolicy.setHeightForWidth(self.frame_pLayout_GD.sizePolicy().hasHeightForWidth())
        self.frame_pLayout_GD.setSizePolicy(sizePolicy)
        self.frame_pLayout_GD.setMinimumSize(QSize(0, 0))
        self.frame_pLayout_GD.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_pLayout_GD.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_pLayout_GD)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.glayout_planet_helper_2 = QGridLayout()
        self.glayout_planet_helper_2.setObjectName(u"glayout_planet_helper_2")
        self.glayout_planet_helper_2.setHorizontalSpacing(10)
        self.glayout_planet_helper_2.setVerticalSpacing(6)
        self.glayout_planet_helper_2.setContentsMargins(0, 0, 0, 0)
        self.cb_output_GD = QComboBox(self.frame_pLayout_GD)
        self.cb_output_GD.addItem("")
        self.cb_output_GD.addItem("")
        self.cb_output_GD.addItem("")
        self.cb_output_GD.setObjectName(u"cb_output_GD")
        sizePolicy1.setHeightForWidth(self.cb_output_GD.sizePolicy().hasHeightForWidth())
        self.cb_output_GD.setSizePolicy(sizePolicy1)

        self.glayout_planet_helper_2.addWidget(self.cb_output_GD, 1, 1, 1, 1)

        self.lb_input_2 = QLabel(self.frame_pLayout_GD)
        self.lb_input_2.setObjectName(u"lb_input_2")
        self.lb_input_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lb_input_2.setWordWrap(True)

        self.glayout_planet_helper_2.addWidget(self.lb_input_2, 0, 0, 1, 1)

        self.lb_stationary_2 = QLabel(self.frame_pLayout_GD)
        self.lb_stationary_2.setObjectName(u"lb_stationary_2")
        self.lb_stationary_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lb_stationary_2.setWordWrap(True)

        self.glayout_planet_helper_2.addWidget(self.lb_stationary_2, 2, 0, 1, 1)

        self.lb_stationGear2 = QLabel(self.frame_pLayout_GD)
        self.lb_stationGear2.setObjectName(u"lb_stationGear2")
        self.lb_stationGear2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.glayout_planet_helper_2.addWidget(self.lb_stationGear2, 2, 1, 1, 1)

        self.lb_output_2 = QLabel(self.frame_pLayout_GD)
        self.lb_output_2.setObjectName(u"lb_output_2")
        self.lb_output_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lb_output_2.setWordWrap(True)

        self.glayout_planet_helper_2.addWidget(self.lb_output_2, 1, 0, 1, 1)

        self.cb_input_GD = QComboBox(self.frame_pLayout_GD)
        self.cb_input_GD.addItem("")
        self.cb_input_GD.addItem("")
        self.cb_input_GD.addItem("")
        self.cb_input_GD.setObjectName(u"cb_input_GD")
        sizePolicy1.setHeightForWidth(self.cb_input_GD.sizePolicy().hasHeightForWidth())
        self.cb_input_GD.setSizePolicy(sizePolicy1)
        self.cb_input_GD.setEditable(False)

        self.glayout_planet_helper_2.addWidget(self.cb_input_GD, 0, 1, 1, 1)


        self.horizontalLayout_17.addLayout(self.glayout_planet_helper_2)


        self.horizontalLayout_14.addWidget(self.frame_pLayout_GD)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_18)


        self.vl_style_GD.addLayout(self.horizontalLayout_14)


        self.verticalLayout.addLayout(self.vl_style_GD)

        self.vl_dims = QVBoxLayout()
        self.vl_dims.setObjectName(u"vl_dims")
        self.vl_dims.setContentsMargins(6, 0, 6, 6)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 10)
        self.label_10 = QLabel(self.tab_GD)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_10)

        self.line_25 = QFrame(self.tab_GD)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFont(font1)
        self.line_25.setFrameShadow(QFrame.Shadow.Raised)
        self.line_25.setLineWidth(5)
        self.line_25.setFrameShape(QFrame.Shape.HLine)

        self.horizontalLayout_12.addWidget(self.line_25)


        self.vl_dims.addLayout(self.horizontalLayout_12)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, -1, 0)
        self.lb_Rr3 = QLabel(self.tab_GD)
        self.lb_Rr3.setObjectName(u"lb_Rr3")
        sizePolicy1.setHeightForWidth(self.lb_Rr3.sizePolicy().hasHeightForWidth())
        self.lb_Rr3.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setItalic(True)
        self.lb_Rr3.setFont(font2)
        self.lb_Rr3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rr3, 29, 3, 1, 1)

        self.le_CD_bkl1 = QLineEdit(self.tab_GD)
        self.le_CD_bkl1.setObjectName(u"le_CD_bkl1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.le_CD_bkl1.sizePolicy().hasHeightForWidth())
        self.le_CD_bkl1.setSizePolicy(sizePolicy4)
        self.le_CD_bkl1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_CD_bkl1, 8, 2, 1, 1)

        self.le_Rr2 = QLineEdit(self.tab_GD)
        self.le_Rr2.setObjectName(u"le_Rr2")
        self.le_Rr2.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.le_Rr2.sizePolicy().hasHeightForWidth())
        self.le_Rr2.setSizePolicy(sizePolicy4)
        self.le_Rr2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.le_Rr2.setReadOnly(False)

        self.gridLayout.addWidget(self.le_Rr2, 29, 4, 1, 1)

        self.le_N1 = QLineEdit(self.tab_GD)
        self.le_N1.setObjectName(u"le_N1")
        sizePolicy4.setHeightForWidth(self.le_N1.sizePolicy().hasHeightForWidth())
        self.le_N1.setSizePolicy(sizePolicy4)
        self.le_N1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_N1, 12, 2, 1, 1)

        self.le_Rtip3 = QLineEdit(self.tab_GD)
        self.le_Rtip3.setObjectName(u"le_Rtip3")
        sizePolicy4.setHeightForWidth(self.le_Rtip3.sizePolicy().hasHeightForWidth())
        self.le_Rtip3.setSizePolicy(sizePolicy4)
        self.le_Rtip3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Rtip3, 22, 3, 1, 1)

        self.lb_Romax_unit = QLabel(self.tab_GD)
        self.lb_Romax_unit.setObjectName(u"lb_Romax_unit")
        sizePolicy1.setHeightForWidth(self.lb_Romax_unit.sizePolicy().hasHeightForWidth())
        self.lb_Romax_unit.setSizePolicy(sizePolicy1)
        self.lb_Romax_unit.setFont(font2)
        self.lb_Romax_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_Romax_unit, 21, 1, 1, 1)

        self.lb_Romax2 = QLabel(self.tab_GD)
        self.lb_Romax2.setObjectName(u"lb_Romax2")
        sizePolicy1.setHeightForWidth(self.lb_Romax2.sizePolicy().hasHeightForWidth())
        self.lb_Romax2.setSizePolicy(sizePolicy1)
        self.lb_Romax2.setFont(font2)
        self.lb_Romax2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Romax2, 21, 4, 1, 1)

        self.le_Ro2 = QLineEdit(self.tab_GD)
        self.le_Ro2.setObjectName(u"le_Ro2")
        sizePolicy4.setHeightForWidth(self.le_Ro2.sizePolicy().hasHeightForWidth())
        self.le_Ro2.setSizePolicy(sizePolicy4)
        self.le_Ro2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Ro2, 19, 4, 1, 1)

        self.le_bkl2 = QLineEdit(self.tab_GD)
        self.le_bkl2.setObjectName(u"le_bkl2")
        sizePolicy4.setHeightForWidth(self.le_bkl2.sizePolicy().hasHeightForWidth())
        self.le_bkl2.setSizePolicy(sizePolicy4)
        self.le_bkl2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_bkl2, 9, 2, 1, 1)

        self.le_Rf3 = QLineEdit(self.tab_GD)
        self.le_Rf3.setObjectName(u"le_Rf3")
        sizePolicy4.setHeightForWidth(self.le_Rf3.sizePolicy().hasHeightForWidth())
        self.le_Rf3.setSizePolicy(sizePolicy4)
        self.le_Rf3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Rf3, 31, 3, 1, 1)

        self.lb_Roe2 = QLabel(self.tab_GD)
        self.lb_Roe2.setObjectName(u"lb_Roe2")
        sizePolicy1.setHeightForWidth(self.lb_Roe2.sizePolicy().hasHeightForWidth())
        self.lb_Roe2.setSizePolicy(sizePolicy1)
        self.lb_Roe2.setFont(font2)
        self.lb_Roe2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Roe2, 24, 4, 1, 1)

        self.label_47 = QLabel(self.tab_GD)
        self.label_47.setObjectName(u"label_47")
        sizePolicy1.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy1)
        self.label_47.setFont(font2)
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_47, 17, 0, 1, 1)

        self.lb_Rp_unit = QLabel(self.tab_GD)
        self.lb_Rp_unit.setObjectName(u"lb_Rp_unit")
        sizePolicy1.setHeightForWidth(self.lb_Rp_unit.sizePolicy().hasHeightForWidth())
        self.lb_Rp_unit.setSizePolicy(sizePolicy1)
        self.lb_Rp_unit.setFont(font2)
        self.lb_Rp_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_Rp_unit, 15, 1, 1, 1)

        self.lb_Rtipmax_unit = QLabel(self.tab_GD)
        self.lb_Rtipmax_unit.setObjectName(u"lb_Rtipmax_unit")
        sizePolicy1.setHeightForWidth(self.lb_Rtipmax_unit.sizePolicy().hasHeightForWidth())
        self.lb_Rtipmax_unit.setSizePolicy(sizePolicy1)
        self.lb_Rtipmax_unit.setFont(font2)
        self.lb_Rtipmax_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_Rtipmax_unit, 23, 1, 1, 1)

        self.label_50 = QLabel(self.tab_GD)
        self.label_50.setObjectName(u"label_50")
        sizePolicy1.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy1)
        self.label_50.setFont(font2)
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_50, 15, 0, 1, 1)

        self.lb_tt_unit = QLabel(self.tab_GD)
        self.lb_tt_unit.setObjectName(u"lb_tt_unit")
        sizePolicy1.setHeightForWidth(self.lb_tt_unit.sizePolicy().hasHeightForWidth())
        self.lb_tt_unit.setSizePolicy(sizePolicy1)
        self.lb_tt_unit.setFont(font2)
        self.lb_tt_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_tt_unit, 17, 1, 1, 1)

        self.le_Rf1 = QLineEdit(self.tab_GD)
        self.le_Rf1.setObjectName(u"le_Rf1")
        sizePolicy4.setHeightForWidth(self.le_Rf1.sizePolicy().hasHeightForWidth())
        self.le_Rf1.setSizePolicy(sizePolicy4)
        self.le_Rf1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Rf1, 31, 2, 1, 1)

        self.lb_Rr_unit = QLabel(self.tab_GD)
        self.lb_Rr_unit.setObjectName(u"lb_Rr_unit")
        sizePolicy1.setHeightForWidth(self.lb_Rr_unit.sizePolicy().hasHeightForWidth())
        self.lb_Rr_unit.setSizePolicy(sizePolicy1)
        self.lb_Rr_unit.setFont(font2)
        self.lb_Rr_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_Rr_unit, 29, 1, 1, 1)

        self.le_Ro3 = QLineEdit(self.tab_GD)
        self.le_Ro3.setObjectName(u"le_Ro3")
        sizePolicy4.setHeightForWidth(self.le_Ro3.sizePolicy().hasHeightForWidth())
        self.le_Ro3.setSizePolicy(sizePolicy4)
        self.le_Ro3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Ro3, 19, 3, 1, 1)

        self.label_66 = QLabel(self.tab_GD)
        self.label_66.setObjectName(u"label_66")
        sizePolicy1.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy1)
        self.label_66.setFont(font2)
        self.label_66.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_66, 28, 0, 1, 1)

        self.lb_CR2 = QLabel(self.tab_GD)
        self.lb_CR2.setObjectName(u"lb_CR2")
        sizePolicy1.setHeightForWidth(self.lb_CR2.sizePolicy().hasHeightForWidth())
        self.lb_CR2.setSizePolicy(sizePolicy1)
        self.lb_CR2.setFont(font2)
        self.lb_CR2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_CR2, 37, 4, 1, 1)

        self.label_55 = QLabel(self.tab_GD)
        self.label_55.setObjectName(u"label_55")
        sizePolicy1.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy1)
        self.label_55.setFont(font2)
        self.label_55.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_55, 13, 1, 1, 1)

        self.lb_N3 = QLabel(self.tab_GD)
        self.lb_N3.setObjectName(u"lb_N3")
        sizePolicy1.setHeightForWidth(self.lb_N3.sizePolicy().hasHeightForWidth())
        self.lb_N3.setSizePolicy(sizePolicy1)
        self.lb_N3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_N3, 12, 3, 1, 1)

        self.lb_Roe3 = QLabel(self.tab_GD)
        self.lb_Roe3.setObjectName(u"lb_Roe3")
        sizePolicy1.setHeightForWidth(self.lb_Roe3.sizePolicy().hasHeightForWidth())
        self.lb_Roe3.setSizePolicy(sizePolicy1)
        self.lb_Roe3.setFont(font2)
        self.lb_Roe3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Roe3, 24, 3, 1, 1)

        self.lb_Ro_unit = QLabel(self.tab_GD)
        self.lb_Ro_unit.setObjectName(u"lb_Ro_unit")
        sizePolicy1.setHeightForWidth(self.lb_Ro_unit.sizePolicy().hasHeightForWidth())
        self.lb_Ro_unit.setSizePolicy(sizePolicy1)
        self.lb_Ro_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_Ro_unit, 19, 1, 1, 1)

        self.lb_Roe1 = QLabel(self.tab_GD)
        self.lb_Roe1.setObjectName(u"lb_Roe1")
        sizePolicy1.setHeightForWidth(self.lb_Roe1.sizePolicy().hasHeightForWidth())
        self.lb_Roe1.setSizePolicy(sizePolicy1)
        self.lb_Roe1.setFont(font2)
        self.lb_Roe1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Roe1, 24, 2, 1, 1)

        self.label_22 = QLabel(self.tab_GD)
        self.label_22.setObjectName(u"label_22")
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_22, 12, 0, 1, 1)

        self.lb_Romax3 = QLabel(self.tab_GD)
        self.lb_Romax3.setObjectName(u"lb_Romax3")
        sizePolicy1.setHeightForWidth(self.lb_Romax3.sizePolicy().hasHeightForWidth())
        self.lb_Romax3.setSizePolicy(sizePolicy1)
        self.lb_Romax3.setFont(font2)
        self.lb_Romax3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Romax3, 21, 3, 1, 1)

        self.lb_Rf_unit = QLabel(self.tab_GD)
        self.lb_Rf_unit.setObjectName(u"lb_Rf_unit")
        sizePolicy1.setHeightForWidth(self.lb_Rf_unit.sizePolicy().hasHeightForWidth())
        self.lb_Rf_unit.setSizePolicy(sizePolicy1)
        self.lb_Rf_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_Rf_unit, 31, 1, 1, 1)

        self.lb_Rrs1 = QLabel(self.tab_GD)
        self.lb_Rrs1.setObjectName(u"lb_Rrs1")
        sizePolicy1.setHeightForWidth(self.lb_Rrs1.sizePolicy().hasHeightForWidth())
        self.lb_Rrs1.setSizePolicy(sizePolicy1)
        self.lb_Rrs1.setFont(font2)
        self.lb_Rrs1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rrs1, 28, 2, 1, 1)

        self.le_Rf2 = QLineEdit(self.tab_GD)
        self.le_Rf2.setObjectName(u"le_Rf2")
        sizePolicy4.setHeightForWidth(self.le_Rf2.sizePolicy().hasHeightForWidth())
        self.le_Rf2.setSizePolicy(sizePolicy4)
        self.le_Rf2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Rf2, 31, 4, 1, 1)

        self.lb_Rrs2 = QLabel(self.tab_GD)
        self.lb_Rrs2.setObjectName(u"lb_Rrs2")
        sizePolicy1.setHeightForWidth(self.lb_Rrs2.sizePolicy().hasHeightForWidth())
        self.lb_Rrs2.setSizePolicy(sizePolicy1)
        self.lb_Rrs2.setFont(font2)
        self.lb_Rrs2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rrs2, 28, 4, 1, 1)

        self.lb_Rff1 = QLabel(self.tab_GD)
        self.lb_Rff1.setObjectName(u"lb_Rff1")
        sizePolicy1.setHeightForWidth(self.lb_Rff1.sizePolicy().hasHeightForWidth())
        self.lb_Rff1.setSizePolicy(sizePolicy1)
        self.lb_Rff1.setFont(font2)
        self.lb_Rff1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rff1, 32, 2, 1, 1)

        self.label_20 = QLabel(self.tab_GD)
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_20, 6, 0, 1, 1)

        self.le_NPlanets = QLineEdit(self.tab_GD)
        self.le_NPlanets.setObjectName(u"le_NPlanets")
        sizePolicy4.setHeightForWidth(self.le_NPlanets.sizePolicy().hasHeightForWidth())
        self.le_NPlanets.setSizePolicy(sizePolicy4)
        self.le_NPlanets.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_NPlanets, 6, 4, 1, 1)

        self.lb_Rf = QLabel(self.tab_GD)
        self.lb_Rf.setObjectName(u"lb_Rf")
        sizePolicy1.setHeightForWidth(self.lb_Rf.sizePolicy().hasHeightForWidth())
        self.lb_Rf.setSizePolicy(sizePolicy1)
        self.lb_Rf.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rf, 31, 0, 1, 1)

        self.le_Rtip2 = QLineEdit(self.tab_GD)
        self.le_Rtip2.setObjectName(u"le_Rtip2")
        sizePolicy4.setHeightForWidth(self.le_Rtip2.sizePolicy().hasHeightForWidth())
        self.le_Rtip2.setSizePolicy(sizePolicy4)
        self.le_Rtip2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Rtip2, 22, 4, 1, 1)

        self.lb_GR = QLabel(self.tab_GD)
        self.lb_GR.setObjectName(u"lb_GR")
        sizePolicy1.setHeightForWidth(self.lb_GR.sizePolicy().hasHeightForWidth())
        self.lb_GR.setSizePolicy(sizePolicy1)
        self.lb_GR.setFont(font2)
        self.lb_GR.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_GR, 34, 2, 1, 1)

        self.label_60 = QLabel(self.tab_GD)
        self.label_60.setObjectName(u"label_60")
        sizePolicy1.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy1)
        self.label_60.setFont(font2)
        self.label_60.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_60, 34, 1, 1, 1)

        self.le_Rrim = QLineEdit(self.tab_GD)
        self.le_Rrim.setObjectName(u"le_Rrim")
        sizePolicy4.setHeightForWidth(self.le_Rrim.sizePolicy().hasHeightForWidth())
        self.le_Rrim.setSizePolicy(sizePolicy4)
        self.le_Rrim.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Rrim, 25, 4, 1, 1)

        self.lb_tt3 = QLabel(self.tab_GD)
        self.lb_tt3.setObjectName(u"lb_tt3")
        sizePolicy1.setHeightForWidth(self.lb_tt3.sizePolicy().hasHeightForWidth())
        self.lb_tt3.setSizePolicy(sizePolicy1)
        self.lb_tt3.setFont(font2)
        self.lb_tt3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_tt3, 17, 3, 1, 1)

        self.lb_CD_text = QLabel(self.tab_GD)
        self.lb_CD_text.setObjectName(u"lb_CD_text")
        sizePolicy1.setHeightForWidth(self.lb_CD_text.sizePolicy().hasHeightForWidth())
        self.lb_CD_text.setSizePolicy(sizePolicy1)
        self.lb_CD_text.setFont(font2)
        self.lb_CD_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_CD_text, 35, 0, 1, 1)

        self.lb_max_planets_text = QLabel(self.tab_GD)
        self.lb_max_planets_text.setObjectName(u"lb_max_planets_text")
        sizePolicy1.setHeightForWidth(self.lb_max_planets_text.sizePolicy().hasHeightForWidth())
        self.lb_max_planets_text.setSizePolicy(sizePolicy1)
        self.lb_max_planets_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_max_planets_text, 7, 3, 1, 1)

        self.le_N2 = QLineEdit(self.tab_GD)
        self.le_N2.setObjectName(u"le_N2")
        sizePolicy4.setHeightForWidth(self.le_N2.sizePolicy().hasHeightForWidth())
        self.le_N2.setSizePolicy(sizePolicy4)
        self.le_N2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_N2, 12, 4, 1, 1)

        self.line_2 = QFrame(self.tab_GD)
        self.line_2.setObjectName(u"line_2")
        sizePolicy4.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy4)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 26, 0, 1, 6)

        self.label_6 = QLabel(self.tab_GD)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 12, 1, 1, 1)

        self.lb_Rrs3 = QLabel(self.tab_GD)
        self.lb_Rrs3.setObjectName(u"lb_Rrs3")
        sizePolicy1.setHeightForWidth(self.lb_Rrs3.sizePolicy().hasHeightForWidth())
        self.lb_Rrs3.setSizePolicy(sizePolicy1)
        self.lb_Rrs3.setFont(font2)
        self.lb_Rrs3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rrs3, 28, 3, 1, 1)

        self.lb_Rtipmax2 = QLabel(self.tab_GD)
        self.lb_Rtipmax2.setObjectName(u"lb_Rtipmax2")
        sizePolicy1.setHeightForWidth(self.lb_Rtipmax2.sizePolicy().hasHeightForWidth())
        self.lb_Rtipmax2.setSizePolicy(sizePolicy1)
        self.lb_Rtipmax2.setFont(font2)
        self.lb_Rtipmax2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rtipmax2, 23, 4, 1, 1)

        self.le_rtcl3 = QLineEdit(self.tab_GD)
        self.le_rtcl3.setObjectName(u"le_rtcl3")
        sizePolicy4.setHeightForWidth(self.le_rtcl3.sizePolicy().hasHeightForWidth())
        self.le_rtcl3.setSizePolicy(sizePolicy4)
        self.le_rtcl3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_rtcl3, 27, 3, 1, 1)

        self.label_14 = QLabel(self.tab_GD)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_14, 23, 0, 1, 1)

        self.lb_Rtipmax3 = QLabel(self.tab_GD)
        self.lb_Rtipmax3.setObjectName(u"lb_Rtipmax3")
        sizePolicy1.setHeightForWidth(self.lb_Rtipmax3.sizePolicy().hasHeightForWidth())
        self.lb_Rtipmax3.setSizePolicy(sizePolicy1)
        self.lb_Rtipmax3.setFont(font2)
        self.lb_Rtipmax3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rtipmax3, 23, 3, 1, 1)

        self.lb_CD_unit = QLabel(self.tab_GD)
        self.lb_CD_unit.setObjectName(u"lb_CD_unit")
        sizePolicy1.setHeightForWidth(self.lb_CD_unit.sizePolicy().hasHeightForWidth())
        self.lb_CD_unit.setSizePolicy(sizePolicy1)
        self.lb_CD_unit.setFont(font2)
        self.lb_CD_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_CD_unit, 35, 1, 1, 1)

        self.lb_tts3 = QLabel(self.tab_GD)
        self.lb_tts3.setObjectName(u"lb_tts3")
        sizePolicy1.setHeightForWidth(self.lb_tts3.sizePolicy().hasHeightForWidth())
        self.lb_tts3.setSizePolicy(sizePolicy1)
        self.lb_tts3.setFont(font2)
        self.lb_tts3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_tts3, 16, 3, 1, 1)

        self.lb_NPlanets_text = QLabel(self.tab_GD)
        self.lb_NPlanets_text.setObjectName(u"lb_NPlanets_text")
        sizePolicy1.setHeightForWidth(self.lb_NPlanets_text.sizePolicy().hasHeightForWidth())
        self.lb_NPlanets_text.setSizePolicy(sizePolicy1)
        self.lb_NPlanets_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_NPlanets_text, 6, 3, 1, 1)

        self.line_3 = QFrame(self.tab_GD)
        self.line_3.setObjectName(u"line_3")
        sizePolicy4.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy4)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 33, 0, 1, 6)

        self.le_x3 = QLineEdit(self.tab_GD)
        self.le_x3.setObjectName(u"le_x3")
        sizePolicy4.setHeightForWidth(self.le_x3.sizePolicy().hasHeightForWidth())
        self.le_x3.setSizePolicy(sizePolicy4)
        self.le_x3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_x3, 13, 3, 1, 1)

        self.lb_Rff3 = QLabel(self.tab_GD)
        self.lb_Rff3.setObjectName(u"lb_Rff3")
        sizePolicy1.setHeightForWidth(self.lb_Rff3.sizePolicy().hasHeightForWidth())
        self.lb_Rff3.setSizePolicy(sizePolicy1)
        self.lb_Rff3.setFont(font2)
        self.lb_Rff3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rff3, 32, 3, 1, 1)

        self.lb_Ros3 = QLabel(self.tab_GD)
        self.lb_Ros3.setObjectName(u"lb_Ros3")
        sizePolicy1.setHeightForWidth(self.lb_Ros3.sizePolicy().hasHeightForWidth())
        self.lb_Ros3.setSizePolicy(sizePolicy1)
        self.lb_Ros3.setFont(font2)
        self.lb_Ros3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Ros3, 20, 3, 1, 1)

        self.lb_undercut3 = QLabel(self.tab_GD)
        self.lb_undercut3.setObjectName(u"lb_undercut3")
        sizePolicy1.setHeightForWidth(self.lb_undercut3.sizePolicy().hasHeightForWidth())
        self.lb_undercut3.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setBold(False)
        font3.setItalic(True)
        self.lb_undercut3.setFont(font3)
        self.lb_undercut3.setTextFormat(Qt.TextFormat.AutoText)
        self.lb_undercut3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_undercut3, 38, 3, 1, 1)

        self.le_rtcl2 = QLineEdit(self.tab_GD)
        self.le_rtcl2.setObjectName(u"le_rtcl2")
        sizePolicy4.setHeightForWidth(self.le_rtcl2.sizePolicy().hasHeightForWidth())
        self.le_rtcl2.setSizePolicy(sizePolicy4)
        self.le_rtcl2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_rtcl2, 27, 4, 1, 1)

        self.lb_tts2 = QLabel(self.tab_GD)
        self.lb_tts2.setObjectName(u"lb_tts2")
        sizePolicy1.setHeightForWidth(self.lb_tts2.sizePolicy().hasHeightForWidth())
        self.lb_tts2.setSizePolicy(sizePolicy1)
        self.lb_tts2.setFont(font2)
        self.lb_tts2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_tts2, 16, 4, 1, 1)

        self.label_59 = QLabel(self.tab_GD)
        self.label_59.setObjectName(u"label_59")
        sizePolicy1.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy1)
        self.label_59.setFont(font2)
        self.label_59.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_59, 37, 1, 1, 1)

        self.lb_tt1 = QLabel(self.tab_GD)
        self.lb_tt1.setObjectName(u"lb_tt1")
        sizePolicy1.setHeightForWidth(self.lb_tt1.sizePolicy().hasHeightForWidth())
        self.lb_tt1.setSizePolicy(sizePolicy1)
        self.lb_tt1.setFont(font2)
        self.lb_tt1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_tt1, 17, 2, 1, 1)

        self.label_13 = QLabel(self.tab_GD)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_13, 21, 0, 1, 1)

        self.lb_Rrs_unit = QLabel(self.tab_GD)
        self.lb_Rrs_unit.setObjectName(u"lb_Rrs_unit")
        sizePolicy1.setHeightForWidth(self.lb_Rrs_unit.sizePolicy().hasHeightForWidth())
        self.lb_Rrs_unit.setSizePolicy(sizePolicy1)
        self.lb_Rrs_unit.setFont(font2)
        self.lb_Rrs_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_Rrs_unit, 28, 1, 1, 1)

        self.lb_rtcl_unit = QLabel(self.tab_GD)
        self.lb_rtcl_unit.setObjectName(u"lb_rtcl_unit")
        sizePolicy1.setHeightForWidth(self.lb_rtcl_unit.sizePolicy().hasHeightForWidth())
        self.lb_rtcl_unit.setSizePolicy(sizePolicy1)
        self.lb_rtcl_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_rtcl_unit, 27, 1, 1, 1)

        self.lb_bkl_unit = QLabel(self.tab_GD)
        self.lb_bkl_unit.setObjectName(u"lb_bkl_unit")
        sizePolicy1.setHeightForWidth(self.lb_bkl_unit.sizePolicy().hasHeightForWidth())
        self.lb_bkl_unit.setSizePolicy(sizePolicy1)
        self.lb_bkl_unit.setFont(font2)
        self.lb_bkl_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_bkl_unit, 36, 1, 1, 1)

        self.lb_undercut2 = QLabel(self.tab_GD)
        self.lb_undercut2.setObjectName(u"lb_undercut2")
        sizePolicy1.setHeightForWidth(self.lb_undercut2.sizePolicy().hasHeightForWidth())
        self.lb_undercut2.setSizePolicy(sizePolicy1)
        self.lb_undercut2.setFont(font3)
        self.lb_undercut2.setTextFormat(Qt.TextFormat.AutoText)
        self.lb_undercut2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_undercut2, 38, 4, 1, 1)

        self.label_16 = QLabel(self.tab_GD)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_16, 27, 0, 1, 1)

        self.line_1 = QFrame(self.tab_GD)
        self.line_1.setObjectName(u"line_1")
        sizePolicy4.setHeightForWidth(self.line_1.sizePolicy().hasHeightForWidth())
        self.line_1.setSizePolicy(sizePolicy4)
        self.line_1.setFrameShape(QFrame.Shape.HLine)
        self.line_1.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_1, 18, 0, 1, 6)

        self.label_29 = QLabel(self.tab_GD)
        self.label_29.setObjectName(u"label_29")
        sizePolicy1.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy1)
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_29, 7, 1, 1, 1)

        self.lb_CD_bkl_unit = QLabel(self.tab_GD)
        self.lb_CD_bkl_unit.setObjectName(u"lb_CD_bkl_unit")
        sizePolicy1.setHeightForWidth(self.lb_CD_bkl_unit.sizePolicy().hasHeightForWidth())
        self.lb_CD_bkl_unit.setSizePolicy(sizePolicy1)
        self.lb_CD_bkl_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_CD_bkl_unit, 8, 1, 1, 1)

        self.lb_Rs3 = QLabel(self.tab_GD)
        self.lb_Rs3.setObjectName(u"lb_Rs3")
        sizePolicy1.setHeightForWidth(self.lb_Rs3.sizePolicy().hasHeightForWidth())
        self.lb_Rs3.setSizePolicy(sizePolicy1)
        self.lb_Rs3.setFont(font2)
        self.lb_Rs3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rs3, 14, 3, 1, 1)

        self.lb_max_planets = QLabel(self.tab_GD)
        self.lb_max_planets.setObjectName(u"lb_max_planets")
        sizePolicy1.setHeightForWidth(self.lb_max_planets.sizePolicy().hasHeightForWidth())
        self.lb_max_planets.setSizePolicy(sizePolicy1)
        self.lb_max_planets.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_max_planets, 7, 4, 1, 1)

        self.lb_mod_unit = QLabel(self.tab_GD)
        self.lb_mod_unit.setObjectName(u"lb_mod_unit")
        sizePolicy1.setHeightForWidth(self.lb_mod_unit.sizePolicy().hasHeightForWidth())
        self.lb_mod_unit.setSizePolicy(sizePolicy1)
        self.lb_mod_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_mod_unit, 6, 1, 1, 1)

        self.lb_CD_value = QLabel(self.tab_GD)
        self.lb_CD_value.setObjectName(u"lb_CD_value")
        self.lb_CD_value.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lb_CD_value.sizePolicy().hasHeightForWidth())
        self.lb_CD_value.setSizePolicy(sizePolicy1)
        self.lb_CD_value.setFont(font2)
        self.lb_CD_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_CD_value, 35, 2, 1, 1)

        self.le_Ro1 = QLineEdit(self.tab_GD)
        self.le_Ro1.setObjectName(u"le_Ro1")
        sizePolicy4.setHeightForWidth(self.le_Ro1.sizePolicy().hasHeightForWidth())
        self.le_Ro1.setSizePolicy(sizePolicy4)
        self.le_Ro1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Ro1, 19, 2, 1, 1)

        self.le_PA_deg = QLineEdit(self.tab_GD)
        self.le_PA_deg.setObjectName(u"le_PA_deg")
        sizePolicy4.setHeightForWidth(self.le_PA_deg.sizePolicy().hasHeightForWidth())
        self.le_PA_deg.setSizePolicy(sizePolicy4)
        self.le_PA_deg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_PA_deg, 7, 2, 1, 1)

        self.label_24 = QLabel(self.tab_GD)
        self.label_24.setObjectName(u"label_24")
        sizePolicy1.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setBold(True)
        self.label_24.setFont(font4)
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_24, 4, 2, 1, 1)

        self.lb_Rs1 = QLabel(self.tab_GD)
        self.lb_Rs1.setObjectName(u"lb_Rs1")
        sizePolicy1.setHeightForWidth(self.lb_Rs1.sizePolicy().hasHeightForWidth())
        self.lb_Rs1.setSizePolicy(sizePolicy1)
        self.lb_Rs1.setFont(font2)
        self.lb_Rs1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rs1, 14, 2, 1, 1)

        self.lb_Rtipmax1 = QLabel(self.tab_GD)
        self.lb_Rtipmax1.setObjectName(u"lb_Rtipmax1")
        sizePolicy1.setHeightForWidth(self.lb_Rtipmax1.sizePolicy().hasHeightForWidth())
        self.lb_Rtipmax1.setSizePolicy(sizePolicy1)
        self.lb_Rtipmax1.setFont(font2)
        self.lb_Rtipmax1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rtipmax1, 23, 2, 1, 1)

        self.lb_tts1 = QLabel(self.tab_GD)
        self.lb_tts1.setObjectName(u"lb_tts1")
        sizePolicy1.setHeightForWidth(self.lb_tts1.sizePolicy().hasHeightForWidth())
        self.lb_tts1.setSizePolicy(sizePolicy1)
        self.lb_tts1.setFont(font2)
        self.lb_tts1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_tts1, 16, 2, 1, 1)

        self.label_32 = QLabel(self.tab_GD)
        self.label_32.setObjectName(u"label_32")
        sizePolicy1.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy1)
        self.label_32.setFont(font2)
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_32, 20, 0, 1, 1)

        self.lb_Romax1 = QLabel(self.tab_GD)
        self.lb_Romax1.setObjectName(u"lb_Romax1")
        sizePolicy1.setHeightForWidth(self.lb_Romax1.sizePolicy().hasHeightForWidth())
        self.lb_Romax1.setSizePolicy(sizePolicy1)
        self.lb_Romax1.setFont(font2)
        self.lb_Romax1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Romax1, 21, 2, 1, 1)

        self.label_12 = QLabel(self.tab_GD)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_12, 13, 0, 1, 1)

        self.lb_Rrim_unit = QLabel(self.tab_GD)
        self.lb_Rrim_unit.setObjectName(u"lb_Rrim_unit")
        self.lb_Rrim_unit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lb_Rrim_unit.sizePolicy().hasHeightForWidth())
        self.lb_Rrim_unit.setSizePolicy(sizePolicy1)
        self.lb_Rrim_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_Rrim_unit, 25, 1, 1, 1)

        self.lb_Roe_unit = QLabel(self.tab_GD)
        self.lb_Roe_unit.setObjectName(u"lb_Roe_unit")
        sizePolicy1.setHeightForWidth(self.lb_Roe_unit.sizePolicy().hasHeightForWidth())
        self.lb_Roe_unit.setSizePolicy(sizePolicy1)
        self.lb_Roe_unit.setFont(font2)
        self.lb_Roe_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_Roe_unit, 24, 1, 1, 1)

        self.lb_CR1 = QLabel(self.tab_GD)
        self.lb_CR1.setObjectName(u"lb_CR1")
        sizePolicy1.setHeightForWidth(self.lb_CR1.sizePolicy().hasHeightForWidth())
        self.lb_CR1.setSizePolicy(sizePolicy1)
        self.lb_CR1.setFont(font2)
        self.lb_CR1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_CR1, 37, 2, 1, 1)

        self.cb_CD_bkl = QComboBox(self.tab_GD)
        self.cb_CD_bkl.addItem("")
        self.cb_CD_bkl.addItem("")
        self.cb_CD_bkl.setObjectName(u"cb_CD_bkl")
        self.cb_CD_bkl.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout.addWidget(self.cb_CD_bkl, 8, 0, 1, 1)

        self.label_40 = QLabel(self.tab_GD)
        self.label_40.setObjectName(u"label_40")
        sizePolicy1.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy1)
        self.label_40.setFont(font2)
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_40, 32, 0, 1, 1)

        self.lb_G2 = QLabel(self.tab_GD)
        self.lb_G2.setObjectName(u"lb_G2")
        sizePolicy1.setHeightForWidth(self.lb_G2.sizePolicy().hasHeightForWidth())
        self.lb_G2.setSizePolicy(sizePolicy1)
        self.lb_G2.setFont(font4)
        self.lb_G2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_G2, 10, 4, 1, 1)

        self.lb_Rs_unit = QLabel(self.tab_GD)
        self.lb_Rs_unit.setObjectName(u"lb_Rs_unit")
        sizePolicy1.setHeightForWidth(self.lb_Rs_unit.sizePolicy().hasHeightForWidth())
        self.lb_Rs_unit.setSizePolicy(sizePolicy1)
        self.lb_Rs_unit.setFont(font2)
        self.lb_Rs_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_Rs_unit, 14, 1, 1, 1)

        self.lb_G3 = QLabel(self.tab_GD)
        self.lb_G3.setObjectName(u"lb_G3")
        sizePolicy1.setHeightForWidth(self.lb_G3.sizePolicy().hasHeightForWidth())
        self.lb_G3.setSizePolicy(sizePolicy1)
        self.lb_G3.setFont(font4)
        self.lb_G3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_G3, 10, 3, 1, 1)

        self.lb_Rff_unit = QLabel(self.tab_GD)
        self.lb_Rff_unit.setObjectName(u"lb_Rff_unit")
        sizePolicy1.setHeightForWidth(self.lb_Rff_unit.sizePolicy().hasHeightForWidth())
        self.lb_Rff_unit.setSizePolicy(sizePolicy1)
        self.lb_Rff_unit.setFont(font2)
        self.lb_Rff_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_Rff_unit, 32, 1, 1, 1)

        self.lb_Rr1 = QLabel(self.tab_GD)
        self.lb_Rr1.setObjectName(u"lb_Rr1")
        sizePolicy1.setHeightForWidth(self.lb_Rr1.sizePolicy().hasHeightForWidth())
        self.lb_Rr1.setSizePolicy(sizePolicy1)
        self.lb_Rr1.setFont(font2)
        self.lb_Rr1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rr1, 29, 2, 1, 1)

        self.lb_Rff2 = QLabel(self.tab_GD)
        self.lb_Rff2.setObjectName(u"lb_Rff2")
        sizePolicy1.setHeightForWidth(self.lb_Rff2.sizePolicy().hasHeightForWidth())
        self.lb_Rff2.setSizePolicy(sizePolicy1)
        self.lb_Rff2.setFont(font2)
        self.lb_Rff2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rff2, 32, 4, 1, 1)

        self.lb_bkl_value = QLabel(self.tab_GD)
        self.lb_bkl_value.setObjectName(u"lb_bkl_value")
        self.lb_bkl_value.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lb_bkl_value.sizePolicy().hasHeightForWidth())
        self.lb_bkl_value.setSizePolicy(sizePolicy1)
        self.lb_bkl_value.setFont(font2)
        self.lb_bkl_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_bkl_value, 36, 2, 1, 1)

        self.lb_Rrim_text = QLabel(self.tab_GD)
        self.lb_Rrim_text.setObjectName(u"lb_Rrim_text")
        self.lb_Rrim_text.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lb_Rrim_text.sizePolicy().hasHeightForWidth())
        self.lb_Rrim_text.setSizePolicy(sizePolicy1)
        self.lb_Rrim_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rrim_text, 25, 0, 1, 1)

        self.lb_Ros1 = QLabel(self.tab_GD)
        self.lb_Ros1.setObjectName(u"lb_Ros1")
        sizePolicy1.setHeightForWidth(self.lb_Ros1.sizePolicy().hasHeightForWidth())
        self.lb_Ros1.setSizePolicy(sizePolicy1)
        self.lb_Ros1.setFont(font2)
        self.lb_Ros1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Ros1, 20, 2, 1, 1)

        self.lb_Rp1 = QLabel(self.tab_GD)
        self.lb_Rp1.setObjectName(u"lb_Rp1")
        sizePolicy1.setHeightForWidth(self.lb_Rp1.sizePolicy().hasHeightForWidth())
        self.lb_Rp1.setSizePolicy(sizePolicy1)
        self.lb_Rp1.setFont(font2)
        self.lb_Rp1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rp1, 15, 2, 1, 1)

        self.lb_undercut1 = QLabel(self.tab_GD)
        self.lb_undercut1.setObjectName(u"lb_undercut1")
        sizePolicy1.setHeightForWidth(self.lb_undercut1.sizePolicy().hasHeightForWidth())
        self.lb_undercut1.setSizePolicy(sizePolicy1)
        self.lb_undercut1.setFont(font3)
        self.lb_undercut1.setTextFormat(Qt.TextFormat.AutoText)
        self.lb_undercut1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_undercut1, 38, 2, 1, 1)

        self.lb_Rs2 = QLabel(self.tab_GD)
        self.lb_Rs2.setObjectName(u"lb_Rs2")
        sizePolicy1.setHeightForWidth(self.lb_Rs2.sizePolicy().hasHeightForWidth())
        self.lb_Rs2.setSizePolicy(sizePolicy1)
        self.lb_Rs2.setFont(font2)
        self.lb_Rs2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rs2, 14, 4, 1, 1)

        self.label_46 = QLabel(self.tab_GD)
        self.label_46.setObjectName(u"label_46")
        sizePolicy1.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy1)
        self.label_46.setFont(font2)
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_46, 29, 0, 1, 1)

        self.label_18 = QLabel(self.tab_GD)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_18, 7, 0, 1, 1)

        self.lb_bkl2_text = QLabel(self.tab_GD)
        self.lb_bkl2_text.setObjectName(u"lb_bkl2_text")
        sizePolicy1.setHeightForWidth(self.lb_bkl2_text.sizePolicy().hasHeightForWidth())
        self.lb_bkl2_text.setSizePolicy(sizePolicy1)
        self.lb_bkl2_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_bkl2_text, 9, 0, 1, 1)

        self.lb_bkl2_unit = QLabel(self.tab_GD)
        self.lb_bkl2_unit.setObjectName(u"lb_bkl2_unit")
        sizePolicy1.setHeightForWidth(self.lb_bkl2_unit.sizePolicy().hasHeightForWidth())
        self.lb_bkl2_unit.setSizePolicy(sizePolicy1)
        self.lb_bkl2_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_bkl2_unit, 9, 1, 1, 1)

        self.lb_Ros_unit = QLabel(self.tab_GD)
        self.lb_Ros_unit.setObjectName(u"lb_Ros_unit")
        sizePolicy1.setHeightForWidth(self.lb_Ros_unit.sizePolicy().hasHeightForWidth())
        self.lb_Ros_unit.setSizePolicy(sizePolicy1)
        self.lb_Ros_unit.setFont(font2)
        self.lb_Ros_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_Ros_unit, 20, 1, 1, 1)

        self.label_30 = QLabel(self.tab_GD)
        self.label_30.setObjectName(u"label_30")
        sizePolicy1.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy1)
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_30, 19, 0, 1, 1)

        self.lb_Rp3 = QLabel(self.tab_GD)
        self.lb_Rp3.setObjectName(u"lb_Rp3")
        sizePolicy1.setHeightForWidth(self.lb_Rp3.sizePolicy().hasHeightForWidth())
        self.lb_Rp3.setSizePolicy(sizePolicy1)
        self.lb_Rp3.setFont(font2)
        self.lb_Rp3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rp3, 15, 3, 1, 1)

        self.le_x2 = QLineEdit(self.tab_GD)
        self.le_x2.setObjectName(u"le_x2")
        sizePolicy4.setHeightForWidth(self.le_x2.sizePolicy().hasHeightForWidth())
        self.le_x2.setSizePolicy(sizePolicy4)
        self.le_x2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_x2, 13, 4, 1, 1)

        self.label_34 = QLabel(self.tab_GD)
        self.label_34.setObjectName(u"label_34")
        sizePolicy1.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy1)
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_34, 22, 0, 1, 1)

        self.label_54 = QLabel(self.tab_GD)
        self.label_54.setObjectName(u"label_54")
        sizePolicy1.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy1)
        self.label_54.setFont(font2)
        self.label_54.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_54, 37, 0, 1, 1)

        self.lb_tt2 = QLabel(self.tab_GD)
        self.lb_tt2.setObjectName(u"lb_tt2")
        sizePolicy1.setHeightForWidth(self.lb_tt2.sizePolicy().hasHeightForWidth())
        self.lb_tt2.setSizePolicy(sizePolicy1)
        self.lb_tt2.setFont(font2)
        self.lb_tt2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_tt2, 17, 4, 1, 1)

        self.lb_tts_unit = QLabel(self.tab_GD)
        self.lb_tts_unit.setObjectName(u"lb_tts_unit")
        sizePolicy1.setHeightForWidth(self.lb_tts_unit.sizePolicy().hasHeightForWidth())
        self.lb_tts_unit.setSizePolicy(sizePolicy1)
        self.lb_tts_unit.setFont(font2)
        self.lb_tts_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_tts_unit, 16, 1, 1, 1)

        self.label_43 = QLabel(self.tab_GD)
        self.label_43.setObjectName(u"label_43")
        sizePolicy1.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy1)
        self.label_43.setFont(font2)
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_43, 14, 0, 1, 1)

        self.le_mod = QLineEdit(self.tab_GD)
        self.le_mod.setObjectName(u"le_mod")
        sizePolicy4.setHeightForWidth(self.le_mod.sizePolicy().hasHeightForWidth())
        self.le_mod.setSizePolicy(sizePolicy4)
        self.le_mod.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_mod, 6, 2, 1, 1)

        self.lb_Ros2 = QLabel(self.tab_GD)
        self.lb_Ros2.setObjectName(u"lb_Ros2")
        sizePolicy1.setHeightForWidth(self.lb_Ros2.sizePolicy().hasHeightForWidth())
        self.lb_Ros2.setSizePolicy(sizePolicy1)
        self.lb_Ros2.setFont(font2)
        self.lb_Ros2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Ros2, 20, 4, 1, 1)

        self.le_rtcl1 = QLineEdit(self.tab_GD)
        self.le_rtcl1.setObjectName(u"le_rtcl1")
        sizePolicy4.setHeightForWidth(self.le_rtcl1.sizePolicy().hasHeightForWidth())
        self.le_rtcl1.setSizePolicy(sizePolicy4)
        self.le_rtcl1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_rtcl1, 27, 2, 1, 1)

        self.lb_G1 = QLabel(self.tab_GD)
        self.lb_G1.setObjectName(u"lb_G1")
        sizePolicy1.setHeightForWidth(self.lb_G1.sizePolicy().hasHeightForWidth())
        self.lb_G1.setSizePolicy(sizePolicy1)
        self.lb_G1.setFont(font4)
        self.lb_G1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_G1, 10, 2, 1, 1)

        self.label_49 = QLabel(self.tab_GD)
        self.label_49.setObjectName(u"label_49")
        sizePolicy1.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy1)
        self.label_49.setFont(font2)
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_49, 24, 0, 1, 1)

        self.label_52 = QLabel(self.tab_GD)
        self.label_52.setObjectName(u"label_52")
        sizePolicy1.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy1)
        self.label_52.setFont(font2)
        self.label_52.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_52, 16, 0, 1, 1)

        self.label_58 = QLabel(self.tab_GD)
        self.label_58.setObjectName(u"label_58")
        sizePolicy1.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy1)
        self.label_58.setFont(font2)
        self.label_58.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_58, 34, 0, 1, 1)

        self.le_x1 = QLineEdit(self.tab_GD)
        self.le_x1.setObjectName(u"le_x1")
        sizePolicy4.setHeightForWidth(self.le_x1.sizePolicy().hasHeightForWidth())
        self.le_x1.setSizePolicy(sizePolicy4)
        self.le_x1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_x1, 13, 2, 1, 1)

        self.le_Rtip1 = QLineEdit(self.tab_GD)
        self.le_Rtip1.setObjectName(u"le_Rtip1")
        sizePolicy4.setHeightForWidth(self.le_Rtip1.sizePolicy().hasHeightForWidth())
        self.le_Rtip1.setSizePolicy(sizePolicy4)
        self.le_Rtip1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.le_Rtip1, 22, 2, 1, 1)

        self.lb_Rp2 = QLabel(self.tab_GD)
        self.lb_Rp2.setObjectName(u"lb_Rp2")
        sizePolicy1.setHeightForWidth(self.lb_Rp2.sizePolicy().hasHeightForWidth())
        self.lb_Rp2.setSizePolicy(sizePolicy1)
        self.lb_Rp2.setFont(font2)
        self.lb_Rp2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_Rp2, 15, 4, 1, 1)

        self.lb_bkl_text = QLabel(self.tab_GD)
        self.lb_bkl_text.setObjectName(u"lb_bkl_text")
        sizePolicy1.setHeightForWidth(self.lb_bkl_text.sizePolicy().hasHeightForWidth())
        self.lb_bkl_text.setSizePolicy(sizePolicy1)
        self.lb_bkl_text.setFont(font2)
        self.lb_bkl_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_bkl_text, 36, 0, 1, 1)

        self.lb_Rtip_unit = QLabel(self.tab_GD)
        self.lb_Rtip_unit.setObjectName(u"lb_Rtip_unit")
        sizePolicy1.setHeightForWidth(self.lb_Rtip_unit.sizePolicy().hasHeightForWidth())
        self.lb_Rtip_unit.setSizePolicy(sizePolicy1)
        self.lb_Rtip_unit.setFont(font2)
        self.lb_Rtip_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_Rtip_unit, 22, 1, 1, 1)

        self.lb_spacing_text = QLabel(self.tab_GD)
        self.lb_spacing_text.setObjectName(u"lb_spacing_text")
        sizePolicy1.setHeightForWidth(self.lb_spacing_text.sizePolicy().hasHeightForWidth())
        self.lb_spacing_text.setSizePolicy(sizePolicy1)
        self.lb_spacing_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_spacing_text, 8, 3, 1, 1)

        self.lb_icon_spacing = QLabel(self.tab_GD)
        self.lb_icon_spacing.setObjectName(u"lb_icon_spacing")
        sizePolicy1.setHeightForWidth(self.lb_icon_spacing.sizePolicy().hasHeightForWidth())
        self.lb_icon_spacing.setSizePolicy(sizePolicy1)
        self.lb_icon_spacing.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lb_icon_spacing, 8, 4, 1, 1)

        self.line_9 = QFrame(self.tab_GD)
        self.line_9.setObjectName(u"line_9")
        sizePolicy4.setHeightForWidth(self.line_9.sizePolicy().hasHeightForWidth())
        self.line_9.setSizePolicy(sizePolicy4)
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_9, 5, 2, 1, 3)

        self.line_4 = QFrame(self.tab_GD)
        self.line_4.setObjectName(u"line_4")
        sizePolicy4.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy4)
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 11, 2, 1, 3)


        self.vl_dims.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.vl_dims)

        self.vl_button_GD = QVBoxLayout()
        self.vl_button_GD.setSpacing(6)
        self.vl_button_GD.setObjectName(u"vl_button_GD")
        self.vl_button_GD.setContentsMargins(6, 0, 6, 0)
        self.line_29 = QFrame(self.tab_GD)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFont(font1)
        self.line_29.setFrameShadow(QFrame.Shadow.Raised)
        self.line_29.setLineWidth(5)
        self.line_29.setFrameShape(QFrame.Shape.HLine)

        self.vl_button_GD.addWidget(self.line_29)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, -1)
        self.pb_drawGear = QPushButton(self.tab_GD)
        self.pb_drawGear.setObjectName(u"pb_drawGear")

        self.horizontalLayout_16.addWidget(self.pb_drawGear)


        self.vl_button_GD.addLayout(self.horizontalLayout_16)


        self.verticalLayout.addLayout(self.vl_button_GD)

        self.verticalSpacer = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.tabW_GD = QTabWidget(self.tab_GD)
        self.tabW_GD.setObjectName(u"tabW_GD")
        self.tabW_GD.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.tabW_GD.sizePolicy().hasHeightForWidth())
        self.tabW_GD.setSizePolicy(sizePolicy3)
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
        self.tab_G3 = QWidget()
        self.tab_G3.setObjectName(u"tab_G3")
        self.tab_G3.setEnabled(True)
        self.vLayout_canvasG3 = QVBoxLayout(self.tab_G3)
        self.vLayout_canvasG3.setObjectName(u"vLayout_canvasG3")
        self.hLayout_toolbarG3 = QHBoxLayout()
        self.hLayout_toolbarG3.setObjectName(u"hLayout_toolbarG3")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_toolbarG3.addItem(self.horizontalSpacer_16)

        self.cb_singleViewG3 = QCheckBox(self.tab_G3)
        self.cb_singleViewG3.setObjectName(u"cb_singleViewG3")

        self.hLayout_toolbarG3.addWidget(self.cb_singleViewG3)

        self.cb_circlesG3 = QCheckBox(self.tab_G3)
        self.cb_circlesG3.setObjectName(u"cb_circlesG3")

        self.hLayout_toolbarG3.addWidget(self.cb_circlesG3)


        self.vLayout_canvasG3.addLayout(self.hLayout_toolbarG3)

        self.tabW_GD.addTab(self.tab_G3, "")
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
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
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

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.cb_singleViewMesh = QCheckBox(self.tab_Mesh)
        self.cb_singleViewMesh.setObjectName(u"cb_singleViewMesh")
        self.cb_singleViewMesh.setChecked(False)

        self.verticalLayout_5.addWidget(self.cb_singleViewMesh)

        self.rb_sp = QRadioButton(self.tab_Mesh)
        self.bg_mesh = QButtonGroup(MainForm)
        self.bg_mesh.setObjectName(u"bg_mesh")
        self.bg_mesh.addButton(self.rb_sp)
        self.rb_sp.setObjectName(u"rb_sp")
        self.rb_sp.setEnabled(False)
        self.rb_sp.setChecked(True)

        self.verticalLayout_5.addWidget(self.rb_sp)

        self.rb_pr = QRadioButton(self.tab_Mesh)
        self.bg_mesh.addButton(self.rb_pr)
        self.rb_pr.setObjectName(u"rb_pr")
        self.rb_pr.setEnabled(False)
        self.rb_pr.setChecked(False)

        self.verticalLayout_5.addWidget(self.rb_pr)


        self.hLayout_toolbarMesh.addLayout(self.verticalLayout_5)

        self.cb_circlesMesh = QCheckBox(self.tab_Mesh)
        self.cb_circlesMesh.setObjectName(u"cb_circlesMesh")

        self.hLayout_toolbarMesh.addWidget(self.cb_circlesMesh)

        self.cb_LoC = QCheckBox(self.tab_Mesh)
        self.cb_LoC.setObjectName(u"cb_LoC")
        self.cb_LoC.setChecked(False)

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
        self.horizontalSpacer_11 = QSpacerItem(6, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(6, 0, 6, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 10)
        self.label_8 = QLabel(self.tab_stress)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_8)

        self.line_27 = QFrame(self.tab_stress)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFont(font1)
        self.line_27.setFrameShadow(QFrame.Shadow.Raised)
        self.line_27.setLineWidth(5)
        self.line_27.setFrameShape(QFrame.Shape.HLine)

        self.horizontalLayout_13.addWidget(self.line_27)


        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(6, 6, -1, 10)
        self.label_62 = QLabel(self.tab_stress)
        self.label_62.setObjectName(u"label_62")
        sizePolicy1.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy1)
        self.label_62.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_62, 0, 1, 1, 1)

        self.lb_torque_unit = QLabel(self.tab_stress)
        self.lb_torque_unit.setObjectName(u"lb_torque_unit")
        sizePolicy1.setHeightForWidth(self.lb_torque_unit.sizePolicy().hasHeightForWidth())
        self.lb_torque_unit.setSizePolicy(sizePolicy1)
        self.lb_torque_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_torque_unit, 1, 1, 1, 1)

        self.label_64 = QLabel(self.tab_stress)
        self.label_64.setObjectName(u"label_64")
        sizePolicy1.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy1)
        self.label_64.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_64, 7, 1, 1, 1)

        self.le_FW1 = QLineEdit(self.tab_stress)
        self.le_FW1.setObjectName(u"le_FW1")
        sizePolicy4.setHeightForWidth(self.le_FW1.sizePolicy().hasHeightForWidth())
        self.le_FW1.setSizePolicy(sizePolicy4)
        self.le_FW1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_FW1, 5, 2, 1, 1)

        self.line_16 = QFrame(self.tab_stress)
        self.line_16.setObjectName(u"line_16")
        sizePolicy4.setHeightForWidth(self.line_16.sizePolicy().hasHeightForWidth())
        self.line_16.setSizePolicy(sizePolicy4)
        self.line_16.setFrameShape(QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_16, 2, 0, 1, 5)

        self.label_85 = QLabel(self.tab_stress)
        self.label_85.setObjectName(u"label_85")
        sizePolicy1.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy1)
        self.label_85.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_85, 0, 0, 1, 1)

        self.lb_stressC_unit = QLabel(self.tab_stress)
        self.lb_stressC_unit.setObjectName(u"lb_stressC_unit")
        sizePolicy1.setHeightForWidth(self.lb_stressC_unit.sizePolicy().hasHeightForWidth())
        self.lb_stressC_unit.setSizePolicy(sizePolicy1)
        self.lb_stressC_unit.setFont(font2)
        self.lb_stressC_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_stressC_unit, 10, 1, 1, 1)

        self.le_FW2 = QLineEdit(self.tab_stress)
        self.le_FW2.setObjectName(u"le_FW2")
        sizePolicy4.setHeightForWidth(self.le_FW2.sizePolicy().hasHeightForWidth())
        self.le_FW2.setSizePolicy(sizePolicy4)
        self.le_FW2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_FW2, 5, 4, 1, 1)

        self.lb_FW_unit = QLabel(self.tab_stress)
        self.lb_FW_unit.setObjectName(u"lb_FW_unit")
        sizePolicy1.setHeightForWidth(self.lb_FW_unit.sizePolicy().hasHeightForWidth())
        self.lb_FW_unit.setSizePolicy(sizePolicy1)
        self.lb_FW_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_FW_unit, 5, 1, 1, 1)

        self.line_17 = QFrame(self.tab_stress)
        self.line_17.setObjectName(u"line_17")
        sizePolicy4.setHeightForWidth(self.line_17.sizePolicy().hasHeightForWidth())
        self.line_17.setSizePolicy(sizePolicy4)
        self.line_17.setFrameShape(QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_17, 4, 2, 1, 3)

        self.lb_stressG3 = QLabel(self.tab_stress)
        self.lb_stressG3.setObjectName(u"lb_stressG3")
        sizePolicy1.setHeightForWidth(self.lb_stressG3.sizePolicy().hasHeightForWidth())
        self.lb_stressG3.setSizePolicy(sizePolicy1)
        self.lb_stressG3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_stressG3, 3, 3, 1, 1)

        self.le_nu2 = QLineEdit(self.tab_stress)
        self.le_nu2.setObjectName(u"le_nu2")
        sizePolicy4.setHeightForWidth(self.le_nu2.sizePolicy().hasHeightForWidth())
        self.le_nu2.setSizePolicy(sizePolicy4)
        self.le_nu2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_nu2, 7, 4, 1, 1)

        self.lb_E_unit = QLabel(self.tab_stress)
        self.lb_E_unit.setObjectName(u"lb_E_unit")
        sizePolicy1.setHeightForWidth(self.lb_E_unit.sizePolicy().hasHeightForWidth())
        self.lb_E_unit.setSizePolicy(sizePolicy1)
        self.lb_E_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_E_unit, 6, 1, 1, 1)

        self.line_15 = QFrame(self.tab_stress)
        self.line_15.setObjectName(u"line_15")
        sizePolicy4.setHeightForWidth(self.line_15.sizePolicy().hasHeightForWidth())
        self.line_15.setSizePolicy(sizePolicy4)
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_15, 8, 0, 1, 5)

        self.le_nu3 = QLineEdit(self.tab_stress)
        self.le_nu3.setObjectName(u"le_nu3")
        sizePolicy4.setHeightForWidth(self.le_nu3.sizePolicy().hasHeightForWidth())
        self.le_nu3.setSizePolicy(sizePolicy4)
        self.le_nu3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_nu3, 7, 3, 1, 1)

        self.le_E1 = QLineEdit(self.tab_stress)
        self.le_E1.setObjectName(u"le_E1")
        sizePolicy4.setHeightForWidth(self.le_E1.sizePolicy().hasHeightForWidth())
        self.le_E1.setSizePolicy(sizePolicy4)
        self.le_E1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_E1, 6, 2, 1, 1)

        self.lb_pitchLineVel = QLabel(self.tab_stress)
        self.lb_pitchLineVel.setObjectName(u"lb_pitchLineVel")
        sizePolicy1.setHeightForWidth(self.lb_pitchLineVel.sizePolicy().hasHeightForWidth())
        self.lb_pitchLineVel.setSizePolicy(sizePolicy1)
        self.lb_pitchLineVel.setFont(font2)
        self.lb_pitchLineVel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_pitchLineVel, 11, 2, 1, 1)

        self.label_78 = QLabel(self.tab_stress)
        self.label_78.setObjectName(u"label_78")
        sizePolicy1.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy1)
        self.label_78.setFont(font2)
        self.label_78.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_78, 10, 0, 1, 1)

        self.label_86 = QLabel(self.tab_stress)
        self.label_86.setObjectName(u"label_86")
        sizePolicy1.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy1)
        self.label_86.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_86, 6, 0, 1, 1)

        self.lb_stressB1 = QLabel(self.tab_stress)
        self.lb_stressB1.setObjectName(u"lb_stressB1")
        sizePolicy1.setHeightForWidth(self.lb_stressB1.sizePolicy().hasHeightForWidth())
        self.lb_stressB1.setSizePolicy(sizePolicy1)
        self.lb_stressB1.setFont(font2)
        self.lb_stressB1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_stressB1, 9, 2, 1, 1)

        self.lb_stressG1 = QLabel(self.tab_stress)
        self.lb_stressG1.setObjectName(u"lb_stressG1")
        sizePolicy1.setHeightForWidth(self.lb_stressG1.sizePolicy().hasHeightForWidth())
        self.lb_stressG1.setSizePolicy(sizePolicy1)
        self.lb_stressG1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_stressG1, 3, 2, 1, 1)

        self.lb_stressG2 = QLabel(self.tab_stress)
        self.lb_stressG2.setObjectName(u"lb_stressG2")
        sizePolicy1.setHeightForWidth(self.lb_stressG2.sizePolicy().hasHeightForWidth())
        self.lb_stressG2.setSizePolicy(sizePolicy1)
        self.lb_stressG2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_stressG2, 3, 4, 1, 1)

        self.le_RPM = QLineEdit(self.tab_stress)
        self.le_RPM.setObjectName(u"le_RPM")
        sizePolicy4.setHeightForWidth(self.le_RPM.sizePolicy().hasHeightForWidth())
        self.le_RPM.setSizePolicy(sizePolicy4)
        self.le_RPM.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_RPM, 0, 2, 1, 1)

        self.label_83 = QLabel(self.tab_stress)
        self.label_83.setObjectName(u"label_83")
        sizePolicy1.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy1)
        self.label_83.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_83, 5, 0, 1, 1)

        self.le_nu1 = QLineEdit(self.tab_stress)
        self.le_nu1.setObjectName(u"le_nu1")
        sizePolicy4.setHeightForWidth(self.le_nu1.sizePolicy().hasHeightForWidth())
        self.le_nu1.setSizePolicy(sizePolicy4)
        self.le_nu1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_nu1, 7, 2, 1, 1)

        self.le_E3 = QLineEdit(self.tab_stress)
        self.le_E3.setObjectName(u"le_E3")
        sizePolicy4.setHeightForWidth(self.le_E3.sizePolicy().hasHeightForWidth())
        self.le_E3.setSizePolicy(sizePolicy4)
        self.le_E3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_E3, 6, 3, 1, 1)

        self.lb_stressC1 = QLabel(self.tab_stress)
        self.lb_stressC1.setObjectName(u"lb_stressC1")
        sizePolicy1.setHeightForWidth(self.lb_stressC1.sizePolicy().hasHeightForWidth())
        self.lb_stressC1.setSizePolicy(sizePolicy1)
        self.lb_stressC1.setFont(font2)
        self.lb_stressC1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_stressC1, 10, 2, 1, 1)

        self.label_76 = QLabel(self.tab_stress)
        self.label_76.setObjectName(u"label_76")
        sizePolicy1.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy1)
        self.label_76.setFont(font2)
        self.label_76.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_76, 9, 0, 1, 1)

        self.label_80 = QLabel(self.tab_stress)
        self.label_80.setObjectName(u"label_80")
        sizePolicy1.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy1)
        self.label_80.setFont(font2)
        self.label_80.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_80, 11, 0, 1, 1)

        self.lb_stressB3 = QLabel(self.tab_stress)
        self.lb_stressB3.setObjectName(u"lb_stressB3")
        sizePolicy1.setHeightForWidth(self.lb_stressB3.sizePolicy().hasHeightForWidth())
        self.lb_stressB3.setSizePolicy(sizePolicy1)
        self.lb_stressB3.setFont(font2)
        self.lb_stressB3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_stressB3, 9, 3, 1, 1)

        self.lb_stressC3 = QLabel(self.tab_stress)
        self.lb_stressC3.setObjectName(u"lb_stressC3")
        sizePolicy1.setHeightForWidth(self.lb_stressC3.sizePolicy().hasHeightForWidth())
        self.lb_stressC3.setSizePolicy(sizePolicy1)
        self.lb_stressC3.setFont(font2)
        self.lb_stressC3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_stressC3, 10, 3, 1, 1)

        self.le_torque = QLineEdit(self.tab_stress)
        self.le_torque.setObjectName(u"le_torque")
        sizePolicy4.setHeightForWidth(self.le_torque.sizePolicy().hasHeightForWidth())
        self.le_torque.setSizePolicy(sizePolicy4)
        self.le_torque.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_torque, 1, 2, 1, 1)

        self.label_87 = QLabel(self.tab_stress)
        self.label_87.setObjectName(u"label_87")
        sizePolicy1.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy1)
        self.label_87.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_87, 7, 0, 1, 1)

        self.lb_pitchLineVel_unit = QLabel(self.tab_stress)
        self.lb_pitchLineVel_unit.setObjectName(u"lb_pitchLineVel_unit")
        sizePolicy1.setHeightForWidth(self.lb_pitchLineVel_unit.sizePolicy().hasHeightForWidth())
        self.lb_pitchLineVel_unit.setSizePolicy(sizePolicy1)
        self.lb_pitchLineVel_unit.setFont(font2)
        self.lb_pitchLineVel_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_pitchLineVel_unit, 11, 1, 1, 1)

        self.lb_stressB_unit = QLabel(self.tab_stress)
        self.lb_stressB_unit.setObjectName(u"lb_stressB_unit")
        sizePolicy1.setHeightForWidth(self.lb_stressB_unit.sizePolicy().hasHeightForWidth())
        self.lb_stressB_unit.setSizePolicy(sizePolicy1)
        self.lb_stressB_unit.setFont(font2)
        self.lb_stressB_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_stressB_unit, 9, 1, 1, 1)

        self.lb_stressB2 = QLabel(self.tab_stress)
        self.lb_stressB2.setObjectName(u"lb_stressB2")
        sizePolicy1.setHeightForWidth(self.lb_stressB2.sizePolicy().hasHeightForWidth())
        self.lb_stressB2.setSizePolicy(sizePolicy1)
        self.lb_stressB2.setFont(font2)
        self.lb_stressB2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_stressB2, 9, 4, 1, 1)

        self.le_E2 = QLineEdit(self.tab_stress)
        self.le_E2.setObjectName(u"le_E2")
        sizePolicy4.setHeightForWidth(self.le_E2.sizePolicy().hasHeightForWidth())
        self.le_E2.setSizePolicy(sizePolicy4)
        self.le_E2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_E2, 6, 4, 1, 1)

        self.le_FW3 = QLineEdit(self.tab_stress)
        self.le_FW3.setObjectName(u"le_FW3")
        sizePolicy4.setHeightForWidth(self.le_FW3.sizePolicy().hasHeightForWidth())
        self.le_FW3.setSizePolicy(sizePolicy4)
        self.le_FW3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_FW3, 5, 3, 1, 1)

        self.label_84 = QLabel(self.tab_stress)
        self.label_84.setObjectName(u"label_84")
        sizePolicy1.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy1)
        self.label_84.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_84, 1, 0, 1, 1)

        self.lb_stressC2 = QLabel(self.tab_stress)
        self.lb_stressC2.setObjectName(u"lb_stressC2")
        sizePolicy1.setHeightForWidth(self.lb_stressC2.sizePolicy().hasHeightForWidth())
        self.lb_stressC2.setSizePolicy(sizePolicy1)
        self.lb_stressC2.setFont(font2)
        self.lb_stressC2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lb_stressC2, 10, 4, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(6, 0, 6, 0)
        self.line_28 = QFrame(self.tab_stress)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFont(font1)
        self.line_28.setFrameShadow(QFrame.Shadow.Raised)
        self.line_28.setLineWidth(5)
        self.line_28.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_11.addWidget(self.line_28)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 6, -1, -1)
        self.pb_stress = QPushButton(self.tab_stress)
        self.pb_stress.setObjectName(u"pb_stress")

        self.horizontalLayout_18.addWidget(self.pb_stress)


        self.verticalLayout_11.addLayout(self.horizontalLayout_18)


        self.verticalLayout_4.addLayout(self.verticalLayout_11)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(10, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.tabW_stress = QTabWidget(self.tab_stress)
        self.tabW_stress.setObjectName(u"tabW_stress")
        self.tabW_stress.setTabPosition(QTabWidget.TabPosition.South)
        self.tab_stress1 = QWidget()
        self.tab_stress1.setObjectName(u"tab_stress1")
        self.vl_tab_stress1 = QVBoxLayout(self.tab_stress1)
        self.vl_tab_stress1.setObjectName(u"vl_tab_stress1")
        self.tabW_stress.addTab(self.tab_stress1, "")
        self.tab_stress2 = QWidget()
        self.tab_stress2.setObjectName(u"tab_stress2")
        self.vl_tab_stress2 = QVBoxLayout(self.tab_stress2)
        self.vl_tab_stress2.setObjectName(u"vl_tab_stress2")
        self.tabW_stress.addTab(self.tab_stress2, "")

        self.horizontalLayout_6.addWidget(self.tabW_stress)

        self.tabW_main.addTab(self.tab_stress, "")

        self.topLayout.addWidget(self.tabW_main)

        QWidget.setTabOrder(self.cb_input_helper, self.cb_output_helper)
        QWidget.setTabOrder(self.cb_output_helper, self.le_targetMod)
        QWidget.setTabOrder(self.le_targetMod, self.le_targetGR)
        QWidget.setTabOrder(self.le_targetGR, self.cb_CD_width)
        QWidget.setTabOrder(self.cb_CD_width, self.le_targetSize)
        QWidget.setTabOrder(self.le_targetSize, self.pb_calcGearSizes)
        QWidget.setTabOrder(self.pb_calcGearSizes, self.le_N1_layout)
        QWidget.setTabOrder(self.le_N1_layout, self.rb_1)
        QWidget.setTabOrder(self.rb_1, self.rb_2)
        QWidget.setTabOrder(self.rb_2, self.rb_3)
        QWidget.setTabOrder(self.rb_3, self.rb_4)
        QWidget.setTabOrder(self.rb_4, self.rb_5)
        QWidget.setTabOrder(self.rb_5, self.le_planets)
        QWidget.setTabOrder(self.le_planets, self.rb_p1)
        QWidget.setTabOrder(self.rb_p1, self.rb_p2)
        QWidget.setTabOrder(self.rb_p2, self.rb_p3)
        QWidget.setTabOrder(self.rb_p3, self.rb_p4)
        QWidget.setTabOrder(self.rb_p4, self.rb_p5)
        QWidget.setTabOrder(self.rb_p5, self.pb_useLayout)
        QWidget.setTabOrder(self.pb_useLayout, self.cb_type_design)
        QWidget.setTabOrder(self.cb_type_design, self.le_mod)
        QWidget.setTabOrder(self.le_mod, self.le_PA_deg)
        QWidget.setTabOrder(self.le_PA_deg, self.cb_CD_bkl)
        QWidget.setTabOrder(self.cb_CD_bkl, self.le_CD_bkl1)
        QWidget.setTabOrder(self.le_CD_bkl1, self.le_bkl2)
        QWidget.setTabOrder(self.le_bkl2, self.le_NPlanets)
        QWidget.setTabOrder(self.le_NPlanets, self.le_N1)
        QWidget.setTabOrder(self.le_N1, self.le_N2)
        QWidget.setTabOrder(self.le_N2, self.le_x1)
        QWidget.setTabOrder(self.le_x1, self.le_x3)
        QWidget.setTabOrder(self.le_x3, self.le_x2)
        QWidget.setTabOrder(self.le_x2, self.le_Ro1)
        QWidget.setTabOrder(self.le_Ro1, self.le_Ro3)
        QWidget.setTabOrder(self.le_Ro3, self.le_Ro2)
        QWidget.setTabOrder(self.le_Ro2, self.le_Rtip1)
        QWidget.setTabOrder(self.le_Rtip1, self.le_Rtip3)
        QWidget.setTabOrder(self.le_Rtip3, self.le_Rtip2)
        QWidget.setTabOrder(self.le_Rtip2, self.le_Rrim)
        QWidget.setTabOrder(self.le_Rrim, self.le_rtcl1)
        QWidget.setTabOrder(self.le_rtcl1, self.le_rtcl3)
        QWidget.setTabOrder(self.le_rtcl3, self.le_rtcl2)
        QWidget.setTabOrder(self.le_rtcl2, self.le_Rr2)
        QWidget.setTabOrder(self.le_Rr2, self.le_Rf1)
        QWidget.setTabOrder(self.le_Rf1, self.le_Rf3)
        QWidget.setTabOrder(self.le_Rf3, self.le_Rf2)
        QWidget.setTabOrder(self.le_Rf2, self.pb_drawGear)
        QWidget.setTabOrder(self.pb_drawGear, self.hSlider_Mesh)
        QWidget.setTabOrder(self.hSlider_Mesh, self.cb_singleViewMesh)
        QWidget.setTabOrder(self.cb_singleViewMesh, self.rb_sp)
        QWidget.setTabOrder(self.rb_sp, self.rb_pr)
        QWidget.setTabOrder(self.rb_pr, self.cb_circlesMesh)
        QWidget.setTabOrder(self.cb_circlesMesh, self.cb_LoC)
        QWidget.setTabOrder(self.cb_LoC, self.pb_animate)
        QWidget.setTabOrder(self.pb_animate, self.le_RPM)
        QWidget.setTabOrder(self.le_RPM, self.le_torque)
        QWidget.setTabOrder(self.le_torque, self.le_FW1)
        QWidget.setTabOrder(self.le_FW1, self.le_FW3)
        QWidget.setTabOrder(self.le_FW3, self.le_FW2)
        QWidget.setTabOrder(self.le_FW2, self.le_E1)
        QWidget.setTabOrder(self.le_E1, self.le_E3)
        QWidget.setTabOrder(self.le_E3, self.le_E2)
        QWidget.setTabOrder(self.le_E2, self.le_nu1)
        QWidget.setTabOrder(self.le_nu1, self.le_nu3)
        QWidget.setTabOrder(self.le_nu3, self.le_nu2)
        QWidget.setTabOrder(self.le_nu2, self.pb_stress)
        QWidget.setTabOrder(self.pb_stress, self.tabW_GD)
        QWidget.setTabOrder(self.tabW_GD, self.cb_singleViewG1)
        QWidget.setTabOrder(self.cb_singleViewG1, self.cb_type_helper)
        QWidget.setTabOrder(self.cb_type_helper, self.cb_output_GD)
        QWidget.setTabOrder(self.cb_output_GD, self.cb_input_GD)
        QWidget.setTabOrder(self.cb_input_GD, self.cb_singleViewG2)
        QWidget.setTabOrder(self.cb_singleViewG2, self.cb_singleViewG3)
        QWidget.setTabOrder(self.cb_singleViewG3, self.tabW_main)
        QWidget.setTabOrder(self.tabW_main, self.cb_circlesG2)
        QWidget.setTabOrder(self.cb_circlesG2, self.tabW_stress)
        QWidget.setTabOrder(self.tabW_stress, self.cb_circlesG1)
        QWidget.setTabOrder(self.cb_circlesG1, self.cb_circlesG3)

        self.retranslateUi(MainForm)

        self.tabW_main.setCurrentIndex(0)
        self.cb_type_helper.setCurrentIndex(0)
        self.cb_output_helper.setCurrentIndex(-1)
        self.cb_input_helper.setCurrentIndex(-1)
        self.cb_type_design.setCurrentIndex(0)
        self.cb_output_GD.setCurrentIndex(-1)
        self.cb_input_GD.setCurrentIndex(-1)
        self.cb_CD_bkl.setCurrentIndex(0)
        self.tabW_GD.setCurrentIndex(0)
        self.tabW_stress.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"jpGear", None))
        self.label_2.setText(QCoreApplication.translate("MainForm", u"Layout Style", None))
        self.cb_type_helper.setItemText(0, QCoreApplication.translate("MainForm", u"External", None))
        self.cb_type_helper.setItemText(1, QCoreApplication.translate("MainForm", u"Internal", None))
        self.cb_type_helper.setItemText(2, QCoreApplication.translate("MainForm", u"Planetary", None))

        self.cb_output_helper.setItemText(0, QCoreApplication.translate("MainForm", u"Sun", None))
        self.cb_output_helper.setItemText(1, QCoreApplication.translate("MainForm", u"Planet Carrier", None))
        self.cb_output_helper.setItemText(2, QCoreApplication.translate("MainForm", u"Ring", None))

        self.cb_output_helper.setPlaceholderText(QCoreApplication.translate("MainForm", u"- Select -", None))
        self.lb_input.setText(QCoreApplication.translate("MainForm", u"Input", None))
        self.lb_stationary.setText(QCoreApplication.translate("MainForm", u"Stationary", None))
        self.lb_stationGear1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_output.setText(QCoreApplication.translate("MainForm", u"Output", None))
        self.cb_input_helper.setItemText(0, QCoreApplication.translate("MainForm", u"Sun", None))
        self.cb_input_helper.setItemText(1, QCoreApplication.translate("MainForm", u"Planet Carrier", None))
        self.cb_input_helper.setItemText(2, QCoreApplication.translate("MainForm", u"Ring", None))

        self.cb_input_helper.setCurrentText("")
        self.cb_input_helper.setPlaceholderText(QCoreApplication.translate("MainForm", u"- Select -", None))
        self.label_3.setText(QCoreApplication.translate("MainForm", u"Overall Size", None))
        self.lb_targetCD_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.cb_CD_width.setItemText(0, QCoreApplication.translate("MainForm", u"Target Center Distance", None))
        self.cb_CD_width.setItemText(1, QCoreApplication.translate("MainForm", u"Target Overall Width", None))

        self.pb_calcGearSizes.setText(QCoreApplication.translate("MainForm", u"Find Gear Sizes", None))
        self.lb_TargetGearRatio.setText(QCoreApplication.translate("MainForm", u"Target Gear Ratio", None))
        self.lb_targetMod_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_TargetModule.setText(QCoreApplication.translate("MainForm", u"Target Module", None))
        self.lb_TargetModule_3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_7.setText(QCoreApplication.translate("MainForm", u"Number of Teeth", None))
        self.lb_planet.setText(QCoreApplication.translate("MainForm", u"Planet", None))
        self.lb_width2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_N3_4.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_GearRatio.setText(QCoreApplication.translate("MainForm", u"Ratio", None))
        self.lb_width1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_CD5.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_CD3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.rb_3.setText("")
        self.lb_width3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_icon4.setText("")
        self.rb_4.setText("")
        self.lb_N3_5.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_width4.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_GR5.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_N3_3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_CD2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.rb_5.setText("")
        self.lb_GR3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_GR4.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_N3_2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_CD4.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_width5.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_icon5.setText("")
        self.lb_N2_1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_N2_4.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_N2_2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_OverallWidth.setText(QCoreApplication.translate("MainForm", u"Overall\n"
"Width", None))
        self.lb_GR2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_icon1.setText("")
        self.lb_gear.setText(QCoreApplication.translate("MainForm", u"Gear", None))
        self.lb_CD1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_GR1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.rb_2.setText("")
        self.lb_N2_3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.rb_1.setText("")
        self.lb_icon3.setText("")
        self.lb_N2_5.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_icon2.setText("")
        self.lb_N3_1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_pinion.setText(QCoreApplication.translate("MainForm", u"Pinion", None))
        self.lb_CenterDistance.setText(QCoreApplication.translate("MainForm", u"Center\n"
"Distance", None))
        self.lb_OverallWidth_2.setText(QCoreApplication.translate("MainForm", u"Coprime?", None))
        self.label_4.setText(QCoreApplication.translate("MainForm", u"Number of Planets", None))
        self.lb_p_icon3.setText("")
        self.lb_p_icon5.setText("")
        self.lb_planet1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_planet3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.rb_p4.setText("")
        self.lb_planet5.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_planet4.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.rb_p3.setText("")
        self.lb_planets.setText(QCoreApplication.translate("MainForm", u"Planets", None))
        self.rb_p2.setText("")
        self.rb_p1.setText("")
        self.rb_p5.setText("")
        self.lb_p_icon2.setText("")
        self.lb_p_icon1.setText("")
        self.lb_planet2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_p_icon4.setText("")
        self.lb_even.setText(QCoreApplication.translate("MainForm", u"Evenly\n"
"Spaced?", None))
        self.pb_useLayout.setText(QCoreApplication.translate("MainForm", u"Use this Layout", None))
        self.tabW_main.setTabText(self.tabW_main.indexOf(self.tab_layout), QCoreApplication.translate("MainForm", u"Layout Helper", None))
        self.label_5.setText(QCoreApplication.translate("MainForm", u"Layout Style", None))
        self.cb_type_design.setItemText(0, QCoreApplication.translate("MainForm", u"External", None))
        self.cb_type_design.setItemText(1, QCoreApplication.translate("MainForm", u"Internal", None))
        self.cb_type_design.setItemText(2, QCoreApplication.translate("MainForm", u"Planetary", None))

        self.cb_output_GD.setItemText(0, QCoreApplication.translate("MainForm", u"Sun", None))
        self.cb_output_GD.setItemText(1, QCoreApplication.translate("MainForm", u"Planet Carrier", None))
        self.cb_output_GD.setItemText(2, QCoreApplication.translate("MainForm", u"Ring", None))

        self.cb_output_GD.setPlaceholderText(QCoreApplication.translate("MainForm", u"- Select -", None))
        self.lb_input_2.setText(QCoreApplication.translate("MainForm", u"Input", None))
        self.lb_stationary_2.setText(QCoreApplication.translate("MainForm", u"Stationary", None))
        self.lb_stationGear2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_output_2.setText(QCoreApplication.translate("MainForm", u"Output", None))
        self.cb_input_GD.setItemText(0, QCoreApplication.translate("MainForm", u"Sun", None))
        self.cb_input_GD.setItemText(1, QCoreApplication.translate("MainForm", u"Planet Carrier", None))
        self.cb_input_GD.setItemText(2, QCoreApplication.translate("MainForm", u"Ring", None))

        self.cb_input_GD.setCurrentText("")
        self.cb_input_GD.setPlaceholderText(QCoreApplication.translate("MainForm", u"- Select -", None))
        self.label_10.setText(QCoreApplication.translate("MainForm", u"Gear Dimensions", None))
        self.lb_Rr3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_CD_bkl1.setText("")
        self.le_CD_bkl1.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_Rr2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_N1.setText("")
        self.le_N1.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_Rtip3.setText("")
        self.le_Rtip3.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Romax_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_Romax2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_Ro2.setText("")
        self.le_Ro2.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_bkl2.setText("")
        self.le_bkl2.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_Rf3.setText("")
        self.le_Rf3.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Roe2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_47.setText(QCoreApplication.translate("MainForm", u"Tooth Thickness", None))
        self.lb_Rp_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_Rtipmax_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.label_50.setText(QCoreApplication.translate("MainForm", u"Pitch Radius", None))
        self.lb_tt_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.le_Rf1.setText("")
        self.le_Rf1.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Rr_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.le_Ro3.setText("")
        self.le_Ro3.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_66.setText(QCoreApplication.translate("MainForm", u"Standard Root Radius", None))
        self.lb_CR2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_55.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_N3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Roe3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Ro_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_Roe1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_22.setText(QCoreApplication.translate("MainForm", u"Teeth", None))
        self.lb_Romax3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Rf_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_Rrs1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_Rf2.setText("")
        self.le_Rf2.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Rrs2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Rff1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_20.setText(QCoreApplication.translate("MainForm", u"Module", None))
        self.le_NPlanets.setText("")
        self.le_NPlanets.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Rf.setText(QCoreApplication.translate("MainForm", u"Root Fillet", None))
        self.le_Rtip2.setText("")
        self.le_Rtip2.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_GR.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_60.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_Rrim.setText("")
        self.le_Rrim.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_tt3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_CD_text.setText(QCoreApplication.translate("MainForm", u"Center Distance", None))
        self.lb_max_planets_text.setText(QCoreApplication.translate("MainForm", u"Max Planets", None))
        self.le_N2.setText("")
        self.le_N2.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_6.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Rrs3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Rtipmax2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_rtcl3.setText("")
        self.le_rtcl3.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_14.setText(QCoreApplication.translate("MainForm", u"Max Tip Fillet", None))
        self.lb_Rtipmax3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_CD_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_tts3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_NPlanets_text.setText(QCoreApplication.translate("MainForm", u"Number of Planets", None))
        self.le_x3.setText("")
        self.le_x3.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Rff3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Ros3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_undercut3.setText("")
        self.le_rtcl2.setText("")
        self.le_rtcl2.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_tts2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_59.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_tt1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_13.setText(QCoreApplication.translate("MainForm", u"Max Outer Radius", None))
        self.lb_Rrs_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_rtcl_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_bkl_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_undercut2.setText("")
        self.label_16.setText(QCoreApplication.translate("MainForm", u"Root Clearance", None))
        self.label_29.setText(QCoreApplication.translate("MainForm", u"deg", None))
        self.lb_CD_bkl_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_Rs3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_max_planets.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_mod_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_CD_value.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_Ro1.setText("")
        self.le_Ro1.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_PA_deg.setText("")
        self.le_PA_deg.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_24.setText(QCoreApplication.translate("MainForm", u"Common", None))
        self.lb_Rs1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Rtipmax1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_tts1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_32.setText(QCoreApplication.translate("MainForm", u"Standard Outer Radius", None))
        self.lb_Romax1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_12.setText(QCoreApplication.translate("MainForm", u"Profile Shift Coefficient", None))
        self.lb_Rrim_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_Roe_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_CR1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.cb_CD_bkl.setItemText(0, QCoreApplication.translate("MainForm", u"Backlash", None))
        self.cb_CD_bkl.setItemText(1, QCoreApplication.translate("MainForm", u"Center Distance", None))

        self.cb_CD_bkl.setCurrentText(QCoreApplication.translate("MainForm", u"Backlash", None))
        self.label_40.setText(QCoreApplication.translate("MainForm", u"Max Root Fillet", None))
        self.lb_G2.setText(QCoreApplication.translate("MainForm", u"Gear 2", None))
        self.lb_Rs_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_G3.setText(QCoreApplication.translate("MainForm", u"Gear 3", None))
        self.lb_Rff_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_Rr1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Rff2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_bkl_value.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Rrim_text.setText(QCoreApplication.translate("MainForm", u"Rim Radius", None))
        self.lb_Ros1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Rp1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_undercut1.setText("")
        self.lb_Rs2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_46.setText(QCoreApplication.translate("MainForm", u"Root Radius", None))
        self.label_18.setText(QCoreApplication.translate("MainForm", u"Pressure Angle", None))
        self.lb_bkl2_text.setText(QCoreApplication.translate("MainForm", u"Backlash, Planet-Ring", None))
        self.lb_bkl2_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_Ros_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.label_30.setText(QCoreApplication.translate("MainForm", u"Outer Radius", None))
        self.lb_Rp3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_x2.setText("")
        self.le_x2.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_34.setText(QCoreApplication.translate("MainForm", u"Tip Fillet", None))
        self.label_54.setText(QCoreApplication.translate("MainForm", u"Contact Ratio", None))
        self.lb_tt2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_tts_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.label_43.setText(QCoreApplication.translate("MainForm", u"Standard Pitch Radius", None))
        self.le_mod.setText("")
        self.le_mod.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Ros2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_rtcl1.setText("")
        self.le_rtcl1.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_G1.setText(QCoreApplication.translate("MainForm", u"Gear 1", None))
        self.label_49.setText(QCoreApplication.translate("MainForm", u"Effective Outer Radius", None))
        self.label_52.setText(QCoreApplication.translate("MainForm", u"Standard Tooth Thickness", None))
        self.label_58.setText(QCoreApplication.translate("MainForm", u"Gear Ratio", None))
        self.le_x1.setText("")
        self.le_x1.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_Rtip1.setText("")
        self.le_Rtip1.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_Rp2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_bkl_text.setText(QCoreApplication.translate("MainForm", u"Backlash", None))
        self.lb_Rtip_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_spacing_text.setText(QCoreApplication.translate("MainForm", u"Evenly Spaced?", None))
        self.lb_icon_spacing.setText("")
        self.pb_drawGear.setText(QCoreApplication.translate("MainForm", u"Draw Gears", None))
        self.cb_singleViewG1.setText(QCoreApplication.translate("MainForm", u"Single Tooth View", None))
        self.cb_circlesG1.setText(QCoreApplication.translate("MainForm", u"Show Circles", None))
        self.tabW_GD.setTabText(self.tabW_GD.indexOf(self.tab_G1), QCoreApplication.translate("MainForm", u"Gear 1", None))
        self.cb_singleViewG3.setText(QCoreApplication.translate("MainForm", u"Single Tooth View", None))
        self.cb_circlesG3.setText(QCoreApplication.translate("MainForm", u"Show Circles", None))
        self.tabW_GD.setTabText(self.tabW_GD.indexOf(self.tab_G3), QCoreApplication.translate("MainForm", u"Gear 3", None))
        self.cb_singleViewG2.setText(QCoreApplication.translate("MainForm", u"Single Tooth View", None))
        self.cb_circlesG2.setText(QCoreApplication.translate("MainForm", u"Show Circles", None))
        self.tabW_GD.setTabText(self.tabW_GD.indexOf(self.tab_G2), QCoreApplication.translate("MainForm", u"Gear 2", None))
        self.label.setText(QCoreApplication.translate("MainForm", u"Rotate", None))
        self.cb_singleViewMesh.setText(QCoreApplication.translate("MainForm", u"Mesh View", None))
        self.rb_sp.setText(QCoreApplication.translate("MainForm", u"Sun-Planet", None))
        self.rb_pr.setText(QCoreApplication.translate("MainForm", u"Planet-Ring", None))
        self.cb_circlesMesh.setText(QCoreApplication.translate("MainForm", u"Show Circles", None))
        self.cb_LoC.setText(QCoreApplication.translate("MainForm", u"Show Line of Contact", None))
        self.pb_animate.setText(QCoreApplication.translate("MainForm", u"Animate", None))
        self.tabW_GD.setTabText(self.tabW_GD.indexOf(self.tab_Mesh), QCoreApplication.translate("MainForm", u"Mesh", None))
        self.tabW_main.setTabText(self.tabW_main.indexOf(self.tab_GD), QCoreApplication.translate("MainForm", u"Gear Designer", None))
        self.label_8.setText(QCoreApplication.translate("MainForm", u"Stress Analysis", None))
        self.label_62.setText(QCoreApplication.translate("MainForm", u"RPM", None))
        self.lb_torque_unit.setText(QCoreApplication.translate("MainForm", u"Nmm", None))
        self.label_64.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_FW1.setText("")
        self.le_FW1.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_85.setText(QCoreApplication.translate("MainForm", u"Pinion Speed", None))
        self.lb_stressC_unit.setText(QCoreApplication.translate("MainForm", u"Mpa", None))
        self.le_FW2.setText("")
        self.le_FW2.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_FW_unit.setText(QCoreApplication.translate("MainForm", u"mm", None))
        self.lb_stressG3.setText(QCoreApplication.translate("MainForm", u"Gear 3", None))
        self.le_nu2.setText("")
        self.le_nu2.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_E_unit.setText(QCoreApplication.translate("MainForm", u"MPa", None))
        self.le_nu3.setText("")
        self.le_nu3.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_E1.setText("")
        self.le_E1.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_pitchLineVel.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_78.setText(QCoreApplication.translate("MainForm", u"Contact Stress", None))
        self.label_86.setText(QCoreApplication.translate("MainForm", u"Young's Modulus", None))
        self.lb_stressB1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_stressG1.setText(QCoreApplication.translate("MainForm", u"Gear 1", None))
        self.lb_stressG2.setText(QCoreApplication.translate("MainForm", u"Gear 2", None))
        self.le_RPM.setText("")
        self.le_RPM.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_83.setText(QCoreApplication.translate("MainForm", u"Face Width", None))
        self.le_nu1.setText("")
        self.le_nu1.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_E3.setText("")
        self.le_E3.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_stressC1.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_76.setText(QCoreApplication.translate("MainForm", u"Bending Stress", None))
        self.label_80.setText(QCoreApplication.translate("MainForm", u"Pitch Line Velocity", None))
        self.lb_stressB3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.lb_stressC3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_torque.setText("")
        self.le_torque.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_87.setText(QCoreApplication.translate("MainForm", u"Poisson's Ratio", None))
        self.lb_pitchLineVel_unit.setText(QCoreApplication.translate("MainForm", u"m/s", None))
        self.lb_stressB_unit.setText(QCoreApplication.translate("MainForm", u"Mpa", None))
        self.lb_stressB2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_E2.setText("")
        self.le_E2.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.le_FW3.setText("")
        self.le_FW3.setPlaceholderText(QCoreApplication.translate("MainForm", u"-", None))
        self.label_84.setText(QCoreApplication.translate("MainForm", u"Pinion Torque", None))
        self.lb_stressC2.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pb_stress.setText(QCoreApplication.translate("MainForm", u"Calculate Stress", None))
        self.tabW_stress.setTabText(self.tabW_stress.indexOf(self.tab_stress1), QCoreApplication.translate("MainForm", u"Gear 1", None))
        self.tabW_stress.setTabText(self.tabW_stress.indexOf(self.tab_stress2), QCoreApplication.translate("MainForm", u"Gear 2", None))
        self.tabW_main.setTabText(self.tabW_main.indexOf(self.tab_stress), QCoreApplication.translate("MainForm", u"Stress", None))
    # retranslateUi

