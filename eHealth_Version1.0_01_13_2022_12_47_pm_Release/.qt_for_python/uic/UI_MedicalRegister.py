# Form implementation generated from reading ui file 'e:\A_Do_An_Endgames\Dev\eHealth_Version1.0_11_19_2021_1_58_pm_Debug\GUI\Design\UI_MedicalRegister.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MedicalRegister(object):
    def setupUi(self, MedicalRegister):
        MedicalRegister.setObjectName("MedicalRegister")
        MedicalRegister.resize(1200, 611)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(MedicalRegister)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, 0, -1, -1)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.label_16 = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_16)
        self.txtIDPatient = QtWidgets.QLineEdit(MedicalRegister)
        self.txtIDPatient.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtIDPatient.setFont(font)
        self.txtIDPatient.setObjectName("txtIDPatient")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtIDPatient)
        self.txtFullName = QtWidgets.QLineEdit(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtFullName.setFont(font)
        self.txtFullName.setObjectName("txtFullName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtFullName)
        self.txtOld = QtWidgets.QLineEdit(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtOld.setFont(font)
        self.txtOld.setObjectName("txtOld")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtOld)
        self.comboGender = QtWidgets.QComboBox(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboGender.setFont(font)
        self.comboGender.setObjectName("comboGender")
        self.comboGender.addItem("")
        self.comboGender.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboGender)
        self.txtEthnic = QtWidgets.QLineEdit(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtEthnic.setFont(font)
        self.txtEthnic.setObjectName("txtEthnic")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtEthnic)
        self.txtJob = QtWidgets.QLineEdit(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtJob.setFont(font)
        self.txtJob.setObjectName("txtJob")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtJob)
        self.txtAddress = QtWidgets.QLineEdit(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtAddress.setFont(font)
        self.txtAddress.setObjectName("txtAddress")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtAddress)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_9 = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.label_15 = QtWidgets.QLabel(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_15)
        self.txtNumberPhone = QtWidgets.QLineEdit(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtNumberPhone.setFont(font)
        self.txtNumberPhone.setObjectName("txtNumberPhone")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtNumberPhone)
        self.txtCitizenID = QtWidgets.QLineEdit(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtCitizenID.setFont(font)
        self.txtCitizenID.setObjectName("txtCitizenID")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtCitizenID)
        self.txtIDHealthInsurance = QtWidgets.QLineEdit(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtIDHealthInsurance.setFont(font)
        self.txtIDHealthInsurance.setObjectName("txtIDHealthInsurance")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtIDHealthInsurance)
        self.txtDiagnoseRequest = QtWidgets.QLineEdit(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtDiagnoseRequest.setFont(font)
        self.txtDiagnoseRequest.setObjectName("txtDiagnoseRequest")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtDiagnoseRequest)
        self.comboFaculty = QtWidgets.QComboBox(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboFaculty.setFont(font)
        self.comboFaculty.setObjectName("comboFaculty")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboFaculty)
        self.comboEmployee = QtWidgets.QComboBox(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboEmployee.setFont(font)
        self.comboEmployee.setObjectName("comboEmployee")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboEmployee)
        self.deTime = QtWidgets.QDateEdit(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deTime.setFont(font)
        self.deTime.setObjectName("deTime")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.deTime)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btAdd = QtWidgets.QPushButton(MedicalRegister)
        self.btAdd.setMinimumSize(QtCore.QSize(90, 30))
        self.btAdd.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btAdd.setFont(font)
        self.btAdd.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btAdd.setObjectName("btAdd")
        self.verticalLayout.addWidget(self.btAdd)
        self.btUpdate = QtWidgets.QPushButton(MedicalRegister)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btUpdate.setFont(font)
        self.btUpdate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btUpdate.setObjectName("btUpdate")
        self.verticalLayout.addWidget(self.btUpdate)
        self.btDel = QtWidgets.QPushButton(MedicalRegister)
        self.btDel.setMinimumSize(QtCore.QSize(90, 30))
        self.btDel.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btDel.setFont(font)
        self.btDel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btDel.setObjectName("btDel")
        self.verticalLayout.addWidget(self.btDel)
        self.btRefresh = QtWidgets.QPushButton(MedicalRegister)
        self.btRefresh.setMinimumSize(QtCore.QSize(90, 30))
        self.btRefresh.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btRefresh.setFont(font)
        self.btRefresh.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btRefresh.setObjectName("btRefresh")
        self.verticalLayout.addWidget(self.btRefresh)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.dataTabMedicalRegister = QtWidgets.QTableWidget(MedicalRegister)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.dataTabMedicalRegister.setFont(font)
        self.dataTabMedicalRegister.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.dataTabMedicalRegister.setObjectName("dataTabMedicalRegister")
        self.dataTabMedicalRegister.setColumnCount(14)
        self.dataTabMedicalRegister.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRegister.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRegister.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRegister.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRegister.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRegister.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRegister.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRegister.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRegister.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRegister.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRegister.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRegister.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRegister.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRegister.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRegister.setHorizontalHeaderItem(13, item)
        self.dataTabMedicalRegister.horizontalHeader().setDefaultSectionSize(120)
        self.verticalLayout_2.addWidget(self.dataTabMedicalRegister)

        self.retranslateUi(MedicalRegister)
        QtCore.QMetaObject.connectSlotsByName(MedicalRegister)

    def retranslateUi(self, MedicalRegister):
        _translate = QtCore.QCoreApplication.translate
        MedicalRegister.setWindowTitle(_translate("MedicalRegister", "Frame"))
        self.label.setText(_translate("MedicalRegister", "ĐĂNG KÝ KHÁM BỆNH"))
        self.label_3.setText(_translate("MedicalRegister", "Mã Bệnh Nhân:"))
        self.label_4.setText(_translate("MedicalRegister", "Họ Tên:"))
        self.label_5.setText(_translate("MedicalRegister", "Tuổi:"))
        self.label_6.setText(_translate("MedicalRegister", "Giới Tính:"))
        self.label_7.setText(_translate("MedicalRegister", "Dân Tộc:"))
        self.label_8.setText(_translate("MedicalRegister", "Nghề Nghiệp:"))
        self.label_16.setText(_translate("MedicalRegister", "Địa Chỉ:"))
        self.comboGender.setItemText(0, _translate("MedicalRegister", "Nam"))
        self.comboGender.setItemText(1, _translate("MedicalRegister", "Nữ"))
        self.label_9.setText(_translate("MedicalRegister", "Số Điện Thoại:"))
        self.label_10.setText(_translate("MedicalRegister", "Số Căn Cước:"))
        self.label_11.setText(_translate("MedicalRegister", "BHYT:"))
        self.label_12.setText(_translate("MedicalRegister", "Yêu Cầu Khám:"))
        self.label_13.setText(_translate("MedicalRegister", "Khoa:"))
        self.label_14.setText(_translate("MedicalRegister", "Bác Sỹ:"))
        self.label_15.setText(_translate("MedicalRegister", "Thời Gian:"))
        self.btAdd.setText(_translate("MedicalRegister", "Thêm Mới"))
        self.btUpdate.setText(_translate("MedicalRegister", "Cập Nhật"))
        self.btDel.setText(_translate("MedicalRegister", "Xóa"))
        self.btRefresh.setText(_translate("MedicalRegister", "Làm Mới"))
        item = self.dataTabMedicalRegister.horizontalHeaderItem(0)
        item.setText(_translate("MedicalRegister", "Mã Bệnh Nhân"))
        item = self.dataTabMedicalRegister.horizontalHeaderItem(1)
        item.setText(_translate("MedicalRegister", "Họ Tên"))
        item = self.dataTabMedicalRegister.horizontalHeaderItem(2)
        item.setText(_translate("MedicalRegister", "Tuổi"))
        item = self.dataTabMedicalRegister.horizontalHeaderItem(3)
        item.setText(_translate("MedicalRegister", "Giới Tính"))
        item = self.dataTabMedicalRegister.horizontalHeaderItem(4)
        item.setText(_translate("MedicalRegister", "Dân Tộc"))
        item = self.dataTabMedicalRegister.horizontalHeaderItem(5)
        item.setText(_translate("MedicalRegister", "Nghề Nghiệp"))
        item = self.dataTabMedicalRegister.horizontalHeaderItem(6)
        item.setText(_translate("MedicalRegister", "Địa Chỉ"))
        item = self.dataTabMedicalRegister.horizontalHeaderItem(7)
        item.setText(_translate("MedicalRegister", "Số Điện Thoại"))
        item = self.dataTabMedicalRegister.horizontalHeaderItem(8)
        item.setText(_translate("MedicalRegister", "Số Căn Cước"))
        item = self.dataTabMedicalRegister.horizontalHeaderItem(9)
        item.setText(_translate("MedicalRegister", "BHYT"))
        item = self.dataTabMedicalRegister.horizontalHeaderItem(10)
        item.setText(_translate("MedicalRegister", "Yêu Cầu"))
        item = self.dataTabMedicalRegister.horizontalHeaderItem(11)
        item.setText(_translate("MedicalRegister", "Khoa"))
        item = self.dataTabMedicalRegister.horizontalHeaderItem(12)
        item.setText(_translate("MedicalRegister", "Bác Sỹ"))
        item = self.dataTabMedicalRegister.horizontalHeaderItem(13)
        item.setText(_translate("MedicalRegister", "Thời Gian"))
