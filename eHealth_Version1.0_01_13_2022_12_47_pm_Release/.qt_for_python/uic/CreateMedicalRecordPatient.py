# Form implementation generated from reading ui file 'e:\A_Do_An_Endgames\Dev\eHealth_Version1.0_11_19_2021_1_58_pm_Debug\GUI\Design\CreateMedicalRecordPatient.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(CreateMedicalRecordPatient)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(CreateMedicalRecordPatient)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 863, 983))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(75)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_6)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_12)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_15)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_16)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName("textEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit)
        self.textEdit_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_2)
        self.textEdit_3 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_3.setObjectName("textEdit_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_3)
        self.textEdit_4 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_4.setObjectName("textEdit_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_4)
        self.textEdit_5 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_5.setObjectName("textEdit_5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_5)
        self.textEdit_6 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_6.setObjectName("textEdit_6")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_6)
        self.textEdit_7 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_7.setObjectName("textEdit_7")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_7)
        self.textEdit_8 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_8.setObjectName("textEdit_8")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_8)
        self.textEdit_9 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_9.setObjectName("textEdit_9")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_9)
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
        self.btCreate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btCreate.setObjectName("btCreate")
        self.horizontalLayout_2.addWidget(self.btCreate)
        self.btRefresh = QtWidgets.QPushButton(CreateMedicalRecordPatient)
        self.btRefresh.setMinimumSize(QtCore.QSize(90, 30))
        self.btRefresh.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btRefresh.setFont(font)
        self.btRefresh.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
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
