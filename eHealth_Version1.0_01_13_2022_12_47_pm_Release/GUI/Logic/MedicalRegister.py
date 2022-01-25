from PyQt5.QtWidgets import QFrame
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from GUI.View.Ui_MedicalRegister import Ui_MedicalRegister
from GUI.Logic.Noticfication import *
from BUS.BUS_MedicalRegister import BUS_MedicalRegister
from DTO.DTO_Patient import DTO_Patient
from GUI.Logic.Noticfication import *
import datetime

class MedicalRegister(QFrame, Ui_MedicalRegister):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        dateSet = QDate(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
        self.deTime.setDate(dateSet)

        self.dtoPatient = DTO_Patient()
        self.busMedicalRegister = BUS_MedicalRegister()
        self.dtoPatient.Time = str(datetime.date.today().month) + "/" + str(datetime.date.today().day) + "/" + str(datetime.date.today().year)

        #Event Handle
        self.comboFaculty.currentTextChanged.connect(self.getEmployeeInFaculty)
        self.comboEmployee.currentTextChanged.connect(self.getIDEmployee)
        self.deTime.dateChanged.connect(self.onChangeDate)
        self.btAdd.clicked.connect(self.addPatientRegister)
        self.btUpdate.clicked.connect(self.updatePatientRegister)
        self.btDel.clicked.connect(self.deletePatientRegister)
        self.btRefresh.clicked.connect(self.clearText)
        self.dataTabMedicalRegister.cellClicked.connect(self.cellClickOnDataTabPatient)

        self.loadData()
        self.getFaculty()
        
    def loadData(self):
        dataMedicalRegister = self.busMedicalRegister.loadData()
        self.dataTabMedicalRegister.setRowCount(0)
        for row_number, row_data in enumerate(dataMedicalRegister):
            self.dataTabMedicalRegister.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabMedicalRegister.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
                if(col_number == 11):
                    dataF = self.busMedicalRegister.getNameFaculty(IDFaculty=str(data))
                    self.dataTabMedicalRegister.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(dataF)))
                if(col_number == 12):
                    dataE = self.busMedicalRegister.getNameEmployee(IDEmployee=str(data))
                    self.dataTabMedicalRegister.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(dataE)))
        self.dataTabMedicalRegister.resizeColumnsToContents()

    def getFaculty(self):
        dataFaculty = self.busMedicalRegister.getFaculty()
        for data in dataFaculty:
            self.comboFaculty.addItem(data[0])

    def getEmployeeInFaculty(self, value):
        dataIDFaculty = self.busMedicalRegister.getIDFaculty(FacultyName=value)
        self.dtoPatient.IDFaculty = dataIDFaculty[0]
        dataEmployee = self.busMedicalRegister.getEmployeeInFaculty(dataIDFaculty[0])
        self.comboEmployee.clear()
        for data in dataEmployee:
            self.comboEmployee.addItem(data[0])
        self.comboEmployee.setCurrentIndex(0)

    def getIDEmployee(self):
        dataIDEmp = self.busMedicalRegister.getIDEmployee(FullName=self.comboEmployee.currentText())
        if(dataIDEmp is not None):
            print(dataIDEmp)
            self.dtoPatient.IDEmployee = dataIDEmp[0]

    def cellClickOnDataTabPatient(self):
        row = self.dataTabMedicalRegister.currentRow()
        item = self.dataTabMedicalRegister.item(row, 0).text()
        self.txtIDPatient.setText(item)
        item = self.dataTabMedicalRegister.item(row, 1).text()
        self.txtFullName.setText(item)
        item = self.dataTabMedicalRegister.item(row, 2).text()
        self.txtOld.setText(item)
        item = self.dataTabMedicalRegister.item(row, 3).text()
        self.comboGender.setCurrentText(item)
        item = self.dataTabMedicalRegister.item(row, 4).text()
        self.txtEthnic.setText(item)
        item = self.dataTabMedicalRegister.item(row, 5).text()
        self.txtJob.setText(item)
        item = self.dataTabMedicalRegister.item(row, 6).text()
        self.txtAddress.setText(item)
        item = self.dataTabMedicalRegister.item(row, 7).text()
        self.txtNumberPhone.setText(item)
        item = self.dataTabMedicalRegister.item(row, 8).text()
        self.txtCitizenID.setText(item)
        item = self.dataTabMedicalRegister.item(row, 9).text()
        self.txtIDHealthInsurance.setText(item)
        item = self.dataTabMedicalRegister.item(row, 10).text()
        self.txtDiagnoseRequest.setText(item)
        item = self.dataTabMedicalRegister.item(row, 11).text()
        self.comboFaculty.setCurrentText(item)
        item = self.dataTabMedicalRegister.item(row, 12).text()
        self.comboEmployee.setCurrentText(item)
        item = self.dataTabMedicalRegister.item(row, 13).text()
        item = item.split("-")
        dateSet = QDate(int(item[0]), int(item[1]), int(item[2]))
        self.deTime.setDate(dateSet)
        self.onChangeDate(dateSet)
        

    def onChangeDate(self, QDate):
        self.dtoPatient.Time = str(QDate.month()) + "/" +str(QDate.day()) + "/" +str(QDate.year())

    def addPatientRegister(self):
        if(self.txtIDPatient.text() == ""):
            if(self.checkEmpty() == 1):
                IDP = 0
                with open("Config/medicalregister.cfg", "r+") as file:
                    for data in file:
                        ID = int(data.strip())
                        ID += 1
                        IDP = ID
                        if(ID > 0 and ID < 10):
                            self.dtoPatient.IDPatient = "BN0" + str(ID)
                        else:
                            self.dtoPatient.IDPatient = "BN" + str(ID)
                self.dtoPatient.FullName = self.txtFullName.text()
                self.dtoPatient.Old = self.txtOld.text()
                self.dtoPatient.Gender = self.comboGender.currentText()
                self.dtoPatient.Ethnic = self.txtEthnic.text()
                self.dtoPatient.Job = self.txtJob.text()
                self.dtoPatient.Address = self.txtAddress.text()
                self.dtoPatient.NumberPhone = self.txtNumberPhone.text()
                self.dtoPatient.CitizenID = self.txtCitizenID.text()
                self.dtoPatient.IDHealthInsurance = self.txtIDHealthInsurance.text()
                self.dtoPatient.RequestDiagnose = self.txtDiagnoseRequest.text()
                #self.dtoPatient.TestPrint()
                result = self.busMedicalRegister.addPatientRegister(dtoPatient=self.dtoPatient)
                if(result == 1):
                    with open("Config/medicalregister.cfg", "w+") as file:
                        file.write(str(IDP) + "\n")
                    self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
                else:
                    self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Bệnh nhân đã có trên hệ thống!", icon_type=1)
        self.loadData()
        self.clearText()

    def updatePatientRegister(self):
        if(self.checkEmpty() == 1):
            self.dtoPatient.IDPatient = self.txtIDPatient.text()
            self.dtoPatient.FullName = self.txtFullName.text()
            self.dtoPatient.Old = self.txtOld.text()
            self.dtoPatient.Gender = self.comboGender.currentText()
            self.dtoPatient.Ethnic = self.txtEthnic.text()
            self.dtoPatient.Job = self.txtJob.text()
            self.dtoPatient.Address = self.txtAddress.text()
            self.dtoPatient.NumberPhone = self.txtNumberPhone.text()
            self.dtoPatient.CitizenID = self.txtCitizenID.text()
            self.dtoPatient.IDHealthInsurance = self.txtIDHealthInsurance.text()
            self.dtoPatient.RequestDiagnose = self.txtDiagnoseRequest.text()
            #self.dtoPatient.TestPrint()
            result = self.busMedicalRegister.updatePatientRegister(dtoPatient=self.dtoPatient)
            if(result == 1):
                self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Không được để trống các trường quan trọng!", icon_type=1)
        self.loadData()
        self.clearText()

    def deletePatientRegister(self):
        if(self.txtIDPatient.text() != ""):
            result = self.busMedicalRegister.deleteMedicalRegister(IDPatient=self.txtIDPatient.text())
            if(result == 1):
                self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn bệnh nhân để xóa!", icon_type=1)
        self.loadData()
        self.clearText()

    def checkEmpty(self):
        if(self.txtFullName.text != "" and self.txtOld.text() != "" and self.txtCitizenID.text() != "" and self.txtDiagnoseRequest.text() != ""):
            return 1
        else:
            return 0

    def clearText(self):
        self.txtIDPatient.setText("")
        self.txtFullName.setText("")
        self.txtOld.setText("")
        self.comboGender.setCurrentIndex(0)
        self.txtEthnic.setText("")
        self.txtJob.setText("")
        self.txtAddress.setText("")
        self.txtNumberPhone.setText("")
        self.txtCitizenID.setText("")
        self.txtIDHealthInsurance.setText("")
        self.txtDiagnoseRequest.setText("")
        self.comboFaculty.setCurrentIndex(0)
        self.comboEmployee.setCurrentIndex(0)
        dateSet = QDate(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
        self.deTime.setDate(dateSet)