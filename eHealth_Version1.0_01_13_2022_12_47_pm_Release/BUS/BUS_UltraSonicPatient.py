from DAL.DAL_UltraSonicPatient import DAL_UltraSonicPatient

class BUS_UltraSonicPatient():
    def __init__(self):
        self.dalUltraSonicPatient = DAL_UltraSonicPatient()

    def firstLoadLinkUltraSonic(self, IDPatient):
        return self.dalUltraSonicPatient.selectLinkUltraSonicViaIDPatient(IDPatient=IDPatient)

    def loadLinkUltraSonic(self, IDPatient, UltraSonicType):
        return self.dalUltraSonicPatient.selectLinkUltraSonic(IDPatient=IDPatient, UltraSonicType=UltraSonicType)