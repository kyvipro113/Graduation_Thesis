from DAL.DAL_TestPatient import DAL_TestPatient

class BUS_TestPatient():
    def __init__(self):
        self.dalTestPatient = DAL_TestPatient()

    def firstLoadLinkTest(self, IDPatient):
        return self.dalTestPatient.selectLinkTestViaIDPatient(IDPatient=IDPatient)

    def loadLinkTest(self, IDPatient, TestType):
        return self.dalTestPatient.selectLinkTest(IDPatient=IDPatient, TestType=TestType)