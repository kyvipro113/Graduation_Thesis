from DAL.DAL_MRIPatient import DAL_MRIPatient

class BUS_MRIPatient():
    def __init__(self):
        self.dalMRIPatient = DAL_MRIPatient()

    def firstLoadLinkMRI(self, IDPatient):
        return self.dalMRIPatient.selectLinkMRIViaIDPatient(IDPatient=IDPatient)

    def loadLinkMRI(self, IDPatient, MRIType):
        return self.dalMRIPatient.selectLinkMRI(IDPatient=IDPatient, MRIType=MRIType)