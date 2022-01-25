from SQL.SQLConnection import SQLConnection

class DAL_XRayPatient(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectLinkXRayViaIDPatient(self, IDPatient):
        data = self.queryDataOnly1("Select XRayType, LinkXRay From XRay Where IDPatient = '{}'".format(IDPatient))
        return data

    def selectLinkXRay(self, IDPatient, XRayType):
        data = self.queryDataOnly1("Select LinkXRay From XRay where IDPatient = '{}' and XRayType = N'{}'".format(IDPatient, XRayType))
        return data