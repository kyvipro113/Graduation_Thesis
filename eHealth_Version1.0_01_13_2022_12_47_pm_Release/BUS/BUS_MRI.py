from DAL.DAL_MRI import DAL_MRI

class BUS_MRI():
    def __init__(self):
        self.dalMRI = DAL_MRI()

    def loadAllData(self):
        return self.dalMRI.selectAllMRI()

    def loadDataWithType(self, MRIType):
        return self.dalMRI.selectMRIWithType(MRIType=MRIType)

    def getLinkMRI(self, IDPatient):
        return self.dalMRI.selectLinkNRI(IDPatient=IDPatient)

    def uploadMRI(self, IDPatient, MRIType, LinkMRI):
        try:
            self.dalMRI.updateMRI(IDPatient=IDPatient, MRIType=MRIType, LinkMRI=LinkMRI)
            return 1
        except:
            return 0

    def searchPatient(self, State, IDPatient="", FullName=""):
        if(State == 0):
            return self.dalMRI.searchPatientWithIDPatient(IDPatient=IDPatient)
        elif(State == 1):
            return self.dalMRI.searchPatientWithFullName(FullName=FullName)
        else:
            return None