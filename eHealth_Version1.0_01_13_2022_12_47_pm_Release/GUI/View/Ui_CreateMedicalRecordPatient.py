# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/Design/UI_CreateMedicalRecordPatient.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateMedicalRecordPatient(object):
    def setupUi(self, CreateMedicalRecordPatient):
        CreateMedicalRecordPatient.setObjectName("CreateMedicalRecordPatient")
        CreateMedicalRecordPatient.resize(900, 615)
        font = QtGui.QFont()
        font.setPointSize(12)
        CreateMedicalRecordPatient.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(CreateMedicalRecordPatient)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(CreateMedicalRecordPatient)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(CreateMedicalRecordPatient)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -267, 863, 983))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(75)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.txtFullName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.txtFullName.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtFullName.setFont(font)
        self.txtFullName.setObjectName("txtFullName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtFullName)
        self.txtOld = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.txtOld.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtOld.setFont(font)
        self.txtOld.setObjectName("txtOld")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtOld)
        self.txtGender = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.txtGender.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtGender.setFont(font)
        self.txtGender.setObjectName("txtGender")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtGender)
        self.txtEthnic = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.txtEthnic.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtEthnic.setFont(font)
        self.txtEthnic.setObjectName("txtEthnic")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtEthnic)
        self.txtJob = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.txtJob.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtJob.setFont(font)
        self.txtJob.setObjectName("txtJob")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtJob)
        self.txtAddress = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.txtAddress.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtAddress.setFont(font)
        self.txtAddress.setObjectName("txtAddress")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtAddress)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: transparent;\n"
"color: black;")
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.txtReasonHospitalize = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtReasonHospitalize.setFont(font)
        self.txtReasonHospitalize.setObjectName("txtReasonHospitalize")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtReasonHospitalize)
        self.txtMedicalHistory = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtMedicalHistory.setFont(font)
        self.txtMedicalHistory.setObjectName("txtMedicalHistory")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtMedicalHistory)
        self.txtAdmissionStatus = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtAdmissionStatus.setFont(font)
        self.txtAdmissionStatus.setObjectName("txtAdmissionStatus")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtAdmissionStatus)
        self.txtPrehistoric = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtPrehistoric.setFont(font)
        self.txtPrehistoric.setObjectName("txtPrehistoric")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtPrehistoric)
        self.txtClinicalExamination = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtClinicalExamination.setFont(font)
        self.txtClinicalExamination.setObjectName("txtClinicalExamination")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtClinicalExamination)
        self.txtDiagnose = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtDiagnose.setFont(font)
        self.txtDiagnose.setObjectName("txtDiagnose")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtDiagnose)
        self.txtPreclinical = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtPreclinical.setFont(font)
        self.txtPreclinical.setObjectName("txtPreclinical")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txtPreclinical)
        self.txtGeneralConclusion = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtGeneralConclusion.setFont(font)
        self.txtGeneralConclusion.setObjectName("txtGeneralConclusion")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.txtGeneralConclusion)
        self.txtRegimen = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtRegimen.setFont(font)
        self.txtRegimen.setObjectName("txtRegimen")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.txtRegimen)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btCreate = QtWidgets.QPushButton(CreateMedicalRecordPatient)
        self.btCreate.setMinimumSize(QtCore.QSize(90, 30))
        self.btCreate.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btCreate.setFont(font)
        self.btCreate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btCreate.setObjectName("btCreate")
        self.horizontalLayout_2.addWidget(self.btCreate)
        self.btRefresh = QtWidgets.QPushButton(CreateMedicalRecordPatient)
        self.btRefresh.setMinimumSize(QtCore.QSize(90, 30))
        self.btRefresh.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btRefresh.setFont(font)
        self.btRefresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btRefresh.setObjectName("btRefresh")
        self.horizontalLayout_2.addWidget(self.btRefresh)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(CreateMedicalRecordPatient)
        QtCore.QMetaObject.connectSlotsByName(CreateMedicalRecordPatient)

    def retranslateUi(self, CreateMedicalRecordPatient):
        _translate = QtCore.QCoreApplication.translate
        CreateMedicalRecordPatient.setWindowTitle(_translate("CreateMedicalRecordPatient", "Tạo Bệnh Án - IDPatient - FullName"))
        self.label.setText(_translate("CreateMedicalRecordPatient", "Tạo Bệnh Án"))
        self.label_2.setText(_translate("CreateMedicalRecordPatient", "Họ Tên:"))
        self.label_3.setText(_translate("CreateMedicalRecordPatient", "Tuổi"))
        self.label_4.setText(_translate("CreateMedicalRecordPatient", "Giới Tính:"))
        self.label_5.setText(_translate("CreateMedicalRecordPatient", "Dân Tộc:"))
        self.label_6.setText(_translate("CreateMedicalRecordPatient", "Nghề Nghiệp:"))
        self.label_7.setText(_translate("CreateMedicalRecordPatient", "Địa Chỉ:"))
        self.label_8.setText(_translate("CreateMedicalRecordPatient", "Lý Do Nhập Viện:"))
        self.label_10.setText(_translate("CreateMedicalRecordPatient", "Bệnh Sử:"))
        self.label_13.setText(_translate("CreateMedicalRecordPatient", "Tình Trạng Nhập Viện:"))
        self.label_14.setText(_translate("CreateMedicalRecordPatient", "Tiền Sử:"))
        self.label_12.setText(_translate("CreateMedicalRecordPatient", "Khám Lâm Sàng:"))
        self.label_15.setText(_translate("CreateMedicalRecordPatient", "Chẩn Đoán Sơ Bộ:"))
        self.label_11.setText(_translate("CreateMedicalRecordPatient", "Cận Lâm Sàng:"))
        self.label_16.setText(_translate("CreateMedicalRecordPatient", "Kết Luận Bệnh:"))
        self.label_9.setText(_translate("CreateMedicalRecordPatient", "Phác Đồ:"))
        self.btCreate.setText(_translate("CreateMedicalRecordPatient", "Tạo Bệnh Án"))
        self.btRefresh.setText(_translate("CreateMedicalRecordPatient", "Làm Mới"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateMedicalRecordPatient = QtWidgets.QFrame()
    ui = Ui_CreateMedicalRecordPatient()
    ui.setupUi(CreateMedicalRecordPatient)
    CreateMedicalRecordPatient.show()
    sys.exit(app.exec_())
