from PyQt5 import QtWidgets
from PyQt5.QtCore import reset
from PyQt5.QtWidgets import QFrame
from GUI.Logic.Noticfication import *
from GUI.View.Ui_Position import Ui_Position
from BUS.BUS_Position import BUS_Position

class Position(QFrame, Ui_Position):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.busPosition = BUS_Position()

        # Event Handle
        self.btAdd.clicked.connect(self.addPosition)
        self.btUpdate.clicked.connect(self.updatePosition)
        self.btDel.clicked.connect(self.deletePosition)
        self.dataTabPosition.cellClicked.connect(self.cellClickOnDataTabPosition)
        self.btRefresh.clicked.connect(self.clearText)

        self.loadData()


    def loadData(self):
        dataPosition = self.busPosition.loadData()
        self.dataTabPosition.setRowCount(0)
        for row_number, row_data in enumerate(dataPosition):
            self.dataTabPosition.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabPosition.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
        self.dataTabPosition.resizeColumnsToContents()

    def addPosition(self):
        if(self.txtIDPosition.text() == ""):
            IDPosition = ""
            IDP = 0
            with open("Config/position.cfg", "r+") as file:
                for data in file:
                    ID = int(data.strip())
                    ID += 1
                    IDP = ID
                    if(ID > 0 and ID < 10):
                        IDPosition = "CV0" + str(ID)
                    else:
                        IDPosition = "CV" + str(ID)
            
            self.txtIDPosition.setText(IDPosition)
            if(self.txtPositionName.text() != ""):
                result = self.busPosition.addNewPosition(IDPosition=IDPosition, PositionName=self.txtPositionName.text())
                if result == 1:
                    with open("Config/position.cfg", "w+") as file:
                        file.write(str(IDP) + "\n")
                    self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
                else:
                    self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Không được để trống các trường!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chức vụ đã có trên hệ thống!", icon_type=1)
        self.loadData()
        self.clearText()
           
    def updatePosition(self):
        if(self.txtIDPosition.text() != "" and self.txtPositionName.text() != ""):
            result = self.busPosition.fixPosition(IDPosition=self.txtIDPosition.text(), PositionName=self.txtPositionName.text())
            if(result == 1):
                self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Không được để trống các trường!", icon_type=1)
        self.loadData()
        self.clearText()

    def deletePosition(self):
        if(self.txtIDPosition.text() != ""):
            result = self.busPosition.delPosition(IDPosition=self.txtIDPosition.text())
            if(result == 1):
                self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Không thể xóa do còn nhân viên trong khoa!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn khoa để xóa!", icon_type=1)
        self.loadData()
        self.clearText()

    def cellClickOnDataTabPosition(self):
        row = self.dataTabPosition.currentRow()
        item = self.dataTabPosition.item(row, 0).text()
        self.txtIDPosition.setText(item)
        item = self.dataTabPosition.item(row, 1).text()
        self.txtPositionName.setText(item)

    def clearText(self):
        self.txtIDPosition.setText("")
        self.txtPositionName.setText("")