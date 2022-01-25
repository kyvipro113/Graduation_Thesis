from SQL.SQLConnection import SQLConnection

class DAL_CTScanPatient(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectLinkCTScanViaIDPatient(self, IDPatient):
        data = self.queryDataOnly1("Select CTScanType, LinkCTScan From CTScan Where IDPatient = '{}'".format(IDPatient))
        return data

    def selectLinkCTScan(self, IDPatient, CTScanType):
        data = self.queryDataOnly1("Select LinkCTScan From CTScan where IDPatient = '{}' and CTScanType = N'{}'".format(IDPatient, CTScanType))
        return data