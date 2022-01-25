from PyQt5.QtCore import left
from PyQt5.QtWidgets import QFrame
from GUI.View.Ui_CreateAccount import Ui_CreateAccount
from GUI.Logic.Noticfication import Notification
from BUS.BUS_CreateAccount import BUS_CreateAccount
from PyQt5 import QtWidgets

class CreateAccount(QFrame, Ui_CreateAccount):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.busCreateAccount = BUS_CreateAccount()
        self.IDPermission = 1
        self.lbIDEmployee.setText("")

        # Event Handle
        self.comboPmission.currentTextChanged.connect(self.selectPermission)
        self.dataTabEmployeeNotHaveAcc.cellClicked.connect(self.cellClickOnDataTabEmpHaveNotAcc)
        self.dataTabEmployeeHaveAcc.cellClicked.connect(self.cellClickOnDataTableHaveAcc)
        self.btUpdate.clicked.connect(self.updateAccount)
        self.btDelete.clicked.connect(self.deleteAccount)

        self.loadData()


    def loadData(self):
        dataEmpHaveNotAcc, dataEmpHaveAcc = self.busCreateAccount.loadData()
        # Employee Have Not Account
        self.dataTabEmployeeNotHaveAcc.setRowCount(0)
        for row_number, row_data in enumerate(dataEmpHaveNotAcc):
            self.dataTabEmployeeNotHaveAcc.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabEmployeeNotHaveAcc.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
        self.dataTabEmployeeNotHaveAcc.resizeColumnsToContents()

        # Employee Have Account
        self.dataTabEmployeeHaveAcc.setRowCount(0)
        for row_number, row_data in enumerate(dataEmpHaveAcc):
            self.dataTabEmployeeHaveAcc.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabEmployeeHaveAcc.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
                if(col_number == 0):
                    dataFullName = self.busCreateAccount.loadFullName(IDEmployee=data)
                    self.dataTabEmployeeHaveAcc.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(dataFullName[0])))
                if(col_number == 2):
                    dataPermissName = self.busCreateAccount.loadPermissionName(IDPermission=data)
                    self.dataTabEmployeeHaveAcc.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(dataPermissName[0])))
        self.dataTabEmployeeHaveAcc.resizeColumnsToContents()
    
    def cellClickOnDataTabEmpHaveNotAcc(self):
        row = self.dataTabEmployeeNotHaveAcc.currentRow()
        self.lbIDEmployee.setText(self.dataTabEmployeeNotHaveAcc.item(row, 0).text())
        self.lbFullName.setText(self.dataTabEmployeeNotHaveAcc.item(row, 1).text())

    def cellClickOnDataTableHaveAcc(self):
        row = self.dataTabEmployeeHaveAcc.currentRow()
        self.lbFullName.setText(self.dataTabEmployeeHaveAcc.item(row, 0).text())
        dataID = self.busCreateAccount.loadIDEmployee(FullName=self.lbFullName.text())
        self.lbIDEmployee.setText(dataID[0])
        self.txtUsername.setText(self.dataTabEmployeeHaveAcc.item(row, 1).text())
        self.comboPmission.setCurrentText(self.dataTabEmployeeHaveAcc.item(row, 2).text())
        self.selectPermission()
        print(self.IDPermission)

    def selectPermission(self):
        if(self.comboPmission.currentText() == "Adminstrator"):
            self.IDPermission = 1
        if(self.comboPmission.currentText() == "Bác Sỹ"):
            self.IDPermission = 2
        if(self.comboPmission.currentText() == "KTV - Cận Lâm Sàng"):
            self.IDPermission = 3
        if(self.comboPmission.currentText() == "Tiếp Tân"):
            self.IDPermission = 4

    def updateAccount(self):
        if(self.lbIDEmployee.text() != ""):
            result = self.busCreateAccount.updateAccount(IDEmployee=self.lbIDEmployee.text(), username=self.txtUsername.text(), password=self.txtPassword.text(), IDPermission=self.IDPermission)
            if(result == 1):
                self.noticfication = Notification(title="Thông báo", message="Thao Tác Thực Hiện Thành Công!")
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Thao Tác Thực Hiện Thất Bại!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa Chọn Nhân Viên", icon_type=1)
        self.loadData()

    def deleteAccount(self):
        if(self.lbIDEmployee.text() != ""):
            result = self.busCreateAccount.deleteAccount(IDEmployee=self.lbIDEmployee.text())
            if(result == 1):
                self.txtUsername.setText("")
                self.noticfication = Notification(title="Thông báo", message="Thao Tác Thực Hiện Thành Công!")
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Thao Tác Thực Hiện Thất Bại!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa Chọn Nhân Viên", icon_type=1)
        self.loadData()
            