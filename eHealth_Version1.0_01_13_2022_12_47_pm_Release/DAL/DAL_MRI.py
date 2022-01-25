from SQL.SQLConnection import SQLConnection

class DAL_MRI(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectAllMRI(self):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, MRI.MRIType, MRI.LinkMRI From Patient, MRI Where MRI.IDPatient = Patient.IDPatient And MRI.MRIType is not NULL")
        return data

    def selectMRIWithType(self, MRIType):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, MRI.MRIType, MRI.LinkMRI From Patient, MRI Where MRI.IDPatient = Patient.IDPatient And MRI.MRIType = N'{}'".format(MRIType))
        return data

    def selectLinkNRI(self, IDPatient):
        data = self.queryDataOnly1("Select LinkMRI From MRI Where IDPatient = '{}'".format(IDPatient))
        return data

    def updateMRI(self, IDPatient, MRIType, LinkMRI):
        self.queryNoReturn("Update MRI Set LinkMRI = '{}' Where IDPatient = '{}' and MRIType = N'{}'".format(LinkMRI, IDPatient, MRIType))

    def searchPatientWithIDPatient(self, IDPatient):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, MRI.MRIType, MRI.LinkMRI From Patient, MRI Where MRI.IDPatient = Patient.IDPatient And MRI.IDPatient = '{}'".format(IDPatient))
        return data

    def searchPatientWithFullName(self, FullName):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, MRI.MRIType, MRI.LinkMRI From Patient, MRI Where MRI.IDPatient = Patient.IDPatient And Patient.FullName Like N'%{}%' And MRI.MRIType is not NULL".format(FullName))
        return data 