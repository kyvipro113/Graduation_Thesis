from SQL.SQLConnection import SQLConnection

class DAL_MRIPatient(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectLinkMRIViaIDPatient(self, IDPatient):
        data = self.queryDataOnly1("Select MRIType, LinkMRI From MRI Where IDPatient = '{}'".format(IDPatient))
        return data

    def selectLinkMRI(self, IDPatient, MRIType):
        data = self.queryDataOnly1("Select LinkMRI From MRI where IDPatient = '{}' and MRIType = N'{}'".format(IDPatient, MRIType))
        return data