# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/Design/UI_SystemPIN.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SystemPIN(object):
    def setupUi(self, SystemPIN):
        SystemPIN.setObjectName("SystemPIN")
        SystemPIN.resize(1200, 611)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(SystemPIN)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(SystemPIN)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(SystemPIN)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(SystemPIN)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(SystemPIN)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.txtOldPIN = QtWidgets.QLineEdit(SystemPIN)
        self.txtOldPIN.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtOldPIN.setFont(font)
        self.txtOldPIN.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtOldPIN.setReadOnly(False)
        self.txtOldPIN.setObjectName("txtOldPIN")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtOldPIN)
        self.txtNewPIN = QtWidgets.QLineEdit(SystemPIN)
        self.txtNewPIN.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtNewPIN.setFont(font)
        self.txtNewPIN.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtNewPIN.setReadOnly(False)
        self.txtNewPIN.setObjectName("txtNewPIN")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtNewPIN)
        self.txtNewPINVerify = QtWidgets.QLineEdit(SystemPIN)
        self.txtNewPINVerify.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtNewPINVerify.setFont(font)
        self.txtNewPINVerify.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtNewPINVerify.setReadOnly(False)
        self.txtNewPINVerify.setObjectName("txtNewPINVerify")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtNewPINVerify)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btChangePIN = QtWidgets.QPushButton(SystemPIN)
        self.btChangePIN.setMinimumSize(QtCore.QSize(161, 30))
        self.btChangePIN.setMaximumSize(QtCore.QSize(161, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btChangePIN.setFont(font)
        self.btChangePIN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btChangePIN.setObjectName("btChangePIN")
        self.verticalLayout.addWidget(self.btChangePIN)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 6)
        self.horizontalLayout_3.setStretch(2, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.verticalLayout_3.setStretch(2, 9)

        self.retranslateUi(SystemPIN)
        QtCore.QMetaObject.connectSlotsByName(SystemPIN)

    def retranslateUi(self, SystemPIN):
        _translate = QtCore.QCoreApplication.translate
        SystemPIN.setWindowTitle(_translate("SystemPIN", "Frame"))
        self.label.setText(_translate("SystemPIN", "CÀI ĐẶT MÃ PIN HỆ THỐNG"))
        self.label_3.setText(_translate("SystemPIN", "Mã PIN Cũ:"))
        self.label_4.setText(_translate("SystemPIN", "Mã PIN Mới:"))
        self.label_5.setText(_translate("SystemPIN", "XT Mã PIN Mới:"))
        self.btChangePIN.setText(_translate("SystemPIN", "Thay Đổi Mật Khẩu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SystemPIN = QtWidgets.QFrame()
    ui = Ui_SystemPIN()
    ui.setupUi(SystemPIN)
    SystemPIN.show()
    sys.exit(app.exec_())
