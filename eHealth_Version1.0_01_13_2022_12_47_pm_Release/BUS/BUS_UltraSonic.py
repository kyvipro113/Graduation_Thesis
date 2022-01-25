from DAL.DAL_UltraSonic import DAL_UltraSonic

class BUS_UltraSonic():
    def __init__(self):
        self.dalUltraSonic = DAL_UltraSonic()

    def loadAllData(self):
        return self.dalUltraSonic.selectAllUltraSonic()

    def loadDataWithType(self, UltraSonicType):
        return self.dalUltraSonic.selectUltraSonicWithType(UltraSonicType=UltraSonicType)

    def getLinkUltraSonic(self, IDPatient):
        return self.dalUltraSonic.selectLinkNRI(IDPatient=IDPatient)

    def uploadUltraSonic(self, IDPatient, UltraSonicType, LinkUltraSonic):
        try:
            self.dalUltraSonic.updateUltraSonic(IDPatient=IDPatient, UltraSonicType=UltraSonicType, LinkUltraSonic=LinkUltraSonic)
            return 1
        except:
            return 0

    def searchPatient(self, State, IDPatient="", FullName=""):
        if(State == 0):
            return self.dalUltraSonic.searchPatientWithIDPatient(IDPatient=IDPatient)
        elif(State == 1):
            return self.dalUltraSonic.searchPatientWithFullName(FullName=FullName)
        else:
            return None