from SQL.SQLConnection import SQLConnection

class DAL_CTScan(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectAllCTScan(self):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, CTScan.CTScanType, CTScan.LinkCTScan From Patient, CTScan Where CTScan.IDPatient = Patient.IDPatient And CTScan.CTScanType is not NULL")
        return data

    def selectCTScanWithType(self, CTScanType):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, CTScan.CTScanType, CTScan.LinkCTScan From Patient, CTScan Where CTScan.IDPatient = Patient.IDPatient And CTScan.CTScanType = N'{}'".format(CTScanType))
        return data

    def selectLinkNRI(self, IDPatient):
        data = self.queryDataOnly1("Select LinkCTScan From CTScan Where IDPatient = '{}'".format(IDPatient))
        return data

    def updateCTScan(self, IDPatient, CTScanType, LinkCTScan):
        self.queryNoReturn("Update CTScan Set LinkCTScan = '{}' Where IDPatient = '{}' and CTScanType = N'{}'".format(LinkCTScan, IDPatient, CTScanType))

    def searchPatientWithIDPatient(self, IDPatient):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, CTScan.CTScanType, CTScan.LinkCTScan From Patient, CTScan Where CTScan.IDPatient = Patient.IDPatient And CTScan.IDPatient = '{}'".format(IDPatient))
        return data

    def searchPatientWithFullName(self, FullName):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, CTScan.CTScanType, CTScan.LinkCTScan From Patient, CTScan Where CTScan.IDPatient = Patient.IDPatient And Patient.FullName Like N'%{}%' And CTScan.CTScanType is not NULL".format(FullName))
        return data 