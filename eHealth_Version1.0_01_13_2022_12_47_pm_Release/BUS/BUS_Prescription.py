from DAL.DAL_Prescription import DAL_Prescription

class BUS_Prescription():
    def __init__(self):
        self.dalPrescription = DAL_Prescription()

    def loadPrescription(self, IDPatient):
        return self.dalPrescription.selectAllPrescription(IDPatient=IDPatient)

    def addPrescription(self, dtoPrescription):
        try:
            self.dalPrescription.addPrescription(dtoPrescription=dtoPrescription)
            return 1
        except:
            return 0

    def updatePrescription(self, dtoPrescription):
        try:
            self.dalPrescription.updatePrescription(dtoPrescription=dtoPrescription)
            return 1
        except:
            return 0

    def deletePrescription(self, IDPrescription):
        try:
            self.dalPrescription.deletePrescription(IDPrescription=IDPrescription)
            return 1
        except:
            return 0