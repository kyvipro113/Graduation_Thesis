from PyQt5.QtWidgets import QMainWindow
from GUI.View.Ui_MainWindow import Ui_MainWindow
from GUI.Logic.Account import Account
from GUI.Logic.MedicalRegister import MedicalRegister
from GUI.Logic.Patient import Patient
from GUI.Logic.MedicalRecord import MedicalRecord
from GUI.Logic.XRay import XRay
from GUI.Logic.CTScan import CTScan
from GUI.Logic.MRI import MRI
from GUI.Logic.UltraSonic import UltraSonic
from GUI.Logic.Test import Test
from GUI.Logic.ECG import ECG
from GUI.Logic.Faculty import Faculty
from GUI.Logic.Position import Position
from GUI.Logic.Employee import Employee
from GUI.Logic.Search import Search
from GUI.Logic.StatisticVisit import StatisticVisit
from GUI.Logic.StatisticUsingAI import StatisticUsingAI
from GUI.Logic.StatisticCovid import StatisticCovid
from GUI.Logic.CreateAccount import CreateAccount
from GUI.Logic.SystemPIN import SystemPIN


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, IDEmployee, FullName, IDPermission, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.statusBar().showMessage("Đăng nhập thành công!", 2000)

        self.IDEmployee = IDEmployee
        self.IDPermission = IDPermission
        self.lbHello.setText("Xin chào: " + FullName)

        # Event Handle
        self.btAccount.clicked.connect(self.openUiAccount)
        self.btLogout.clicked.connect(self.logout)
        self.btRegister.clicked.connect(self.openUiMedicalRegister)
        self.btPatient.clicked.connect(self.openUiPatient)
        self.btMedicalRecord.clicked.connect(self.openUiMedicalRecord)
        self.btXrays.clicked.connect(self.openUiXRays)
        self.btCTScan.clicked.connect(self.openUiCTScan)
        self.btMRI.clicked.connect(self.openUiMRI)
        self.btUltrasonic.clicked.connect(self.openUiUltraSonic)
        self.btTest.clicked.connect(self.openUiTest)
        self.btECG.clicked.connect(self.openUiECG)
        self.btFaculty.clicked.connect(self.openUiFaculty)
        self.btEmployee.clicked.connect(self.openUiEmployee)
        self.btPosition.clicked.connect(self.openUiPosition)
        self.btSearch.clicked.connect(self.openUiSearch)
        self.btVisits.clicked.connect(self.openUiStatisticVisit)
        self.btStatisticAI.clicked.connect(self.openUiStatisticUsingAI)
        self.btStatisticCovid.clicked.connect(self.openUiStatisticCovid)
        self.btCreateAccount.clicked.connect(self.openUiCreateAccount)
        self.btSystemPINSettings.clicked.connect(self.openUiSystemPIN)

    def cleanWidget(self):
        self.mainFrame.hide()
        while self.mainLayout.count():
            childFrame = self.mainLayout.takeAt(0)
            if childFrame.widget():
                childFrame.widget().deleteLater()

    def openUiAccount(self):
        self.cleanWidget()
        self.uiFrame = Account(IDEmployee=self.IDEmployee)
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()
    
    def openUiMedicalRegister(self):
        self.cleanWidget()
        self.uiFrame = MedicalRegister()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiPatient(self):
        self.cleanWidget()
        self.uiFrame = Patient(IDEmployee=self.IDEmployee)
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiMedicalRecord(self):
        self.cleanWidget()
        self.uiFrame = MedicalRecord()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiXRays(self):
        self.cleanWidget()
        self.uiFrame = XRay()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiCTScan(self):
        self.cleanWidget()
        self.uiFrame = CTScan()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiMRI(self):
        self.cleanWidget()
        self.uiFrame = MRI()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiUltraSonic(self):
        self.cleanWidget()
        self.uiFrame = UltraSonic()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiTest(self):
        self.cleanWidget()
        self.uiFrame = Test()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()
    
    def openUiECG(self):
        self.cleanWidget()
        self.uiFrame = ECG()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiFaculty(self):
        self.cleanWidget()
        self.uiFrame = Faculty()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiEmployee(self):
        self.cleanWidget()
        self.uiFrame = Employee()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiPosition(self):
        self.cleanWidget()
        self.uiFrame = Position()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()
    
    def openUiSearch(self):
        self.cleanWidget()
        self.uiFrame = Search()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiStatisticVisit(self):
        self.cleanWidget()
        self.uiFrame = StatisticVisit()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiStatisticCovid(self):
        self.cleanWidget()
        self.uiFrame = StatisticCovid()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiStatisticUsingAI(self):
        self.cleanWidget()
        self.uiFrame = StatisticUsingAI()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiCreateAccount(self):
        self.cleanWidget()
        self.uiFrame = CreateAccount()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def openUiSystemPIN(self):
        self.cleanWidget()
        self.uiFrame = SystemPIN()
        self.mainLayout.addWidget(self.uiFrame)
        self.mainFrame.show()

    def logout(self):
        import os
        import sys
        os.execl(sys.executable, sys.executable, *sys.argv)
