from DAL.DAL_Test import DAL_Test

class BUS_Test():
    def __init__(self):
        self.dalTest = DAL_Test()

    def loadAllData(self):
        return self.dalTest.selectAllTest()

    def loadDataWithType(self, TestType):
        return self.dalTest.selectTestWithType(TestType=TestType)

    def getLinkTest(self, IDPatient):
        return self.dalTest.selectLinkTest(IDPatient=IDPatient)

    def uploadTest(self, IDPatient, TestType, LinkTest):
        try:
            self.dalTest.updateTest(IDPatient=IDPatient, TestType=TestType, LinkTest=LinkTest)
            return 1
        except:
            return 0

    def searchPatient(self, State, IDPatient="", FullName=""):
        if(State == 0):
            return self.dalTest.searchPatientWithIDPatient(IDPatient=IDPatient)
        if(State == 1):
            return self.dalTest.searchPatientWithFullName(FullName=FullName)
        else:
            return None