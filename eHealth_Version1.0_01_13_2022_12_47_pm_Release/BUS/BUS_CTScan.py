from DAL.DAL_CTScan import DAL_CTScan

class BUS_CTScan():
    def __init__(self):
        self.dalCTScan = DAL_CTScan()

    def loadAllData(self):
        return self.dalCTScan.selectAllCTScan()

    def loadDataWithType(self, CTScanType):
        return self.dalCTScan.selectCTScanWithType(CTScanType=CTScanType)

    def getLinkCTScan(self, IDPatient):
        return self.dalCTScan.selectLinkNRI(IDPatient=IDPatient)

    def uploadCTScan(self, IDPatient, CTScanType, LinkCTScan):
        try:
            self.dalCTScan.updateCTScan(IDPatient=IDPatient, CTScanType=CTScanType, LinkCTScan=LinkCTScan)
            return 1
        except:
            return 0

    def searchPatient(self, State, IDPatient="", FullName=""):
        if(State == 0):
            return self.dalCTScan.searchPatientWithIDPatient(IDPatient=IDPatient)
        elif(State == 1):
            return self.dalCTScan.searchPatientWithFullName(FullName=FullName)
        else:
            return None