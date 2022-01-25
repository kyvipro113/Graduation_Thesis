from PyQt5.QtWidgets import QFrame
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from GUI.View.Ui_MedicalRecord import Ui_MedicalRecord
from GUI.Logic.MedicalRecordPatient import MedicalRecordPatient
from GUI.Logic.Noticfication import *
from BUS.BUS_MedicalRecord import BUS_MedicalRecord
from GUI.Logic.Noticfication import *
from GUI.Logic.CreateMedicalRecord import CreateMedicalRecordPatient
from GUI.Logic.UpdateMedicalRecord import UpdateMedicalRecord

class MedicalRecord(QFrame, Ui_MedicalRecord):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)
        
        self.busMedicalRecord = BUS_MedicalRecord()
 
        self.listIDPatientExist = None
        self.IDMedicalRecord = ""
        self.IDPatient = ""
        self.FullName = ""

        self.loadData()

        # Event Handle
        self.dataTabPatient.cellClicked.connect(self.cellClickDataTabPatient)
        self.dataTabMedicalRecord.cellClicked.connect(self.cellClickOnDataTabMedicalRecord)
        self.btView.clicked.connect(self.openUiMedicalRecordPatient)
        self.btAdd.clicked.connect(self.openUiCreateMedicalRecordPatient)
        self.btUpdate.clicked.connect(self.openUiUpdateMedicalRecordPatient)
        self.btDel.clicked.connect(self.deleteMedicalRecord)

    def openUiMedicalRecordPatient(self):
        if(self.IDPatient != "" and self.IDMedicalRecord != ""):
            self.ui = MedicalRecordPatient(IDPatient=self.IDPatient, IDMedicalRecord=self.IDMedicalRecord)
            self.mainMDI.addSubWindow(self.ui)
            self.ui.show()
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn bệnh án để mở", icon_type=1)

    def openUiCreateMedicalRecordPatient(self):
        if(self.IDPatient != ""):
            if(self.IDPatient not in self.listIDPatientExist):
                self.uiCreateMRPatient = CreateMedicalRecordPatient(IDPatient=self.IDPatient, FullName=self.FullName)
                self.mainMDI.addSubWindow(self.uiCreateMRPatient)
                self.uiCreateMRPatient.signal.connect(self.slotLoadData)
                self.uiCreateMRPatient.show()
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Bệnh đã tồn tại trên hệ thống", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn bệnh nhân!", icon_type=1)

    def openUiUpdateMedicalRecordPatient(self):
        if(self.IDPatient != "" and self.IDMedicalRecord != ""):
            self.uiUpdateMRPatient = UpdateMedicalRecord(IDPatient=self.IDPatient, IDMedicalRecord=self.IDMedicalRecord)
            self.mainMDI.addSubWindow(self.uiUpdateMRPatient)
            self.uiUpdateMRPatient.signal.connect(self.slotLoadData)
            self.uiUpdateMRPatient.show()
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn bệnh án!", icon_type=1)

    def loadData(self):
        self.listIDPatientExist = []
        dataP = self.busMedicalRecord.loadPatientData()
        self.dataTabPatient.setRowCount(0)
        for row_number, row_data in enumerate(dataP):
            self.dataTabPatient.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
        self.dataTabPatient.resizeColumnsToContents()
        
        dataMR = self.busMedicalRecord.loadMedicalRecordData()
        self.dataTabMedicalRecord.setRowCount(0)
        for row_number, row_data in enumerate(dataMR):
            self.dataTabMedicalRecord.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabMedicalRecord.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
                if(col_number == 1):
                    self.listIDPatientExist.append(data)
        self.dataTabMedicalRecord.resizeColumnsToContents()

    def cellClickDataTabPatient(self):
        self.IDMedicalRecord = ""
        row = self.dataTabPatient.currentRow()
        self.IDPatient = self.dataTabPatient.item(row, 0).text()
        self.FullName = self.dataTabPatient.item(row, 1).text()
        self.lbIDPatient.setText(self.IDPatient)

    def cellClickOnDataTabMedicalRecord(self):
        row = self.dataTabMedicalRecord.currentRow()
        self.IDMedicalRecord = self.dataTabMedicalRecord.item(row, 0).text()
        self.IDPatient = self.dataTabMedicalRecord.item(row, 1).text()
        self.lbIDPatient.setText(self.IDPatient)

    QtCore.pyqtSlot(int)
    def slotLoadData(self, result):
        if(result == 1):
            self.loadData()

    def deleteMedicalRecord(self):
        if(self.IDMedicalRecord != ""):
            result = self.busMedicalRecord.deleteMedicalRecord(IDMedicalRecord=self.IDMedicalRecord)
            if(result == 1):
                self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Thao thác thực hiện thất bại!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn bệnh án!", icon_type=1)
        self.loadData()
