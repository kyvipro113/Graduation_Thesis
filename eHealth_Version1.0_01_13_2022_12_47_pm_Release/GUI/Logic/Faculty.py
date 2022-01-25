from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFrame
from GUI.Logic.Noticfication import *
from GUI.View.Ui_Faculty import Ui_Faculty
from BUS.BUS_Faculty import BUS_Faculty

class Faculty(QFrame, Ui_Faculty):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.busFaculty = BUS_Faculty()

        # Event Handle
        self.dataTabFaculty.cellClicked.connect(self.cellClickOnDataTabFaculty)
        self.btAdd.clicked.connect(self.addFaculty)
        self.btUpdate.clicked.connect(self.updateFaculty)
        self.btDel.clicked.connect(self.deleteFaculty)
        self.btRefresh.clicked.connect(self.clearText)

        self.loadData()

    def loadData(self):
        dataFaculty = self.busFaculty.loadData()
        self.dataTabFaculty.setRowCount(0)
        for row_number, row_data in enumerate(dataFaculty):
            self.dataTabFaculty.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabFaculty.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
        self.dataTabFaculty.resizeColumnsToContents()

    def addFaculty(self):
        if(self.txtIDFaculty.text() == ""):
            IDFaculty = ""
            IDF = 0
            with open("Config/faculty.cfg", "r+") as file:
                for data in file:
                    ID = int(data.strip())
                    ID += 1
                    IDF = ID
                    if(ID > 0 and ID < 10):
                        IDFaculty = "KH0" + str(ID)
                    else:
                        IDFaculty = "KH" + str(ID) 

            self.txtIDFaculty.setText(IDFaculty)
            if(self.txtFacultyName.text() != ""):
                result = self.busFaculty.addNewFaculty(IDFaculty=IDFaculty, FacultyName=self.txtFacultyName.text())
                if(result == 1):
                    with open("Config/faculty.cfg", "w+") as file:
                        file.write(str(IDF) + "\n")
                    self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
                else:
                    self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Không được để trống các trường!", icon_type=1)    
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Khoa đã có trên hệ thống!", icon_type=1)
        self.loadData()  
        self.clearText()  
    
    def updateFaculty(self):
        if(self.txtIDFaculty.text() != "" and self.txtFacultyName.text() != ""):
            result = self.busFaculty.fixFaculty(IDFaculty=self.txtIDFaculty.text(), FacultyName=self.txtFacultyName.text())
            if(result == 1):
                self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Không được để trống các trường!", icon_type=1)
        self.loadData()
        self.clearText()

    def deleteFaculty(self):
        if(self.lbTotalEmployee.text() == "0"):
            if(self.txtIDFaculty.text() != ""):
                result = self.busFaculty.delFaculty(IDFaculty=self.txtIDFaculty.text())
                if(result == 1):
                    self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
                else:
                    self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn khoa để xóa!", icon_type=1)
            self.txtIDFaculty.setText("")
            self.txtFacultyName.setText("")
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Không thể xóa khoa có nhân viên!", icon_type=1)
        self.loadData()
        self.clearText()

    def cellClickOnDataTabFaculty(self):
        row = self.dataTabFaculty.currentRow()
        ID = self.dataTabFaculty.item(row, 0).text()
        data = self.busFaculty.cellClickFaculty(IDFaculty=ID)
        self.txtIDFaculty.setText(data[0])
        self.txtFacultyName.setText(data[1])
        self.lbTotalEmployee.setText(str(data[2]))

    def clearText(self):
        self.txtIDFaculty.setText("")
        self.txtFacultyName.setText("")
        self.lbTotalEmployee.setText("0")