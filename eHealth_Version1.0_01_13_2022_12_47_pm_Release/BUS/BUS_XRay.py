from DAL.DAL_XRay import DAL_XRay

class BUS_XRay():
    def __init__(self):
        self.dalXRay = DAL_XRay()

    def loadAllData(self):
        return self.dalXRay.selectAllXRay()

    def loadDataWithType(self, XRayType):
        return self.dalXRay.selectXRayWithType(XRayType=XRayType)

    def getLinkXRay(self, IDPatient):
        return self.dalXRay.selectLinkXRay(IDPatient=IDPatient)

    def uploadXRay(self, IDPatient, XRayType, LinkXRay):
        try:
            self.dalXRay.updateXRay(IDPatient=IDPatient, XRayType=XRayType, LinkXRay=LinkXRay)
            return 1
        except:
            return 0

    def searchPatient(self, State, IDPatient="", FullName=""):
        if(State == 0):
            return self.dalXRay.searchPatientWithIDPatient(IDPatient=IDPatient)
        if(State == 1):
            return self.dalXRay.searchPatientWithFullName(FullName=FullName)
        else:
            return None