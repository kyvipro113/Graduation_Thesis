# Form implementation generated from reading ui file 'e:\A_Do_An_Endgames\Dev\eHealth_Version1.0_11_19_2021_1_58_pm_Debug\GUI\Design\UI_Employee.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Employee(object):
    def setupUi(self, Employee):
        Employee.setObjectName("Employee")
        Employee.resize(1200, 611)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Employee)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Employee)
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
        self.formLayout.setContentsMargins(-1, 15, -1, 5)
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.txtIDEmployee = QtWidgets.QLineEdit(Employee)
        self.txtIDEmployee.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtIDEmployee.setFont(font)
        self.txtIDEmployee.setObjectName("txtIDEmployee")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtIDEmployee)
        self.label_3 = QtWidgets.QLabel(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.txtFullName = QtWidgets.QLineEdit(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtFullName.setFont(font)
        self.txtFullName.setObjectName("txtFullName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtFullName)
        self.label_4 = QtWidgets.QLabel(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.deDateOfBirth = QtWidgets.QDateEdit(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deDateOfBirth.setFont(font)
        self.deDateOfBirth.setObjectName("deDateOfBirth")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.deDateOfBirth)
        self.label_5 = QtWidgets.QLabel(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.comboGender = QtWidgets.QComboBox(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboGender.setFont(font)
        self.comboGender.setObjectName("comboGender")
        self.comboGender.addItem("")
        self.comboGender.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboGender)
        self.label_6 = QtWidgets.QLabel(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.txtCitizenID = QtWidgets.QLineEdit(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtCitizenID.setFont(font)
        self.txtCitizenID.setObjectName("txtCitizenID")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtCitizenID)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(-1, 15, -1, 5)
        self.formLayout_3.setVerticalSpacing(25)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_9 = QtWidgets.QLabel(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.txtNumberPhone = QtWidgets.QLineEdit(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtNumberPhone.setFont(font)
        self.txtNumberPhone.setObjectName("txtNumberPhone")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtNumberPhone)
        self.label_13 = QtWidgets.QLabel(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.txtAddress = QtWidgets.QLineEdit(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtAddress.setFont(font)
        self.txtAddress.setObjectName("txtAddress")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtAddress)
        self.label_10 = QtWidgets.QLabel(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.txtDegree = QtWidgets.QLineEdit(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtDegree.setFont(font)
        self.txtDegree.setObjectName("txtDegree")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtDegree)
        self.label_11 = QtWidgets.QLabel(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.comboFaculty = QtWidgets.QComboBox(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboFaculty.setFont(font)
        self.comboFaculty.setObjectName("comboFaculty")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboFaculty)
        self.label_12 = QtWidgets.QLabel(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_12)
        self.comboPosition = QtWidgets.QComboBox(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboPosition.setFont(font)
        self.comboPosition.setObjectName("comboPosition")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboPosition)
        self.horizontalLayout_2.addLayout(self.formLayout_3)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(-1, 15, -1, 5)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lbImage = QtWidgets.QLabel(Employee)
        self.lbImage.setMinimumSize(QtCore.QSize(130, 160))
        self.lbImage.setMaximumSize(QtCore.QSize(130, 160))
        self.lbImage.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.lbImage.setText("")
        self.lbImage.setObjectName("lbImage")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lbImage)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout_2.setItem(1, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem2)
        self.btChooseImage = QtWidgets.QPushButton(Employee)
        self.btChooseImage.setMinimumSize(QtCore.QSize(80, 30))
        self.btChooseImage.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btChooseImage.setFont(font)
        self.btChooseImage.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btChooseImage.setObjectName("btChooseImage")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.btChooseImage)
        self.label_8 = QtWidgets.QLabel(Employee)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 15, -1, -1)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btAdd = QtWidgets.QPushButton(Employee)
        self.btAdd.setMinimumSize(QtCore.QSize(90, 30))
        self.btAdd.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btAdd.setFont(font)
        self.btAdd.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btAdd.setObjectName("btAdd")
        self.verticalLayout.addWidget(self.btAdd)
        self.btUpdate = QtWidgets.QPushButton(Employee)
        self.btUpdate.setMinimumSize(QtCore.QSize(90, 30))
        self.btUpdate.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btUpdate.setFont(font)
        self.btUpdate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btUpdate.setObjectName("btUpdate")
        self.verticalLayout.addWidget(self.btUpdate)
        self.btDel = QtWidgets.QPushButton(Employee)
        self.btDel.setMinimumSize(QtCore.QSize(90, 30))
        self.btDel.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btDel.setFont(font)
        self.btDel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btDel.setObjectName("btDel")
        self.verticalLayout.addWidget(self.btDel)
        self.btRefresh = QtWidgets.QPushButton(Employee)
        self.btRefresh.setMinimumSize(QtCore.QSize(90, 30))
        self.btRefresh.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btRefresh.setFont(font)
        self.btRefresh.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btRefresh.setObjectName("btRefresh")
        self.verticalLayout.addWidget(self.btRefresh)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.dataTabEmployee = QtWidgets.QTableWidget(Employee)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.dataTabEmployee.setFont(font)
        self.dataTabEmployee.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.dataTabEmployee.setObjectName("dataTabEmployee")
        self.dataTabEmployee.setColumnCount(10)
        self.dataTabEmployee.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabEmployee.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabEmployee.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabEmployee.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabEmployee.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabEmployee.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabEmployee.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabEmployee.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabEmployee.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabEmployee.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabEmployee.setHorizontalHeaderItem(9, item)
        self.verticalLayout_2.addWidget(self.dataTabEmployee)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 3)

        self.retranslateUi(Employee)
        QtCore.QMetaObject.connectSlotsByName(Employee)

    def retranslateUi(self, Employee):
        _translate = QtCore.QCoreApplication.translate
        Employee.setWindowTitle(_translate("Employee", "Frame"))
        self.label.setText(_translate("Employee", "NH??N VI??N"))
        self.label_2.setText(_translate("Employee", "M?? Nh??n Vi??n:"))
        self.label_3.setText(_translate("Employee", "T??n Nh??n Vi??n:"))
        self.label_4.setText(_translate("Employee", "Ng??y Sinh:"))
        self.label_5.setText(_translate("Employee", "Gi???i T??nh:"))
        self.comboGender.setItemText(0, _translate("Employee", "Nam"))
        self.comboGender.setItemText(1, _translate("Employee", "N???"))
        self.label_6.setText(_translate("Employee", "S??? C??n C?????c:"))
        self.label_9.setText(_translate("Employee", "S??? ??i???n Tho???i:"))
        self.label_13.setText(_translate("Employee", "?????a Ch???:"))
        self.label_10.setText(_translate("Employee", "Tr??nh ?????:"))
        self.label_11.setText(_translate("Employee", "Khoa:"))
        self.label_12.setText(_translate("Employee", "Ch???c V???:"))
        self.btChooseImage.setText(_translate("Employee", "Ch???n ???nh"))
        self.label_8.setText(_translate("Employee", "???nh"))
        self.btAdd.setText(_translate("Employee", "Th??m M???i"))
        self.btUpdate.setText(_translate("Employee", "C???p Nh???t"))
        self.btDel.setText(_translate("Employee", "X??a"))
        self.btRefresh.setText(_translate("Employee", "L??m M???i"))
        item = self.dataTabEmployee.horizontalHeaderItem(0)
        item.setText(_translate("Employee", "M?? Nh??n Vi??n"))
        item = self.dataTabEmployee.horizontalHeaderItem(1)
        item.setText(_translate("Employee", "T??n Nh??n Vi??n"))
        item = self.dataTabEmployee.horizontalHeaderItem(2)
        item.setText(_translate("Employee", "Ng??y Sinh"))
        item = self.dataTabEmployee.horizontalHeaderItem(3)
        item.setText(_translate("Employee", "Gi???i T??nh"))
        item = self.dataTabEmployee.horizontalHeaderItem(4)
        item.setText(_translate("Employee", "S??? C??n C?????c"))
        item = self.dataTabEmployee.horizontalHeaderItem(5)
        item.setText(_translate("Employee", "S??? ??i???n Tho???i"))
        item = self.dataTabEmployee.horizontalHeaderItem(6)
        item.setText(_translate("Employee", "?????a Ch???"))
        item = self.dataTabEmployee.horizontalHeaderItem(7)
        item.setText(_translate("Employee", "Tr??nh ?????"))
        item = self.dataTabEmployee.horizontalHeaderItem(8)
        item.setText(_translate("Employee", "Khoa"))
        item = self.dataTabEmployee.horizontalHeaderItem(9)
        item.setText(_translate("Employee", "Ch???c V???"))
