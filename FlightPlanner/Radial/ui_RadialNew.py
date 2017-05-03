# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Radial.ui'
#
# Created: Sun Jan 17 10:58:00 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from FlightPlanner.Panels.TrackRadialBoxPanel import TrackRadialBoxPanel
from FlightPlanner.Panels.ComboBoxPanel import ComboBoxPanel

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

class Ui_Radial(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(512, 434)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.gbNavAid = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbNavAid.sizePolicy().hasHeightForWidth())
        self.gbNavAid.setSizePolicy(sizePolicy)
        self.gbNavAid.setObjectName(_fromUtf8("gbNavAid"))
        self.vl_gbNavAid = QtGui.QVBoxLayout(self.gbNavAid)
        self.vl_gbNavAid.setObjectName(_fromUtf8("vl_gbNavAid"))


        self.cmbNavAidType = ComboBoxPanel(self.gbNavAid)
        self.cmbNavAidType.Caption = "Type"
        self.cmbNavAidType.LabelWidth = 120
        self.vl_gbNavAid.addWidget(self.cmbNavAidType)

        self.cmbBasedOn = ComboBoxPanel(self.gbNavAid, True)
        self.cmbBasedOn.Caption = "Based On"
        self.cmbBasedOn.LabelWidth = 120
        self.cmbBasedOn.Width = 120
        self.vl_gbNavAid.addWidget(self.cmbBasedOn)
        # self.frameNavAidType = QtGui.QFrame(self.gbNavAid)
        # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frameNavAidType.sizePolicy().hasHeightForWidth())
        # self.frameNavAidType.setSizePolicy(sizePolicy)
        # self.frameNavAidType.setFrameShape(QtGui.QFrame.NoFrame)
        # self.frameNavAidType.setFrameShadow(QtGui.QFrame.Raised)
        # self.frameNavAidType.setObjectName(_fromUtf8("frameNavAidType"))
        # self.hlNavAidType = QtGui.QHBoxLayout(self.frameNavAidType)
        # self.hlNavAidType.setSpacing(0)
        # self.hlNavAidType.setMargin(0)
        # self.hlNavAidType.setObjectName(_fromUtf8("hlNavAidType"))
        # self.label_67 = QtGui.QLabel(self.frameNavAidType)
        # self.label_67.setMinimumSize(QtCore.QSize(180, 0))
        # self.label_67.setMaximumSize(QtCore.QSize(180, 16777215))
        # font = QtGui.QFont()
        # font.setBold(False)
        # font.setWeight(50)
        # self.label_67.setFont(font)
        # self.label_67.setObjectName(_fromUtf8("label_67"))
        # self.hlNavAidType.addWidget(self.label_67)
        # self.cmbNavAidType = QtGui.QComboBox(self.frameNavAidType)
        # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.cmbNavAidType.sizePolicy().hasHeightForWidth())
        # self.cmbNavAidType.setSizePolicy(sizePolicy)
        # self.cmbNavAidType.setMinimumSize(QtCore.QSize(66, 0))
        # font = QtGui.QFont()
        # font.setBold(False)
        # font.setWeight(50)
        # self.cmbNavAidType.setFont(font)
        # self.cmbNavAidType.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        # self.cmbNavAidType.setObjectName(_fromUtf8("cmbNavAidType"))
        # self.hlNavAidType.addWidget(self.cmbNavAidType)
        # self.vl_gbNavAid.addWidget(self.frameNavAidType)
        self.verticalLayout.addWidget(self.gbNavAid)
        self.gbParameters = QtGui.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.gbParameters.setFont(font)
        self.gbParameters.setObjectName(_fromUtf8("gbParameters"))
        self.vl_gbParameters = QtGui.QVBoxLayout(self.gbParameters)
        self.vl_gbParameters.setObjectName(_fromUtf8("vl_gbParameters"))

        self.txtTrackRadial = TrackRadialBoxPanel(self.gbParameters)
        self.txtTrackRadial.Caption = "Track"
        self.vl_gbParameters.addWidget(self.txtTrackRadial)
        # self.frameTrackRadial = QtGui.QFrame(self.gbParameters)
        # self.frameTrackRadial.setFrameShape(QtGui.QFrame.NoFrame)
        # self.frameTrackRadial.setFrameShadow(QtGui.QFrame.Raised)
        # self.frameTrackRadial.setObjectName(_fromUtf8("frameTrackRadial"))
        # self.hlTrackRadial = QtGui.QHBoxLayout(self.frameTrackRadial)
        # self.hlTrackRadial.setSpacing(0)
        # self.hlTrackRadial.setMargin(0)
        # self.hlTrackRadial.setObjectName(_fromUtf8("hlTrackRadial"))
        # self.label_74 = QtGui.QLabel(self.frameTrackRadial)
        # self.label_74.setMinimumSize(QtCore.QSize(180, 0))
        # self.label_74.setMaximumSize(QtCore.QSize(180, 16777215))
        # font = QtGui.QFont()
        # font.setBold(False)
        # font.setWeight(50)
        # self.label_74.setFont(font)
        # self.label_74.setObjectName(_fromUtf8("label_74"))
        # self.hlTrackRadial.addWidget(self.label_74)
        # self.frame_APV_9 = QtGui.QFrame(self.frameTrackRadial)
        # self.frame_APV_9.setFrameShape(QtGui.QFrame.StyledPanel)
        # self.frame_APV_9.setFrameShadow(QtGui.QFrame.Raised)
        # self.frame_APV_9.setObjectName(_fromUtf8("frame_APV_9"))
        # self.horizontalLayout_13 = QtGui.QHBoxLayout(self.frame_APV_9)
        # self.horizontalLayout_13.setSpacing(0)
        # self.horizontalLayout_13.setMargin(0)
        # self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        # self.txtTrackRadial = QtGui.QLineEdit(self.frame_APV_9)
        # self.txtTrackRadial.setEnabled(True)
        # font = QtGui.QFont()
        # font.setBold(False)
        # font.setWeight(50)
        # self.txtTrackRadial.setFont(font)
        # self.txtTrackRadial.setObjectName(_fromUtf8("txtTrackRadial"))
        # self.horizontalLayout_13.addWidget(self.txtTrackRadial)
        # self.btnCaptureTrackRadial = QtGui.QToolButton(self.frame_APV_9)
        # self.btnCaptureTrackRadial.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/coordinate_capture.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.btnCaptureTrackRadial.setIcon(icon)
        # self.btnCaptureTrackRadial.setObjectName(_fromUtf8("btnCaptureTrackRadial"))
        # self.horizontalLayout_13.addWidget(self.btnCaptureTrackRadial)
        # self.hlTrackRadial.addWidget(self.frame_APV_9)
        # self.vl_gbParameters.addWidget(self.frameTrackRadial)
        self.frameDistStart = QtGui.QFrame(self.gbParameters)
        self.frameDistStart.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameDistStart.setFrameShadow(QtGui.QFrame.Raised)
        self.frameDistStart.setObjectName(_fromUtf8("frameDistStart"))
        self.hlDistStart = QtGui.QHBoxLayout(self.frameDistStart)
        self.hlDistStart.setSpacing(0)
        self.hlDistStart.setMargin(0)
        self.hlDistStart.setObjectName(_fromUtf8("hlDistStart"))
        self.label_75 = QtGui.QLabel(self.frameDistStart)
        self.label_75.setMinimumSize(QtCore.QSize(180, 0))
        self.label_75.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_75.setFont(font)
        self.label_75.setObjectName(_fromUtf8("label_75"))
        self.hlDistStart.addWidget(self.label_75)
        self.frame_APV_10 = QtGui.QFrame(self.frameDistStart)
        self.frame_APV_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_APV_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_APV_10.setObjectName(_fromUtf8("frame_APV_10"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.frame_APV_10)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setMargin(0)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.txtDistStart = QtGui.QLineEdit(self.frame_APV_10)
        self.txtDistStart.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtDistStart.setFont(font)
        self.txtDistStart.setObjectName(_fromUtf8("txtDistStart"))
        self.horizontalLayout_14.addWidget(self.txtDistStart)
        self.btnCaptureDistStart = QtGui.QToolButton(self.frame_APV_10)
        self.btnCaptureDistStart.setText(_fromUtf8(""))
        self.btnCaptureDistStart.setIcon(icon)
        self.btnCaptureDistStart.setObjectName(_fromUtf8("btnCaptureDistStart"))
        self.horizontalLayout_14.addWidget(self.btnCaptureDistStart)
        self.hlDistStart.addWidget(self.frame_APV_10)
        self.vl_gbParameters.addWidget(self.frameDistStart)
        self.frameDistFinish = QtGui.QFrame(self.gbParameters)
        self.frameDistFinish.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameDistFinish.setFrameShadow(QtGui.QFrame.Raised)
        self.frameDistFinish.setObjectName(_fromUtf8("frameDistFinish"))
        self.hlDistFinish = QtGui.QHBoxLayout(self.frameDistFinish)
        self.hlDistFinish.setSpacing(0)
        self.hlDistFinish.setMargin(0)
        self.hlDistFinish.setObjectName(_fromUtf8("hlDistFinish"))
        self.label_76 = QtGui.QLabel(self.frameDistFinish)
        self.label_76.setMinimumSize(QtCore.QSize(180, 0))
        self.label_76.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_76.setFont(font)
        self.label_76.setObjectName(_fromUtf8("label_76"))
        self.hlDistFinish.addWidget(self.label_76)
        self.frame_APV_11 = QtGui.QFrame(self.frameDistFinish)
        self.frame_APV_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_APV_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_APV_11.setObjectName(_fromUtf8("frame_APV_11"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.frame_APV_11)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setMargin(0)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.txtDistFinish = QtGui.QLineEdit(self.frame_APV_11)
        self.txtDistFinish.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtDistFinish.setFont(font)
        self.txtDistFinish.setObjectName(_fromUtf8("txtDistFinish"))
        self.horizontalLayout_15.addWidget(self.txtDistFinish)
        self.btnCaptureDistFinish = QtGui.QToolButton(self.frame_APV_11)
        self.btnCaptureDistFinish.setText(_fromUtf8(""))
        self.btnCaptureDistFinish.setIcon(icon)
        self.btnCaptureDistFinish.setObjectName(_fromUtf8("btnCaptureDistFinish"))
        self.horizontalLayout_15.addWidget(self.btnCaptureDistFinish)
        self.hlDistFinish.addWidget(self.frame_APV_11)
        self.vl_gbParameters.addWidget(self.frameDistFinish)
        self.frameStartAltitude = QtGui.QFrame(self.gbParameters)
        self.frameStartAltitude.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameStartAltitude.setFrameShadow(QtGui.QFrame.Raised)
        self.frameStartAltitude.setObjectName(_fromUtf8("frameStartAltitude"))
        self.hlStartAltitude = QtGui.QHBoxLayout(self.frameStartAltitude)
        self.hlStartAltitude.setSpacing(0)
        self.hlStartAltitude.setMargin(0)
        self.hlStartAltitude.setObjectName(_fromUtf8("hlStartAltitude"))
        self.label_79 = QtGui.QLabel(self.frameStartAltitude)
        self.label_79.setMinimumSize(QtCore.QSize(180, 0))
        self.label_79.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_79.setFont(font)
        self.label_79.setObjectName(_fromUtf8("label_79"))
        self.hlStartAltitude.addWidget(self.label_79)
        self.frame_APV_14 = QtGui.QFrame(self.frameStartAltitude)
        self.frame_APV_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_APV_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_APV_14.setObjectName(_fromUtf8("frame_APV_14"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.frame_APV_14)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setMargin(0)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.txtStartAltitude = QtGui.QLineEdit(self.frame_APV_14)
        self.txtStartAltitude.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtStartAltitude.setFont(font)
        self.txtStartAltitude.setObjectName(_fromUtf8("txtStartAltitude"))
        self.horizontalLayout_18.addWidget(self.txtStartAltitude)
        self.hlStartAltitude.addWidget(self.frame_APV_14)
        self.vl_gbParameters.addWidget(self.frameStartAltitude)
        self.frameAltitudeChange = QtGui.QFrame(self.gbParameters)
        self.frameAltitudeChange.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameAltitudeChange.setFrameShadow(QtGui.QFrame.Raised)
        self.frameAltitudeChange.setObjectName(_fromUtf8("frameAltitudeChange"))
        self.hlAltitudeChange = QtGui.QHBoxLayout(self.frameAltitudeChange)
        self.hlAltitudeChange.setSpacing(0)
        self.hlAltitudeChange.setMargin(0)
        self.hlAltitudeChange.setObjectName(_fromUtf8("hlAltitudeChange"))
        self.label_77 = QtGui.QLabel(self.frameAltitudeChange)
        self.label_77.setMinimumSize(QtCore.QSize(180, 0))
        self.label_77.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_77.setFont(font)
        self.label_77.setObjectName(_fromUtf8("label_77"))
        self.hlAltitudeChange.addWidget(self.label_77)
        self.frame_APV_12 = QtGui.QFrame(self.frameAltitudeChange)
        self.frame_APV_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_APV_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_APV_12.setObjectName(_fromUtf8("frame_APV_12"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.frame_APV_12)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setMargin(0)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.txtAltitudeChange = QtGui.QLineEdit(self.frame_APV_12)
        self.txtAltitudeChange.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtAltitudeChange.setFont(font)
        self.txtAltitudeChange.setObjectName(_fromUtf8("txtAltitudeChange"))
        self.horizontalLayout_16.addWidget(self.txtAltitudeChange)
        self.hlAltitudeChange.addWidget(self.frame_APV_12)
        self.vl_gbParameters.addWidget(self.frameAltitudeChange)
        self.frameToleranceType = QtGui.QFrame(self.gbParameters)
        self.frameToleranceType.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameToleranceType.setFrameShadow(QtGui.QFrame.Raised)
        self.frameToleranceType.setObjectName(_fromUtf8("frameToleranceType"))
        self.hlToleranceType = QtGui.QHBoxLayout(self.frameToleranceType)
        self.hlToleranceType.setSpacing(0)
        self.hlToleranceType.setMargin(0)
        self.hlToleranceType.setObjectName(_fromUtf8("hlToleranceType"))
        self.label_66 = QtGui.QLabel(self.frameToleranceType)
        self.label_66.setMinimumSize(QtCore.QSize(180, 0))
        self.label_66.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_66.setFont(font)
        self.label_66.setObjectName(_fromUtf8("label_66"))
        self.hlToleranceType.addWidget(self.label_66)
        self.cmbToleranceType = QtGui.QComboBox(self.frameToleranceType)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbToleranceType.sizePolicy().hasHeightForWidth())
        self.cmbToleranceType.setSizePolicy(sizePolicy)
        self.cmbToleranceType.setMinimumSize(QtCore.QSize(66, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cmbToleranceType.setFont(font)
        self.cmbToleranceType.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.cmbToleranceType.setObjectName(_fromUtf8("cmbToleranceType"))
        self.hlToleranceType.addWidget(self.cmbToleranceType)
        self.vl_gbParameters.addWidget(self.frameToleranceType)
        self.frameSelectionMode = QtGui.QFrame(self.gbParameters)
        self.frameSelectionMode.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameSelectionMode.setFrameShadow(QtGui.QFrame.Raised)
        self.frameSelectionMode.setObjectName(_fromUtf8("frameSelectionMode"))
        self.hLayoutSelectionMode = QtGui.QHBoxLayout(self.frameSelectionMode)
        self.hLayoutSelectionMode.setSpacing(0)
        self.hLayoutSelectionMode.setMargin(0)
        self.hLayoutSelectionMode.setObjectName(_fromUtf8("hLayoutSelectionMode"))
        self.label_68 = QtGui.QLabel(self.frameSelectionMode)
        self.label_68.setMinimumSize(QtCore.QSize(180, 0))
        self.label_68.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_68.setFont(font)
        self.label_68.setObjectName(_fromUtf8("label_68"))
        self.hLayoutSelectionMode.addWidget(self.label_68)
        self.cmbSelectionMode = QtGui.QComboBox(self.frameSelectionMode)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbSelectionMode.sizePolicy().hasHeightForWidth())
        self.cmbSelectionMode.setSizePolicy(sizePolicy)
        self.cmbSelectionMode.setMinimumSize(QtCore.QSize(72, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cmbSelectionMode.setFont(font)
        self.cmbSelectionMode.setObjectName(_fromUtf8("cmbSelectionMode"))
        self.hLayoutSelectionMode.addWidget(self.cmbSelectionMode)
        self.vl_gbParameters.addWidget(self.frameSelectionMode)
        self.framePrimaryMoc = QtGui.QFrame(self.gbParameters)
        self.framePrimaryMoc.setFrameShape(QtGui.QFrame.NoFrame)
        self.framePrimaryMoc.setFrameShadow(QtGui.QFrame.Raised)
        self.framePrimaryMoc.setObjectName(_fromUtf8("framePrimaryMoc"))
        self.hLayoutPrimaryMoc = QtGui.QHBoxLayout(self.framePrimaryMoc)
        self.hLayoutPrimaryMoc.setSpacing(0)
        self.hLayoutPrimaryMoc.setMargin(0)
        self.hLayoutPrimaryMoc.setObjectName(_fromUtf8("hLayoutPrimaryMoc"))
        self.label_70 = QtGui.QLabel(self.framePrimaryMoc)
        self.label_70.setMinimumSize(QtCore.QSize(180, 0))
        self.label_70.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_70.setFont(font)
        self.label_70.setObjectName(_fromUtf8("label_70"))
        self.hLayoutPrimaryMoc.addWidget(self.label_70)
        self.txtPrimaryMOC = QtGui.QLineEdit(self.framePrimaryMoc)
        self.txtPrimaryMOC.setMinimumSize(QtCore.QSize(72, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtPrimaryMOC.setFont(font)
        self.txtPrimaryMOC.setObjectName(_fromUtf8("txtPrimaryMOC"))
        self.hLayoutPrimaryMoc.addWidget(self.txtPrimaryMOC)
        self.label_6 = QtGui.QLabel(self.framePrimaryMoc)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.hLayoutPrimaryMoc.addWidget(self.label_6)
        self.txtPrimaryMOCFt = QtGui.QLineEdit(self.framePrimaryMoc)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtPrimaryMOCFt.setFont(font)
        self.txtPrimaryMOCFt.setText(_fromUtf8(""))
        self.txtPrimaryMOCFt.setObjectName(_fromUtf8("txtPrimaryMOCFt"))
        self.hLayoutPrimaryMoc.addWidget(self.txtPrimaryMOCFt)
        self.labelMocFt = QtGui.QLabel(self.framePrimaryMoc)
        self.labelMocFt.setObjectName(_fromUtf8("labelMocFt"))
        self.hLayoutPrimaryMoc.addWidget(self.labelMocFt)
        self.vl_gbParameters.addWidget(self.framePrimaryMoc)
        self.frameConstructionType = QtGui.QFrame(self.gbParameters)
        self.frameConstructionType.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameConstructionType.setFrameShadow(QtGui.QFrame.Raised)
        self.frameConstructionType.setObjectName(_fromUtf8("frameConstructionType"))
        self.hlConstructionType = QtGui.QHBoxLayout(self.frameConstructionType)
        self.hlConstructionType.setSpacing(0)
        self.hlConstructionType.setMargin(0)
        self.hlConstructionType.setObjectName(_fromUtf8("hlConstructionType"))
        self.label_69 = QtGui.QLabel(self.frameConstructionType)
        self.label_69.setMinimumSize(QtCore.QSize(180, 0))
        self.label_69.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_69.setFont(font)
        self.label_69.setObjectName(_fromUtf8("label_69"))
        self.hlConstructionType.addWidget(self.label_69)
        self.cmbConstructionType = QtGui.QComboBox(self.frameConstructionType)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbConstructionType.sizePolicy().hasHeightForWidth())
        self.cmbConstructionType.setSizePolicy(sizePolicy)
        self.cmbConstructionType.setMinimumSize(QtCore.QSize(66, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cmbConstructionType.setFont(font)
        self.cmbConstructionType.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.cmbConstructionType.setObjectName(_fromUtf8("cmbConstructionType"))
        self.hlConstructionType.addWidget(self.cmbConstructionType)
        self.vl_gbParameters.addWidget(self.frameConstructionType)
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
        self.horizontalLayout_76.addWidget(self.mocSpinBox)
        self.vl_gbParameters.addWidget(self.frameMOCmultipiler)
        self.chbOverhead = QtGui.QCheckBox(self.gbParameters)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.chbOverhead.setFont(font)
        self.chbOverhead.setObjectName(_fromUtf8("chbOverhead"))
        self.vl_gbParameters.addWidget(self.chbOverhead)
        self.verticalLayout.addWidget(self.gbParameters)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.gbNavAid.setTitle(_translate("Form", "Navigational Aid", None))
        # self.label_67.setText(_translate("Form", "Type:", None))
        self.gbParameters.setTitle(_translate("Form", "Parameters", None))
        # self.label_74.setText(_translate("Form", "Track():", None))
        # self.txtTrackRadial.setText(_translate("Form", "0", None))
        self.label_75.setText(_translate("Form", "Distance to Start(nm):", None))
        self.txtDistStart.setText(_translate("Form", "0", None))
        self.label_76.setText(_translate("Form", "Distance to Finish(nm):", None))
        self.txtDistFinish.setText(_translate("Form", "0", None))
        self.label_79.setText(_translate("Form", "Starting Altitude(m):", None))
        self.txtStartAltitude.setText(_translate("Form", "3000", None))
        self.label_77.setText(_translate("Form", "Altitude Change(%):", None))
        self.txtAltitudeChange.setText(_translate("Form", "0", None))
        self.label_66.setText(_translate("Form", "Tolerance Type:", None))
        self.label_68.setText(_translate("Form", "Selection Mode:", None))
        self.label_70.setText(_translate("Form", "Primary Moc:", None))
        self.txtPrimaryMOC.setText(_translate("Form", "300", None))
        self.label_6.setText(_translate("Form", "m", None))
        self.labelMocFt.setText(_translate("Form", "ft", None))
        self.label_69.setText(_translate("Form", "Construction Type:", None))
        self.label_84.setText(_translate("Form", "MOCmultiplier:", None))
        self.chbOverhead.setText(_translate("Form", "2.5 nm over-head the NDB", None))

