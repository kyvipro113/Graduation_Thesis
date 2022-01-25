from PyQt5.QtWidgets import QFrame
from PyQt5 import QtWidgets
from GUI.View.Ui_Patient import Ui_Patient
from GUI.Logic.Preclinical import Preclinical
from GUI.Logic.Noticfication import *
from DTO.DTO_Patient import DTO_Patient
from BUS.BUS_Patient import BUS_Patient
from GUI.Logic.Prescription import Prescription
from GUI.Logic.Preclinicalindications import PreclinicalIndications

class Patient(QFrame, Ui_Patient):
    def __init__(self, IDEmployee, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)
        self.IDEmployee = IDEmployee
        
        self.dtoPatient = DTO_Patient()
        self.busPatient = BUS_Patient()

        # self.ui = Preclinical()
        # self.mainMDI.addSubWindow(self.ui)

        # Event Handle
        self.checkAllPatient.stateChanged.connect(self.stateCheck)
        self.dataTabPatient.cellClicked.connect(self.cellClickOnDataTabPatient)
        self.btDiagnose.clicked.connect(self.updateDiagnose)
        self.btPreclinical.clicked.connect(self.openPreclinical)
        self.btPrescription.clicked.connect(self.openPrescription)
        self.btPreclinicalindications.clicked.connect(self.openPreclinicalIndications)

        self.loadDataOfEmployee()
        

    def loadDataToDataTab(self, dataP):
        self.dataTabPatient.setRowCount(0)
        for row_number, row_data in enumerate(dataP):
            self.dataTabPatient.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
        self.dataTabPatient.resizeColumnsToContents()

    def loadDataOfEmployee(self):
        dataPatient = self.busPatient.loadPatientOfEmployee(IDEmployee=self.IDEmployee)
        self.loadDataToDataTab(dataP=dataPatient)
        self.btDiagnose.setEnabled(True)
        self.btPreclinical.setEnabled(True)
        self.btPrescription.setEnabled(True)
        self.btPreclinicalindications.setEnabled(True)

    def loadAllData(self):
        dataPatient = self.busPatient.loadAllPatient()
        self.loadDataToDataTab(dataP=dataPatient)
        self.btDiagnose.setEnabled(False)
        self.btPreclinical.setEnabled(False)
        self.btPrescription.setEnabled(False)
        self.btPreclinicalindications.setEnabled(False)

    def stateCheck(self):
        if(self.checkAllPatient.isChecked()):
            self.loadAllData()
        else:
            self.loadDataOfEmployee()

    def cellClickOnDataTabPatient(self):
        row = self.dataTabPatient.currentRow()
        item = self.dataTabPatient.item(row, 0).text()
        self.dtoPatient.IDPatient = item
        self.txtIDPatient.setText(item)
        item = self.dataTabPatient.item(row, 1).text()
        self.txtFullName.setText(item)
        item = self.dataTabPatient.item(row, 3).text()
        self.txtDiagnose.setText(item)
        self.dtoPatient.Diagnose = item

    def updateDiagnose(self):
        if(self.txtIDPatient.text() != ""):
            self.dtoPatient.Diagnose = self.txtDiagnose.toPlainText()
            result = self.busPatient.updateDiagnose(dtoPatient=self.dtoPatient)
            if(result == 1):
                self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn bệnh nhân!", icon_type=1)
        self.loadDataOfEmployee()

    def openPrescription(self):
        if(self.txtIDPatient.text() != ""):
            self.uiPrescription = Prescription(IDPatient=self.txtIDPatient.text(), FullName=self.txtFullName.text(), IDEmployee=self.IDEmployee)
            self.mainMDI.addSubWindow(self.uiPrescription)
            self.uiPrescription.show()
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn bệnh nhân!", icon_type=1)
        
    def openPreclinical(self):
        if(self.txtIDPatient.text() != ""):
            self.uiPreclinical = Preclinical(IDPatient=self.txtIDPatient.text(), FullName= self.txtFullName.text())
            self.mainMDI.addSubWindow(self.uiPreclinical)
            self.uiPreclinical.show()
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn bệnh nhân!", icon_type=1)

    def openPreclinicalIndications(self):
        if(self.txtIDPatient.text() != ""):
            self.uiPreclinicalIndications = PreclinicalIndications(IDPatient=self.txtIDPatient.text(), FullName=self.txtFullName.text())
            self.mainMDI.addSubWindow(self.uiPreclinicalIndications)
            self.uiPreclinicalIndications.show()
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn bệnh nhân", icon_type=1)