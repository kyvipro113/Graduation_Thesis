# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/Design/UI_ECGPatient.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ECGPatient(object):
    def setupUi(self, ECGPatient):
        ECGPatient.setObjectName("ECGPatient")
        ECGPatient.resize(885, 550)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ECGPatient)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(ECGPatient)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.comboECGType = QtWidgets.QComboBox(ECGPatient)
        self.comboECGType.setMinimumSize(QtCore.QSize(284, 0))
        self.comboECGType.setMaximumSize(QtCore.QSize(9999, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboECGType.setFont(font)
        self.comboECGType.setObjectName("comboECGType")
        self.comboECGType.addItem("")
        self.comboECGType.addItem("")
        self.horizontalLayout.addWidget(self.comboECGType)
        self.horizontalLayout.setStretch(1, 9)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.mainFrame = QtWidgets.QFrame(ECGPatient)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setLineWidth(3)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.verticalLayout_2.addLayout(self.mainLayout)
        self.verticalLayout_3.addWidget(self.mainFrame)
        self.verticalLayout_3.setStretch(1, 9)

        self.retranslateUi(ECGPatient)
        QtCore.QMetaObject.connectSlotsByName(ECGPatient)

    def retranslateUi(self, ECGPatient):
        _translate = QtCore.QCoreApplication.translate
        ECGPatient.setWindowTitle(_translate("ECGPatient", "Frame"))
        self.label_4.setText(_translate("ECGPatient", "Lo???i ??i???n ?????:"))
        self.comboECGType.setItemText(0, _translate("ECGPatient", "??i???n T??m ?????"))
        self.comboECGType.setItemText(1, _translate("ECGPatient", "??i???n N??o ?????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ECGPatient = QtWidgets.QFrame()
    ui = Ui_ECGPatient()
    ui.setupUi(ECGPatient)
    ECGPatient.show()
    sys.exit(app.exec_())
