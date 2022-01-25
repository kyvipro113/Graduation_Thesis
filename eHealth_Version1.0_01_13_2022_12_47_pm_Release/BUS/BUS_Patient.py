from  DAL.DAL_Patient import DAL_Patient

class BUS_Patient():
    def __init__(self):
        self.dalPatient = DAL_Patient()

    def loadAllPatient(self):
        return self.dalPatient.selectAllPatient()

    def loadPatientOfEmployee(self, IDEmployee):
        return self.dalPatient.selectPatientOfEmployee(IDEmployee=IDEmployee)

    def updateDiagnose(self, dtoPatient):
        try:
            self.dalPatient.updateDiagnose(dtoPatient=dtoPatient)
            return 1
        except:
            return 0