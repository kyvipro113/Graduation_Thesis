from PyQt5.QtWidgets import QFrame
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from GUI.View.Ui_Prescription import Ui_Prescription
import datetime
from DTO.DTO_Prescription import DTO_Prescription
from BUS.BUS_Prescription import BUS_Prescription
from GUI.Logic.Noticfication import *

class Prescription(QFrame, Ui_Prescription):
    def __init__(self, IDPatient, FullName, IDEmployee, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.dtoPrescription = DTO_Prescription()
        self.busPrescription = BUS_Prescription()

        self.IDPatient = IDPatient
        self.txtIDPatient.setText(IDPatient)
        self.IDEmployee = IDEmployee
        self.txtFullName.setText(FullName)
        self.setWindowTitle("Đơn Thuôc - " + IDPatient + " - " + FullName)

        dtSet = QDate(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
        self.deTime.setDate(dtSet)
        self.dtoPrescription.Time = str(datetime.date.today().month) + "/" + str(datetime.date.today().day) + "/" + str(datetime.date.today().year)

        # Event Handle
        self.deTime.dateChanged.connect(self.onChangeDate)
        self.btAdd.clicked.connect(self.addPrescription)
        self.btUpdate.clicked.connect(self.updatePrescription)
        self.btDel.clicked.connect(self.deletePrescription)
        self.btRefresh.clicked.connect(self.clearText)
        self.dataTabPresciption.cellClicked.connect(self.cellClickOnDataTabPrescription)

        self.loadData()

    def onChangeDate(self, QDate):
        self.dtoPrescription.Time = str(QDate.month()) + "/" +str(QDate.day()) + "/" +str(QDate.year())
        #print(self.dtoPrescription.Time) #Debug

    def addPrescription(self):
        if(self.txtIDPrescription.text() == ""):
            if(self.txtContent.toPlainText() != ""):
                IDP = 0
                with open("Config/prescription.cfg", "r+") as file:
                    for data in file:
                        ID = int(data.strip())
                        ID += 1
                        IDP = ID
                        if(ID > 0 and ID < 10):
                            self.dtoPrescription.IDPrescription = "DT0" + str(ID)
                        else:
                            self.dtoPrescription.IDPrescription = "DT" +str(ID)
                self.txtIDPrescription.setText(self.dtoPrescription.IDPrescription)
                self.dtoPrescription.IDPatient = self.IDPatient
                self.dtoPrescription.ContentPS = self.txtContent.toPlainText()
                self.dtoPrescription.IDEmployee = self.IDEmployee
                result = self.busPrescription.addPrescription(dtoPrescription=self.dtoPrescription)
                #self.dtoPrescription.TestPrint()
                if(result == 1):
                    with open("Config/prescription.cfg", "w+") as file:
                        file.write(str(IDP) + "\n")
                    self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
                else:
                    self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Không được để trống nội dung!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Đơn thuốc đã tồn tại!", icon_type=1)
        self.loadData()
        self.clearText()

    def updatePrescription(self):
        if(self.txtIDPrescription.text() != ""):
            self.dtoPrescription.IDPrescription = self.txtIDPrescription.text()
            self.dtoPrescription.IDPatient = self.IDPatient
            self.dtoPrescription.ContentPS = self.txtContent.toPlainText()
            self.dtoPrescription.IDEmployee = self.IDEmployee
            #self.dtoPrescription.TestPrint()
            result = self.busPrescription.updatePrescription(dtoPrescription=self.dtoPrescription)
            if(result == 1):
                self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn đơn thuốc!", icon_type=1)
        self.loadData()
        self.clearText()

    def deletePrescription(self):
        if(self.txtIDPatient.text() != ""):
            result = self.busPrescription.deletePrescription(IDPrescription=self.txtIDPrescription.text())
            if(result == 1):
                self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn đơn thuốc!", icon_type=1)
        self.loadData()
        self.clearText()

    def loadData(self):
        dataP = self.busPrescription.loadPrescription(IDPatient=self.IDPatient)
        self.dataTabPresciption.setRowCount(0)
        for row_number, row_data in enumerate(dataP):
            self.dataTabPresciption.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabPresciption.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
        self.dataTabPresciption.resizeColumnsToContents()

    def cellClickOnDataTabPrescription(self):
        row = self.dataTabPresciption.currentRow()
        item = self.dataTabPresciption.item(row, 0).text()
        self.txtIDPrescription.setText(item)
        item = self.dataTabPresciption.item(row, 1).text()
        self.txtContent.setText(item)
        item = self.dataTabPresciption.item(row, 2).text()
        item = item.split("-")
        dateSet = QDate(int(item[0]), int(item[1]), int(item[2]))
        self.deTime.setDate(dateSet)

    def clearText(self):
        self.txtIDPrescription.setText("")
        self.txtContent.setText("")
        dtSet = QDate(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
        self.deTime.setDate(dtSet)

