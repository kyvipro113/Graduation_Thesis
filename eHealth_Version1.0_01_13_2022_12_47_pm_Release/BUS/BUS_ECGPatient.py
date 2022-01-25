from DAL.DAL_ECGPatient import DAL_ECGPatient

class BUS_ECGPatient():
    def __init__(self):
        self.dalECGPatient = DAL_ECGPatient()

    def firstLoadLinkECG(self, IDPatient):
        return self.dalECGPatient.selectLinkECGViaIDPatient(IDPatient=IDPatient)

    def loadLinkECG(self, IDPatient, ECGType):
        return self.dalECGPatient.selectLinkECG(IDPatient=IDPatient, ECGType=ECGType)