# Form implementation generated from reading ui file 'e:\A_Do_An_Endgames\Dev\eHealth_Version1.0_11_19_2021_1_58_pm_Debug\GUI\Design\MedicalRecord.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MedicalRecord(object):
    def setupUi(self, MedicalRecord):
        MedicalRecord.setObjectName("MedicalRecord")
        MedicalRecord.resize(1200, 611)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(MedicalRecord)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(MedicalRecord)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(MedicalRecord)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.dataTabPatient = QtWidgets.QTableWidget(MedicalRecord)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.dataTabPatient.setFont(font)
        self.dataTabPatient.setObjectName("dataTabPatient")
        self.dataTabPatient.setColumnCount(2)
        self.dataTabPatient.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabPatient.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabPatient.setHorizontalHeaderItem(1, item)
        self.dataTabPatient.horizontalHeader().setDefaultSectionSize(120)
        self.verticalLayout_2.addWidget(self.dataTabPatient)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(MedicalRecord)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.dataTabMedicalRecord = QtWidgets.QTableWidget(MedicalRecord)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.dataTabMedicalRecord.setFont(font)
        self.dataTabMedicalRecord.setObjectName("dataTabMedicalRecord")
        self.dataTabMedicalRecord.setColumnCount(3)
        self.dataTabMedicalRecord.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRecord.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRecord.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabMedicalRecord.setHorizontalHeaderItem(2, item)
        self.dataTabMedicalRecord.horizontalHeader().setDefaultSectionSize(120)
        self.verticalLayout.addWidget(self.dataTabMedicalRecord)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btAdd = QtWidgets.QPushButton(MedicalRecord)
        self.btAdd.setMinimumSize(QtCore.QSize(90, 25))
        self.btAdd.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btAdd.setFont(font)
        self.btAdd.setObjectName("btAdd")
        self.horizontalLayout_2.addWidget(self.btAdd)
        self.btUpdate = QtWidgets.QPushButton(MedicalRecord)
        self.btUpdate.setMinimumSize(QtCore.QSize(90, 25))
        self.btUpdate.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btUpdate.setFont(font)
        self.btUpdate.setObjectName("btUpdate")
        self.horizontalLayout_2.addWidget(self.btUpdate)
        self.btDel = QtWidgets.QPushButton(MedicalRecord)
        self.btDel.setMinimumSize(QtCore.QSize(90, 25))
        self.btDel.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btDel.setFont(font)
        self.btDel.setObjectName("btDel")
        self.horizontalLayout_2.addWidget(self.btDel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.mainMDI = QtWidgets.QMdiArea(MedicalRecord)
        self.mainMDI.setObjectName("mainMDI")
        self.horizontalLayout_4.addWidget(self.mainMDI)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.retranslateUi(MedicalRecord)
        QtCore.QMetaObject.connectSlotsByName(MedicalRecord)

    def retranslateUi(self, MedicalRecord):
        _translate = QtCore.QCoreApplication.translate
        MedicalRecord.setWindowTitle(_translate("MedicalRecord", "Frame"))
        self.label.setText(_translate("MedicalRecord", "BỆNH ÁN"))
        self.label_3.setText(_translate("MedicalRecord", "Danh Sách Bệnh Nhân"))
        item = self.dataTabPatient.horizontalHeaderItem(0)
        item.setText(_translate("MedicalRecord", "Mã Bệnh Nhân"))
        item = self.dataTabPatient.horizontalHeaderItem(1)
        item.setText(_translate("MedicalRecord", "Tên Bệnh Nhân"))
        self.label_2.setText(_translate("MedicalRecord", "Danh Sách Bệnh Án"))
        item = self.dataTabMedicalRecord.horizontalHeaderItem(0)
        item.setText(_translate("MedicalRecord", "Mã Bệnh Án"))
        item = self.dataTabMedicalRecord.horizontalHeaderItem(1)
        item.setText(_translate("MedicalRecord", "Mã Bệnh Nhân"))
        item = self.dataTabMedicalRecord.horizontalHeaderItem(2)
        item.setText(_translate("MedicalRecord", "Tên Bệnh Nhân"))
        self.btAdd.setText(_translate("MedicalRecord", "Tạo Bệnh Án"))
        self.btUpdate.setText(_translate("MedicalRecord", "Sửa Bệnh Án"))
        self.btDel.setText(_translate("MedicalRecord", "Xóa Bệnh Án"))
