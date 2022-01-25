from SQL.SQLConnection import SQLConnection

class DAL_Prescription(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectAllPrescription(self, IDPatient):
        data = self.queryData("Select IDPrescription, ContentPS, Time From Prescription Where IDPatient = '{}'".format(IDPatient))
        return data

    def addPrescription(self, dtoPrescription):
        self.queryNoReturn("Insert Into Prescription Values('{}', '{}', N'{}', '{}', '{}')".format(dtoPrescription.IDPrescription, dtoPrescription.IDPatient, dtoPrescription.ContentPS, dtoPrescription.IDEmployee, dtoPrescription.Time))

    def updatePrescription(self, dtoPrescription):
        self.queryNoReturn("Update Prescription Set ContentPS = N'{}', Time = '{}' Where IDPrescription = '{}'".format(dtoPrescription.ContentPS, dtoPrescription.Time, dtoPrescription.IDPrescription))

    def deletePrescription(self, IDPrescription):
        self.queryNoReturn("Delete From Prescription Where IDPrescription = '{}'".format(IDPrescription))