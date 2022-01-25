from DAL.DAL_CTScanPatient import DAL_CTScanPatient

class BUS_CTScanPatient():
    def __init__(self):
        self.dalCTScanPatient = DAL_CTScanPatient()

    def firstLoadLinkCTScan(self, IDPatient):
        return self.dalCTScanPatient.selectLinkCTScanViaIDPatient(IDPatient=IDPatient)

    def loadLinkCTScan(self, IDPatient, CTScanType):
        return self.dalCTScanPatient.selectLinkCTScan(IDPatient=IDPatient, CTScanType=CTScanType)