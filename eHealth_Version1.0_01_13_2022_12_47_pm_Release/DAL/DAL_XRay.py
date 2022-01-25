from SQL.SQLConnection import SQLConnection

class DAL_XRay(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectAllXRay(self):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, XRay.XRayType, XRay.LinkXRay From Patient, XRay Where XRay.IDPatient = Patient.IDPatient And XRay.XRayType is not NULL")
        return data
    
    def selectXRayWithType(self, XRayType):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, XRay.XRayType, XRay.LinkXRay From Patient, XRay Where XRay.IDPatient = Patient.IDPatient And XRay.XRayType = N'{}'".format(XRayType))
        return data

    def selectLinkXRay(self, IDPatient):
        data = self.queryDataOnly1("Select LinkXRay From XRay Where IDPatient = '{}'".format(IDPatient))
        return data

    def updateXRay(self, IDPatient, XRayType, LinkXRay):
        self.queryNoReturn("Update XRay Set LinkXRay = '{}' Where IDPatient = '{}' and XRayType = N'{}'".format(LinkXRay, IDPatient, XRayType))

    def searchPatientWithIDPatient(self, IDPatient):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, XRay.XRayType, XRay.LinkXRay From Patient, XRay Where XRay.IDPatient = Patient.IDPatient And XRay.IDPatient = '{}'".format(IDPatient))
        return data

    def searchPatientWithFullName(self, FullName):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, XRay.XRayType, XRay.LinkXRay From Patient, XRay Where XRay.IDPatient = Patient.IDPatient And Patient.FullName Like N'%{}%' And Xray.XrayType is not NULL".format(FullName))
        return data 