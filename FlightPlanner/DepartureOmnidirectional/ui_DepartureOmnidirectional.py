# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DepartureOmnidirectional.ui'
#
# Created: Tue Oct 27 15:50:57 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DepartureOmnidirectional(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(509, 368)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gbRunway = QtGui.QGroupBox(Form)
        self.gbRunway.setObjectName(_fromUtf8("gbRunway"))
        self.vl_gbRunway = QtGui.QVBoxLayout(self.gbRunway)
        self.vl_gbRunway.setObjectName(_fromUtf8("vl_gbRunway"))
        self.verticalLayout.addWidget(self.gbRunway)
        self.gbParameters = QtGui.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.gbParameters.setFont(font)
        self.gbParameters.setObjectName(_fromUtf8("gbParameters"))
        self.vl_gbParameters = QtGui.QVBoxLayout(self.gbParameters)
        self.vl_gbParameters.setObjectName(_fromUtf8("vl_gbParameters"))
        self.frameSelectionMode = QtGui.QFrame(self.gbParameters)
        self.frameSelectionMode.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameSelectionMode.setFrameShadow(QtGui.QFrame.Raised)
        self.frameSelectionMode.setObjectName(_fromUtf8("frameSelectionMode"))
        self.hLayoutSelectionMode = QtGui.QHBoxLayout(self.frameSelectionMode)
        self.hLayoutSelectionMode.setSpacing(0)
        self.hLayoutSelectionMode.setMargin(0)
        self.hLayoutSelectionMode.setObjectName(_fromUtf8("hLayoutSelectionMode"))
        self.label_66 = QtGui.QLabel(self.frameSelectionMode)
        self.label_66.setMinimumSize(QtCore.QSize(180, 0))
        self.label_66.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_66.setFont(font)
        self.label_66.setObjectName(_fromUtf8("label_66"))
        self.hLayoutSelectionMode.addWidget(self.label_66)
        self.cmbSelectionMode = QtGui.QComboBox(self.frameSelectionMode)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbSelectionMode.sizePolicy().hasHeightForWidth())
        self.cmbSelectionMode.setSizePolicy(sizePolicy)
        self.cmbSelectionMode.setMinimumSize(QtCore.QSize(70, 0))
        self.cmbSelectionMode.setMaximumSize(QtCore.QSize(70, 12121))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cmbSelectionMode.setFont(font)
        self.cmbSelectionMode.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.cmbSelectionMode.setObjectName(_fromUtf8("cmbSelectionMode"))
        self.hLayoutSelectionMode.addWidget(self.cmbSelectionMode)
        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hLayoutSelectionMode.addItem(horizontalSpacer)
        self.vl_gbParameters.addWidget(self.frameSelectionMode)
        self.frameMinTurnHeight = QtGui.QFrame(self.gbParameters)
        self.frameMinTurnHeight.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameMinTurnHeight.setFrameShadow(QtGui.QFrame.Raised)
        self.frameMinTurnHeight.setObjectName(_fromUtf8("frameMinTurnHeight"))
        self.horizontalLayout_70 = QtGui.QHBoxLayout(self.frameMinTurnHeight)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setMargin(0)
        self.horizontalLayout_70.setObjectName(_fromUtf8("horizontalLayout_70"))
        self.label_78 = QtGui.QLabel(self.frameMinTurnHeight)
        self.label_78.setMinimumSize(QtCore.QSize(180, 0))
        self.label_78.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_78.setFont(font)
        self.label_78.setObjectName(_fromUtf8("label_78"))
        self.horizontalLayout_70.addWidget(self.label_78)
        self.txtMinTurnHeight = QtGui.QLineEdit(self.frameMinTurnHeight)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtMinTurnHeight.setFont(font)
        self.txtMinTurnHeight.setObjectName(_fromUtf8("txtMinTurnHeight"))
        self.txtMinTurnHeight.setMinimumSize(QtCore.QSize(90, 0))
        self.txtMinTurnHeight.setMaximumSize(QtCore.QSize(90, 12121))
        self.horizontalLayout_70.addWidget(self.txtMinTurnHeight)
        self.label_7 = QtGui.QLabel(self.frameMinTurnHeight)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_70.addWidget(self.label_7)
        self.txtMinTurnHeightFt = QtGui.QLineEdit(self.frameMinTurnHeight)
        self.txtMinTurnHeightFt.setObjectName(_fromUtf8("txtMinTurnHeightFt"))
        self.txtMinTurnHeightFt.setMinimumSize(QtCore.QSize(90, 0))
        self.txtMinTurnHeightFt.setMaximumSize(QtCore.QSize(90, 12121))
        self.horizontalLayout_70.addWidget(self.txtMinTurnHeightFt)
        self.label_8 = QtGui.QLabel(self.frameMinTurnHeight)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_70.addWidget(self.label_8)
        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_70.addItem(horizontalSpacer)
        self.vl_gbParameters.addWidget(self.frameMinTurnHeight)
        self.frameMinTurnHeight_CATH = QtGui.QFrame(self.gbParameters)
        self.frameMinTurnHeight_CATH.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameMinTurnHeight_CATH.setFrameShadow(QtGui.QFrame.Raised)
        self.frameMinTurnHeight_CATH.setObjectName(_fromUtf8("frameMinTurnHeight_CATH"))
        self.horizontalLayout_73 = QtGui.QHBoxLayout(self.frameMinTurnHeight_CATH)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setMargin(0)
        self.horizontalLayout_73.setObjectName(_fromUtf8("horizontalLayout_73"))
        self.label_81 = QtGui.QLabel(self.frameMinTurnHeight_CATH)
        self.label_81.setMinimumSize(QtCore.QSize(180, 0))
        self.label_81.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_81.setFont(font)
        self.label_81.setObjectName(_fromUtf8("label_81"))
        self.horizontalLayout_73.addWidget(self.label_81)
        self.txtMinTurnHeight_CATH = QtGui.QLineEdit(self.frameMinTurnHeight_CATH)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtMinTurnHeight_CATH.setFont(font)
        self.txtMinTurnHeight_CATH.setObjectName(_fromUtf8("txtMinTurnHeight_CATH"))
        self.txtMinTurnHeight_CATH.setMinimumSize(QtCore.QSize(90, 0))
        self.txtMinTurnHeight_CATH.setMaximumSize(QtCore.QSize(90, 12121))
        self.horizontalLayout_73.addWidget(self.txtMinTurnHeight_CATH)
        self.label_9 = QtGui.QLabel(self.frameMinTurnHeight_CATH)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_73.addWidget(self.label_9)
        self.txtMinTurnHeight_CATH_2 = QtGui.QLineEdit(self.frameMinTurnHeight_CATH)
        self.txtMinTurnHeight_CATH_2.setObjectName(_fromUtf8("txtMinTurnHeight_CATH_2"))
        self.txtMinTurnHeight_CATH_2.setMinimumSize(QtCore.QSize(90, 0))
        self.txtMinTurnHeight_CATH_2.setMaximumSize(QtCore.QSize(90, 12121))
        self.horizontalLayout_73.addWidget(self.txtMinTurnHeight_CATH_2)
        self.label_10 = QtGui.QLabel(self.frameMinTurnHeight_CATH)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_73.addWidget(self.label_10)
        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_73.addItem(horizontalSpacer)
        self.vl_gbParameters.addWidget(self.frameMinTurnHeight_CATH)
        self.frameTurningAltitude = QtGui.QFrame(self.gbParameters)
        self.frameTurningAltitude.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameTurningAltitude.setFrameShadow(QtGui.QFrame.Raised)
        self.frameTurningAltitude.setObjectName(_fromUtf8("frameTurningAltitude"))
        self.hLayoutTurningAltitude = QtGui.QHBoxLayout(self.frameTurningAltitude)
        self.hLayoutTurningAltitude.setSpacing(0)
        self.hLayoutTurningAltitude.setMargin(0)
        self.hLayoutTurningAltitude.setObjectName(_fromUtf8("hLayoutTurningAltitude"))
        self.label_79 = QtGui.QLabel(self.frameTurningAltitude)
        self.label_79.setMinimumSize(QtCore.QSize(180, 0))
        self.label_79.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_79.setFont(font)
        self.label_79.setObjectName(_fromUtf8("label_79"))
        self.hLayoutTurningAltitude.addWidget(self.label_79)
        self.txtTurningAltitudeM = QtGui.QLineEdit(self.frameTurningAltitude)
        self.txtTurningAltitudeM.setObjectName(_fromUtf8("txtTurningAltitudeM"))
        self.txtTurningAltitudeM.setMinimumSize(QtCore.QSize(90, 0))
        self.txtTurningAltitudeM.setMaximumSize(QtCore.QSize(90, 12121))
        self.hLayoutTurningAltitude.addWidget(self.txtTurningAltitudeM)
        self.label = QtGui.QLabel(self.frameTurningAltitude)
        self.label.setObjectName(_fromUtf8("label"))
        self.hLayoutTurningAltitude.addWidget(self.label)
        self.txtTurningAltitude = QtGui.QLineEdit(self.frameTurningAltitude)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtTurningAltitude.setFont(font)
        self.txtTurningAltitude.setObjectName(_fromUtf8("txtTurningAltitude"))
        self.txtTurningAltitude.setMinimumSize(QtCore.QSize(90, 0))
        self.txtTurningAltitude.setMaximumSize(QtCore.QSize(90, 12121))
        self.hLayoutTurningAltitude.addWidget(self.txtTurningAltitude)
        self.label_2 = QtGui.QLabel(self.frameTurningAltitude)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.hLayoutTurningAltitude.addWidget(self.label_2)
        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hLayoutTurningAltitude.addItem(horizontalSpacer)
        self.vl_gbParameters.addWidget(self.frameTurningAltitude)
        self.frameNextSegmentAltitude = QtGui.QFrame(self.gbParameters)
        self.frameNextSegmentAltitude.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameNextSegmentAltitude.setFrameShadow(QtGui.QFrame.Raised)
        self.frameNextSegmentAltitude.setObjectName(_fromUtf8("frameNextSegmentAltitude"))
        self.horizontalLayout_72 = QtGui.QHBoxLayout(self.frameNextSegmentAltitude)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setMargin(0)
        self.horizontalLayout_72.setObjectName(_fromUtf8("horizontalLayout_72"))
        self.label_80 = QtGui.QLabel(self.frameNextSegmentAltitude)
        self.label_80.setMinimumSize(QtCore.QSize(180, 0))
        self.label_80.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_80.setFont(font)
        self.label_80.setObjectName(_fromUtf8("label_80"))
        self.horizontalLayout_72.addWidget(self.label_80)
        self.txtNextSegmentAltitudeM = QtGui.QLineEdit(self.frameNextSegmentAltitude)
        self.txtNextSegmentAltitudeM.setObjectName(_fromUtf8("txtNextSegmentAltitudeM"))
        self.txtNextSegmentAltitudeM.setMinimumSize(QtCore.QSize(90, 0))
        self.txtNextSegmentAltitudeM.setMaximumSize(QtCore.QSize(90, 12121))
        self.horizontalLayout_72.addWidget(self.txtNextSegmentAltitudeM)
        self.label_3 = QtGui.QLabel(self.frameNextSegmentAltitude)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_72.addWidget(self.label_3)
        self.txtNextSegmentAltitude = QtGui.QLineEdit(self.frameNextSegmentAltitude)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtNextSegmentAltitude.setFont(font)
        self.txtNextSegmentAltitude.setObjectName(_fromUtf8("txtNextSegmentAltitude"))
        self.txtNextSegmentAltitude.setMinimumSize(QtCore.QSize(90, 0))
        self.txtNextSegmentAltitude.setMaximumSize(QtCore.QSize(90, 12121))
        self.horizontalLayout_72.addWidget(self.txtNextSegmentAltitude)
        self.label_4 = QtGui.QLabel(self.frameNextSegmentAltitude)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_72.addWidget(self.label_4)
        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_72.addItem(horizontalSpacer)
        self.vl_gbParameters.addWidget(self.frameNextSegmentAltitude)
        self.frameMOC = QtGui.QFrame(self.gbParameters)
        self.frameMOC.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameMOC.setFrameShadow(QtGui.QFrame.Raised)
        self.frameMOC.setObjectName(_fromUtf8("frameMOC"))
        self.horizontalLayout_69 = QtGui.QHBoxLayout(self.frameMOC)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setMargin(0)
        self.horizontalLayout_69.setObjectName(_fromUtf8("horizontalLayout_69"))
        self.label_77 = QtGui.QLabel(self.frameMOC)
        self.label_77.setMinimumSize(QtCore.QSize(180, 0))
        self.label_77.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_77.setFont(font)
        self.label_77.setObjectName(_fromUtf8("label_77"))
        self.horizontalLayout_69.addWidget(self.label_77)
        self.txtMoc = QtGui.QLineEdit(self.frameMOC)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtMoc.setFont(font)
        self.txtMoc.setObjectName(_fromUtf8("txtMoc"))
        self.txtMoc.setMinimumSize(QtCore.QSize(60, 0))
        self.txtMoc.setMaximumSize(QtCore.QSize(60, 12121))
        self.horizontalLayout_69.addWidget(self.txtMoc)
        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_69.addItem(horizontalSpacer)
        self.vl_gbParameters.addWidget(self.frameMOC)
        self.framePDG = QtGui.QFrame(self.gbParameters)
        self.framePDG.setFrameShape(QtGui.QFrame.NoFrame)
        self.framePDG.setFrameShadow(QtGui.QFrame.Raised)
        self.framePDG.setObjectName(_fromUtf8("framePDG"))
        self.horizontalLayout_60 = QtGui.QHBoxLayout(self.framePDG)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setMargin(0)
        self.horizontalLayout_60.setObjectName(_fromUtf8("horizontalLayout_60"))
        self.label_68 = QtGui.QLabel(self.framePDG)
        self.label_68.setMinimumSize(QtCore.QSize(180, 0))
        self.label_68.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_68.setFont(font)
        self.label_68.setObjectName(_fromUtf8("label_68"))
        self.horizontalLayout_60.addWidget(self.label_68)
        self.txtPdg = QtGui.QLineEdit(self.framePDG)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtPdg.setFont(font)
        self.txtPdg.setObjectName(_fromUtf8("txtPdg"))
        self.txtPdg.setMinimumSize(QtCore.QSize(60, 0))
        self.txtPdg.setMaximumSize(QtCore.QSize(60, 12121))
        self.horizontalLayout_60.addWidget(self.txtPdg)
        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_60.addItem(horizontalSpacer)
        self.vl_gbParameters.addWidget(self.framePDG)
        self.frameNextSegmentAltitude_2 = QtGui.QFrame(self.gbParameters)
        self.frameNextSegmentAltitude_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameNextSegmentAltitude_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frameNextSegmentAltitude_2.setObjectName(_fromUtf8("frameNextSegmentAltitude_2"))
        self.horizontalLayout_74 = QtGui.QHBoxLayout(self.frameNextSegmentAltitude_2)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setMargin(0)
        self.horizontalLayout_74.setObjectName(_fromUtf8("horizontalLayout_74"))
        self.label_82 = QtGui.QLabel(self.frameNextSegmentAltitude_2)
        self.label_82.setMinimumSize(QtCore.QSize(180, 0))
        self.label_82.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_82.setFont(font)
        self.label_82.setObjectName(_fromUtf8("label_82"))
        self.horizontalLayout_74.addWidget(self.label_82)
        self.txtRadius = QtGui.QLineEdit(self.frameNextSegmentAltitude_2)
        self.txtRadius.setObjectName(_fromUtf8("txtRadius"))
        self.txtRadius.setMinimumSize(QtCore.QSize(90, 0))
        self.txtRadius.setMaximumSize(QtCore.QSize(90, 12121))
        self.horizontalLayout_74.addWidget(self.txtRadius)
        self.label_5 = QtGui.QLabel(self.frameNextSegmentAltitude_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_74.addWidget(self.label_5)
        self.txtRadiusFt = QtGui.QLineEdit(self.frameNextSegmentAltitude_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtRadiusFt.setFont(font)
        self.txtRadiusFt.setText(_fromUtf8(""))
        self.txtRadiusFt.setObjectName(_fromUtf8("txtRadiusFt"))
        self.txtRadiusFt.setMinimumSize(QtCore.QSize(90, 0))
        self.txtRadiusFt.setMaximumSize(QtCore.QSize(90, 12121))
        self.horizontalLayout_74.addWidget(self.txtRadiusFt)
        self.label_6 = QtGui.QLabel(self.frameNextSegmentAltitude_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_74.addWidget(self.label_6)
        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_74.addItem(horizontalSpacer)
        self.vl_gbParameters.addWidget(self.frameNextSegmentAltitude_2)
        self.frameMOCmultipiler = QtGui.QFrame(self.gbParameters)
        self.frameMOCmultipiler.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameMOCmultipiler.setFrameShadow(QtGui.QFrame.Raised)
        self.frameMOCmultipiler.setObjectName(_fromUtf8("frameMOCmultipiler"))
        self.horizontalLayout_76 = QtGui.QHBoxLayout(self.frameMOCmultipiler)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setMargin(0)
        self.horizontalLayout_76.setObjectName(_fromUtf8("horizontalLayout_76"))
        self.label_84 = QtGui.QLabel(self.frameMOCmultipiler)
        self.label_84.setMinimumSize(QtCore.QSize(180, 0))
        self.label_84.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_84.setFont(font)
        self.label_84.setObjectName(_fromUtf8("label_84"))
        self.horizontalLayout_76.addWidget(self.label_84)
        self.mocSpinBox = QtGui.QSpinBox(self.frameMOCmultipiler)
        self.mocSpinBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mocSpinBox.sizePolicy().hasHeightForWidth())
        self.mocSpinBox.setSizePolicy(sizePolicy)
        self.mocSpinBox.setMinimumSize(QtCore.QSize(66, 0))
        self.mocSpinBox.setMinimum(1)
        self.mocSpinBox.setObjectName(_fromUtf8("mocSpinBox"))
        self.mocSpinBox.setMinimumSize(QtCore.QSize(60, 0))
        self.mocSpinBox.setMaximumSize(QtCore.QSize(60, 12121))
        self.horizontalLayout_76.addWidget(self.mocSpinBox)
        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_76.addItem(horizontalSpacer)
        self.vl_gbParameters.addWidget(self.frameMOCmultipiler)
        self.chbTurnsBeforeDer = QtGui.QCheckBox(self.gbParameters)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.chbTurnsBeforeDer.setFont(font)
        self.chbTurnsBeforeDer.setObjectName(_fromUtf8("chbTurnsBeforeDer"))
        self.vl_gbParameters.addWidget(self.chbTurnsBeforeDer)
        self.chbCatH = QtGui.QCheckBox(self.gbParameters)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.chbCatH.setFont(font)
        self.chbCatH.setObjectName(_fromUtf8("chbCatH"))
        self.vl_gbParameters.addWidget(self.chbCatH)
        self.verticalLayout.addWidget(self.gbParameters)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.gbRunway.setTitle(_translate("Form", "Runway", None))
        self.gbParameters.setTitle(_translate("Form", "Parameters", None))
        self.label_66.setText(_translate("Form", "Selection Mode:", None))
        self.label_78.setText(_translate("Form", "Minimum Turn Height(m):", None))
        self.txtMinTurnHeight.setText(_translate("Form", "120", None))
        self.label_7.setText(_translate("Form", "m", None))
        self.label_8.setText(_translate("Form", "ft", None))
        self.label_81.setText(_translate("Form", "Minimum Turn Height(m):", None))
        self.txtMinTurnHeight_CATH.setText(_translate("Form", "120", None))
        self.label_9.setText(_translate("Form", "m", None))
        self.label_10.setText(_translate("Form", "ft", None))
        self.label_79.setText(_translate("Form", "Turning Altitude(ft):", None))
        self.label.setText(_translate("Form", "m", None))
        self.txtTurningAltitude.setText(_translate("Form", "3000", None))
        self.label_2.setText(_translate("Form", "ft", None))
        self.label_80.setText(_translate("Form", "Next Segment Altitude/MSA:", None))
        self.label_3.setText(_translate("Form", "m", None))
        self.txtNextSegmentAltitude.setText(_translate("Form", "6000", None))
        self.label_4.setText(_translate("Form", "ft", None))
        self.label_77.setText(_translate("Form", "MOC(%):", None))
        self.txtMoc.setText(_translate("Form", "0.8", None))
        self.label_68.setText(_translate("Form", "PDG(%):", None))
        self.txtPdg.setText(_translate("Form", "3.3", None))
        self.label_82.setText(_translate("Form", "Radius for the Area3:", None))
        self.label_5.setText(_translate("Form", "m", None))
        self.label_6.setText(_translate("Form", "nm", None))
        self.label_84.setText(_translate("Form", "MOCmultiplier:", None))
        self.chbTurnsBeforeDer.setText(_translate("Form", "Allow turns before DER", None))
        self.chbCatH.setText(_translate("Form", "Cat. H", None))

