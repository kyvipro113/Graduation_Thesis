from DAL.DAL_XRayPatient import DAL_XRayPatient

class BUS_XRayPatient():
    def __init__(self):
        self.dalXRayPatient = DAL_XRayPatient()

    def firstLoadLinkXRay(self, IDPatient):
        return self.dalXRayPatient.selectLinkXRayViaIDPatient(IDPatient=IDPatient)

    def loadLinkXRay(self, IDPatient, XRayType):
        return self.dalXRayPatient.selectLinkXRay(IDPatient=IDPatient, XRayType=XRayType)