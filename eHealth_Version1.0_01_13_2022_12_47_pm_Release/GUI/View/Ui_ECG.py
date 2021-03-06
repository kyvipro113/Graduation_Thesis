# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/Design/UI_ECG.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ECG(object):
    def setupUi(self, ECG):
        ECG.setObjectName("ECG")
        ECG.resize(1200, 620)
        font = QtGui.QFont()
        font.setPointSize(12)
        ECG.setFont(font)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(ECG)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(ECG)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(ECG)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.txtSearch = QtWidgets.QLineEdit(ECG)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtSearch.setFont(font)
        self.txtSearch.setObjectName("txtSearch")
        self.horizontalLayout_2.addWidget(self.txtSearch)
        self.btSearch = QtWidgets.QPushButton(ECG)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btSearch.setFont(font)
        self.btSearch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btSearch.setObjectName("btSearch")
        self.horizontalLayout_2.addWidget(self.btSearch)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(ECG)
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
        self.label_4 = QtWidgets.QLabel(ECG)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboTypeECG = QtWidgets.QComboBox(ECG)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboTypeECG.setFont(font)
        self.comboTypeECG.setObjectName("comboTypeECG")
        self.comboTypeECG.addItem("")
        self.comboTypeECG.addItem("")
        self.horizontalLayout_3.addWidget(self.comboTypeECG)
        self.horizontalLayout_3.setStretch(1, 9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.dataTabPatient = QtWidgets.QTableWidget(ECG)
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
        self.checkAllPatient = QtWidgets.QCheckBox(ECG)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkAllPatient.setFont(font)
        self.checkAllPatient.setObjectName("checkAllPatient")
        self.verticalLayout_2.addWidget(self.checkAllPatient)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.btUpload = QtWidgets.QPushButton(ECG)
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
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbPatient = QtWidgets.QLabel(ECG)
        self.lbPatient.setMinimumSize(QtCore.QSize(0, 27))
        self.lbPatient.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbPatient.setFont(font)
        self.lbPatient.setObjectName("lbPatient")
        self.verticalLayout_4.addWidget(self.lbPatient)
        self.mainFrame = QtWidgets.QFrame(ECG)
        self.mainFrame.setMinimumSize(QtCore.QSize(700, 240))
        self.mainFrame.setMaximumSize(QtCore.QSize(16777215, 9999))
        self.mainFrame.setStyleSheet("")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setLineWidth(3)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName("mainLayout")
        self.verticalLayout_3.addLayout(self.mainLayout)
        self.verticalLayout_3.setStretch(0, 9)
        self.verticalLayout_4.addWidget(self.mainFrame)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.verticalLayout_4.setStretch(1, 1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.retranslateUi(ECG)
        QtCore.QMetaObject.connectSlotsByName(ECG)

    def retranslateUi(self, ECG):
        _translate = QtCore.QCoreApplication.translate
        ECG.setWindowTitle(_translate("ECG", "Frame"))
        self.label.setText(_translate("ECG", "??I???N ?????"))
        self.label_5.setText(_translate("ECG", "T??m Ki???m B???nh Nh??n:"))
        self.btSearch.setText(_translate("ECG", "T??m Ki???m"))
        self.groupBox.setTitle(_translate("ECG", "T??m Ki???m Theo"))
        self.radioBTIDPatient.setText(_translate("ECG", "M?? B???nh Nh??n"))
        self.radioBTFullName.setText(_translate("ECG", "T??n B???nh Nh??n"))
        self.label_4.setText(_translate("ECG", "Lo???i ??i???n ?????:"))
        self.comboTypeECG.setItemText(0, _translate("ECG", "??i???n T??m ?????"))
        self.comboTypeECG.setItemText(1, _translate("ECG", "??i???n N??o ?????"))
        item = self.dataTabPatient.horizontalHeaderItem(0)
        item.setText(_translate("ECG", "M?? B???nh Nh??n"))
        item = self.dataTabPatient.horizontalHeaderItem(1)
        item.setText(_translate("ECG", "T??n B???nh Nh??n"))
        item = self.dataTabPatient.horizontalHeaderItem(2)
        item.setText(_translate("ECG", "Lo???i ??i???n ?????"))
        item = self.dataTabPatient.horizontalHeaderItem(3)
        item.setText(_translate("ECG", "Tr???ng Th??i"))
        self.checkAllPatient.setText(_translate("ECG", "Hi???n Th??? T???t C??? B???nh Nh??n"))
        self.btUpload.setText(_translate("ECG", "C???p Nh???t\n"
"K???t Qu??? ??i???n ?????"))
        self.lbPatient.setText(_translate("ECG", "B???nh Nh??n: IDPatient - FullName"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ECG = QtWidgets.QFrame()
    ui = Ui_ECG()
    ui.setupUi(ECG)
    ECG.show()
    sys.exit(app.exec_())
