from DAL.DAL_ECG import DAL_ECG

class BUS_ECG():
    def __init__(self):
        self.dalECG = DAL_ECG()

    def loadAllData(self):
        return self.dalECG.selectAllECG()

    def loadDataWithType(self, ECGType):
        return self.dalECG.selectECGWithType(ECGType=ECGType)

    def getLinkECG(self, IDPatient):
        return self.dalECG.selectLinkNRI(IDPatient=IDPatient)

    def uploadECG(self, IDPatient, ECGType, LinkECG):
        try:
            self.dalECG.updateECG(IDPatient=IDPatient, ECGType=ECGType, LinkECG=LinkECG)
            return 1
        except:
            return 0

    def searchPatient(self, State, IDPatient="", FullName=""):
        if(State == 0):
            return self.dalECG.searchPatientWithIDPatient(IDPatient=IDPatient)
        elif(State == 1):
            return self.dalECG.searchPatientWithFullName(FullName=FullName)
        else:
            return None