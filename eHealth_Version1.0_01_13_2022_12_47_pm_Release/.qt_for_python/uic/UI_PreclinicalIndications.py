# Form implementation generated from reading ui file 'e:\A_Do_An_Endgames\Dev\eHealth_Version1.0_11_19_2021_1_58_pm_Debug\GUI\Design\UI_PreclinicalIndications.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PreclinicalIndications(object):
    def setupUi(self, PreclinicalIndications):
        PreclinicalIndications.setObjectName("PreclinicalIndications")
        PreclinicalIndications.resize(480, 402)
        self.verticalLayout = QtWidgets.QVBoxLayout(PreclinicalIndications)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(PreclinicalIndications)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lbPatient = QtWidgets.QLabel(PreclinicalIndications)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbPatient.setFont(font)
        self.lbPatient.setObjectName("lbPatient")
        self.horizontalLayout_3.addWidget(self.lbPatient)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setContentsMargins(6, 6, 6, 6)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.checkXRays = QtWidgets.QCheckBox(PreclinicalIndications)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkXRays.setFont(font)
        self.checkXRays.setObjectName("checkXRays")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.checkXRays)
        self.comboTypeXRays = QtWidgets.QComboBox(PreclinicalIndications)
        self.comboTypeXRays.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboTypeXRays.setFont(font)
        self.comboTypeXRays.setObjectName("comboTypeXRays")
        self.comboTypeXRays.addItem("")
        self.comboTypeXRays.addItem("")
        self.comboTypeXRays.addItem("")
        self.comboTypeXRays.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboTypeXRays)
        self.checkCTScan = QtWidgets.QCheckBox(PreclinicalIndications)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkCTScan.setFont(font)
        self.checkCTScan.setObjectName("checkCTScan")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.checkCTScan)
        self.comboTypeCTScan = QtWidgets.QComboBox(PreclinicalIndications)
        self.comboTypeCTScan.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboTypeCTScan.setFont(font)
        self.comboTypeCTScan.setObjectName("comboTypeCTScan")
        self.comboTypeCTScan.addItem("")
        self.comboTypeCTScan.addItem("")
        self.comboTypeCTScan.addItem("")
        self.comboTypeCTScan.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboTypeCTScan)
        self.checkMRI = QtWidgets.QCheckBox(PreclinicalIndications)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkMRI.setFont(font)
        self.checkMRI.setObjectName("checkMRI")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.checkMRI)
        self.comboTypeMRI = QtWidgets.QComboBox(PreclinicalIndications)
        self.comboTypeMRI.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboTypeMRI.setFont(font)
        self.comboTypeMRI.setObjectName("comboTypeMRI")
        self.comboTypeMRI.addItem("")
        self.comboTypeMRI.addItem("")
        self.comboTypeMRI.addItem("")
        self.comboTypeMRI.addItem("")
        self.comboTypeMRI.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboTypeMRI)
        self.checkUltrasonic = QtWidgets.QCheckBox(PreclinicalIndications)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkUltrasonic.setFont(font)
        self.checkUltrasonic.setObjectName("checkUltrasonic")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.checkUltrasonic)
        self.comboTypeUltrasonic = QtWidgets.QComboBox(PreclinicalIndications)
        self.comboTypeUltrasonic.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboTypeUltrasonic.setFont(font)
        self.comboTypeUltrasonic.setObjectName("comboTypeUltrasonic")
        self.comboTypeUltrasonic.addItem("")
        self.comboTypeUltrasonic.addItem("")
        self.comboTypeUltrasonic.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboTypeUltrasonic)
        self.checkTest = QtWidgets.QCheckBox(PreclinicalIndications)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkTest.setFont(font)
        self.checkTest.setObjectName("checkTest")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.checkTest)
        self.comboTypeTest = QtWidgets.QComboBox(PreclinicalIndications)
        self.comboTypeTest.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboTypeTest.setFont(font)
        self.comboTypeTest.setObjectName("comboTypeTest")
        self.comboTypeTest.addItem("")
        self.comboTypeTest.addItem("")
        self.comboTypeTest.addItem("")
        self.comboTypeTest.addItem("")
        self.comboTypeTest.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboTypeTest)
        self.checkECG = QtWidgets.QCheckBox(PreclinicalIndications)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkECG.setFont(font)
        self.checkECG.setObjectName("checkECG")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.checkECG)
        self.comboTypeECG = QtWidgets.QComboBox(PreclinicalIndications)
        self.comboTypeECG.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboTypeECG.setFont(font)
        self.comboTypeECG.setObjectName("comboTypeECG")
        self.comboTypeECG.addItem("")
        self.comboTypeECG.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboTypeECG)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(70)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btUpdate = QtWidgets.QPushButton(PreclinicalIndications)
        self.btUpdate.setMinimumSize(QtCore.QSize(80, 30))
        self.btUpdate.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btUpdate.setFont(font)
        self.btUpdate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btUpdate.setObjectName("btUpdate")
        self.horizontalLayout_2.addWidget(self.btUpdate)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 8)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(PreclinicalIndications)
        QtCore.QMetaObject.connectSlotsByName(PreclinicalIndications)

    def retranslateUi(self, PreclinicalIndications):
        _translate = QtCore.QCoreApplication.translate
        PreclinicalIndications.setWindowTitle(_translate("PreclinicalIndications", "Chỉ Định Cận Lâm Sàng - IDPatient - FullName"))
        self.label.setText(_translate("PreclinicalIndications", "Chỉ Định Cận Lâm Sàng"))
        self.lbPatient.setText(_translate("PreclinicalIndications", "Bệnh Nhân: IDPatient - FullName"))
        self.checkXRays.setText(_translate("PreclinicalIndications", "Chụp X - Quang"))
        self.comboTypeXRays.setItemText(0, _translate("PreclinicalIndications", "Phổi"))
        self.comboTypeXRays.setItemText(1, _translate("PreclinicalIndications", "Cột Sống"))
        self.comboTypeXRays.setItemText(2, _translate("PreclinicalIndications", "Xương"))
        self.comboTypeXRays.setItemText(3, _translate("PreclinicalIndications", "Tuyến Vú"))
        self.checkCTScan.setText(_translate("PreclinicalIndications", "Chụp Cắt Lớp CT"))
        self.comboTypeCTScan.setItemText(0, _translate("PreclinicalIndications", "Sọ Não"))
        self.comboTypeCTScan.setItemText(1, _translate("PreclinicalIndications", "Phổi"))
        self.comboTypeCTScan.setItemText(2, _translate("PreclinicalIndications", "Xương"))
        self.comboTypeCTScan.setItemText(3, _translate("PreclinicalIndications", "Ổ Bụng"))
        self.checkMRI.setText(_translate("PreclinicalIndications", "Chụp MRI"))
        self.comboTypeMRI.setItemText(0, _translate("PreclinicalIndications", "Sọ Não"))
        self.comboTypeMRI.setItemText(1, _translate("PreclinicalIndications", "Mạch Máu Não"))
        self.comboTypeMRI.setItemText(2, _translate("PreclinicalIndications", "Tĩnh Mạch Đồ"))
        self.comboTypeMRI.setItemText(3, _translate("PreclinicalIndications", "Tim"))
        self.comboTypeMRI.setItemText(4, _translate("PreclinicalIndications", "Tuyến Vú"))
        self.checkUltrasonic.setText(_translate("PreclinicalIndications", "Siêu Âm"))
        self.comboTypeUltrasonic.setItemText(0, _translate("PreclinicalIndications", "Tim"))
        self.comboTypeUltrasonic.setItemText(1, _translate("PreclinicalIndications", "Thai Nhi"))
        self.comboTypeUltrasonic.setItemText(2, _translate("PreclinicalIndications", "Gan Mật"))
        self.checkTest.setText(_translate("PreclinicalIndications", "Xét Nghiệm"))
        self.comboTypeTest.setItemText(0, _translate("PreclinicalIndications", "Máu"))
        self.comboTypeTest.setItemText(1, _translate("PreclinicalIndications", "Nước Tiểu"))
        self.comboTypeTest.setItemText(2, _translate("PreclinicalIndications", "SARS - COV - 2"))
        self.comboTypeTest.setItemText(3, _translate("PreclinicalIndications", "Sinh Thiết"))
        self.comboTypeTest.setItemText(4, _translate("PreclinicalIndications", "CRP"))
        self.checkECG.setText(_translate("PreclinicalIndications", "ECG - EEG"))
        self.comboTypeECG.setItemText(0, _translate("PreclinicalIndications", "Điện Tâm Đồ"))
        self.comboTypeECG.setItemText(1, _translate("PreclinicalIndications", "Điện Não Đồ"))
        self.btUpdate.setText(_translate("PreclinicalIndications", "Cập Nhật"))
