from PyQt5.QtWidgets import QFrame
from GUI.View.Ui_Preclinical import Ui_Preclinical
from GUI.Logic.MRIPatient import MRIPatient
from GUI.Logic.CTScanPatient import CTScanPatient
from GUI.Logic.XRayPatient import XRayPatient
from GUI.Logic.UltraSonicPatient import UltraSonicPatient
from GUI.Logic.TestPatient import TestPatient
from GUI.Logic.ECGPatient import ECGPatient

class Preclinical(QFrame, Ui_Preclinical):
    def __init__(self, IDPatient, FullName, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)
    
        self.IDPatient = IDPatient
       
        self.setWindowTitle("Cận Lâm Sàng - " + IDPatient + " - " + FullName)

        # Event Handle
        self.tabPreclinical.tabBarClicked.connect(self.tabBarClicked)

    def cleanWidget(self):
        #self.mainFrame.hide()
        while self.mainLayout.count():
            childFrame = self.mainLayout.takeAt(0)
            if childFrame.widget():
                childFrame.widget().deleteLater()
    
    def openUi(self, ui):
        self.mainLayout.addWidget(ui)
        self.mainFrame.show()

    def tabBarClicked(self, index):
        self.cleanWidget()
        if(index == 0): 
            self.uiFrame = XRayPatient(IDPatient=self.IDPatient)
            self.openUi(ui=self.uiFrame)
        if(index == 1):
            self.uiFrame = CTScanPatient(IDPatient=self.IDPatient)
            self.openUi(ui=self.uiFrame)
        if(index == 2):
            self.uiFrame = MRIPatient(IDPatient=self.IDPatient)
            self.openUi(ui=self.uiFrame)
        if(index == 3): #Ultrasonic
            self.uiFrame = UltraSonicPatient(IDPatient=self.IDPatient)
            self.openUi(ui=self.uiFrame)
        if(index == 4): #Test
            self.uiFrame = TestPatient(IDPatient=self.IDPatient)
            self.openUi(ui=self.uiFrame)
        if(index == 5): #ECG
            self.uiFrame = ECGPatient(IDPatient=self.IDPatient)
            self.openUi(ui=self.uiFrame)

