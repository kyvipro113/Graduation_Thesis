from DAL.DAL_Search import DAL_Search

class BUS_Search():
    def __init__(self):
        self.dalSearch = DAL_Search()

    def searchEmployee(self, State, IDEmployee="", FullName=""):
        if(State == 1):
            return self.dalSearch.selectEmployeeViaID(IDEmployee=IDEmployee)
        elif(State == 0):
            return self.dalSearch.selectEmployeeViaFullName(FullName=FullName)
        else:
            return None

    def searchPatient(self, State, IDPatient="", FullName=""):
        if(State == 1):
            return self.dalSearch.selectPatientViaID(IDPatient=IDPatient)
        elif(State == 0):
            return self.dalSearch.selectPatientViaFullName(FullName=FullName)
        else:
            return None