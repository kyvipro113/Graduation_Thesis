# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/Design/UI_CTScan.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CTScan(object):
    def setupUi(self, CTScan):
        CTScan.setObjectName("CTScan")
        CTScan.resize(1200, 611)
        font = QtGui.QFont()
        font.setPointSize(12)
        CTScan.setFont(font)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(CTScan)
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(CTScan)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(CTScan)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.txtSearch = QtWidgets.QLineEdit(CTScan)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtSearch.setFont(font)
        self.txtSearch.setObjectName("txtSearch")
        self.horizontalLayout_2.addWidget(self.txtSearch)
        self.btSearch = QtWidgets.QPushButton(CTScan)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btSearch.setFont(font)
        self.btSearch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btSearch.setObjectName("btSearch")
        self.horizontalLayout_2.addWidget(self.btSearch)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(CTScan)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(False)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioBTIDPatient = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.radioBTIDPatient.setFont(font)
        self.radioBTIDPatient.setObjectName("radioBTIDPatient")
        self.verticalLayout.addWidget(self.radioBTIDPatient)
        self.radioBTFullName = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioBTFullName.setFont(font)
        self.radioBTFullName.setObjectName("radioBTFullName")
        self.verticalLayout.addWidget(self.radioBTFullName)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(CTScan)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboTypeCTScan = QtWidgets.QComboBox(CTScan)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboTypeCTScan.setFont(font)
        self.comboTypeCTScan.setObjectName("comboTypeCTScan")
        self.comboTypeCTScan.addItem("")
        self.comboTypeCTScan.addItem("")
        self.comboTypeCTScan.addItem("")
        self.comboTypeCTScan.addItem("")
        self.horizontalLayout_3.addWidget(self.comboTypeCTScan)
        self.horizontalLayout_3.setStretch(1, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.dataTabPatient = QtWidgets.QTableWidget(CTScan)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.dataTabPatient.setFont(font)
        self.dataTabPatient.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dataTabPatient.setObjectName("dataTabPatient")
        self.dataTabPatient.setColumnCount(4)
        self.dataTabPatient.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabPatient.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabPatient.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabPatient.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTabPatient.setHorizontalHeaderItem(3, item)
        self.dataTabPatient.horizontalHeader().setDefaultSectionSize(120)
        self.verticalLayout_2.addWidget(self.dataTabPatient)
        self.checkAllPatient = QtWidgets.QCheckBox(CTScan)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkAllPatient.setFont(font)
        self.checkAllPatient.setObjectName("checkAllPatient")
        self.verticalLayout_2.addWidget(self.checkAllPatient)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.btUpload = QtWidgets.QPushButton(CTScan)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btUpload.setFont(font)
        self.btUpload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btUpload.setObjectName("btUpload")
        self.horizontalLayout_4.addWidget(self.btUpload)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(3, 7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbPatient = QtWidgets.QLabel(CTScan)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbPatient.setFont(font)
        self.lbPatient.setObjectName("lbPatient")
        self.verticalLayout_3.addWidget(self.lbPatient)
        self.lbCTScanImg = QtWidgets.QLabel(CTScan)
        self.lbCTScanImg.setMinimumSize(QtCore.QSize(384, 384))
        self.lbCTScanImg.setMaximumSize(QtCore.QSize(384, 384))
        self.lbCTScanImg.setFrameShape(QtWidgets.QFrame.Box)
        self.lbCTScanImg.setText("")
        self.lbCTScanImg.setObjectName("lbCTScanImg")
        self.verticalLayout_3.addWidget(self.lbCTScanImg)
        self.hSlider = QtWidgets.QSlider(CTScan)
        self.hSlider.setMinimumSize(QtCore.QSize(384, 0))
        self.hSlider.setMaximumSize(QtCore.QSize(384, 16777215))
        self.hSlider.setMinimum(1)
        self.hSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hSlider.setObjectName("hSlider")
        self.verticalLayout_3.addWidget(self.hSlider)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.setStretch(1, 9)

        self.retranslateUi(CTScan)
        QtCore.QMetaObject.connectSlotsByName(CTScan)

    def retranslateUi(self, CTScan):
        _translate = QtCore.QCoreApplication.translate
        CTScan.setWindowTitle(_translate("CTScan", "Frame"))
        self.label.setText(_translate("CTScan", "CHỤP CẮT LỚP VI TÍNH"))
        self.label_5.setText(_translate("CTScan", "Tìm Kiếm Bệnh Nhân:"))
        self.btSearch.setText(_translate("CTScan", "Tìm Kiếm"))
        self.groupBox.setTitle(_translate("CTScan", "Tìm Kiếm Theo"))
        self.radioBTIDPatient.setText(_translate("CTScan", "Mã Bệnh Nhân"))
        self.radioBTFullName.setText(_translate("CTScan", "Tên Bệnh Nhân"))
        self.label_4.setText(_translate("CTScan", "Loại Chụp CT:"))
        self.comboTypeCTScan.setItemText(0, _translate("CTScan", "Sọ Não"))
        self.comboTypeCTScan.setItemText(1, _translate("CTScan", "Phổi"))
        self.comboTypeCTScan.setItemText(2, _translate("CTScan", "Xương"))
        self.comboTypeCTScan.setItemText(3, _translate("CTScan", "Ổ Bụng"))
        item = self.dataTabPatient.horizontalHeaderItem(0)
        item.setText(_translate("CTScan", "Mã Bệnh Nhân"))
        item = self.dataTabPatient.horizontalHeaderItem(1)
        item.setText(_translate("CTScan", "Tên Bệnh Nhân"))
        item = self.dataTabPatient.horizontalHeaderItem(2)
        item.setText(_translate("CTScan", "Loại Chụp CT"))
        item = self.dataTabPatient.horizontalHeaderItem(3)
        item.setText(_translate("CTScan", "Trạng Thái"))
        self.checkAllPatient.setText(_translate("CTScan", "Hiển Thị Tất Cả Bệnh Nhân"))
        self.btUpload.setText(_translate("CTScan", "Cập Nhật\n"
"Kết Quả Chụp"))
        self.lbPatient.setText(_translate("CTScan", "Bệnh Nhân: IDPatient - FullName"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CTScan = QtWidgets.QFrame()
    ui = Ui_CTScan()
    ui.setupUi(CTScan)
    CTScan.show()
    sys.exit(app.exec_())
