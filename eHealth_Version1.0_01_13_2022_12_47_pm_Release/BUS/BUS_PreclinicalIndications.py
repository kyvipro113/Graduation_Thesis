from DAL.DAL_PreclinicalIndications import DAL_PreclinicalIndications

class BUS_PreclinicalIndications():
    def __init__(self):
        self.dalPreclinicalIndications = DAL_PreclinicalIndications()

    # XRAYS
    def loadPreclinicalXray(self, IDPatient):
        return self.dalPreclinicalIndications.selectPreclinicalXray(IDPatient=IDPatient)

    # def addPreclinicalXray(self, IDPatient, XrayType):
    #     try:
    #         self.dalPreclinicalIndications.addPreclinicalXray(IDPatient=IDPatient, XrayType=XrayType)
    #         return 1
    #     except:
    #         return 0

    def updatePreclinicalXray(self, IDPatient, XrayType, LinkXray):
        try:
            self.dalPreclinicalIndications.updatePreclinicalXray(IDPatient=IDPatient, XrayType=XrayType, LinkXray=LinkXray)
            return 1
        except:
            return 0
    
    def deletePreclinicalXray(self, IDPatient):
        try:
            self.dalPreclinicalIndications.deletePreclinicalXray(IDPatient=IDPatient)
            return 1
        except:
            return 0

    #MRI
    def loadPreclinicalMRI(self, IDPatient):
        return self.dalPreclinicalIndications.selectPreclinicalMRI(IDPatient=IDPatient)

    # def addPreclinicalMRI(self, IDPatient, MRIType):
    #     try:
    #         self.dalPreclinicalIndications.addPreclinicalMRI(IDPatient=IDPatient, MRIType=MRIType)
    #         return 1
    #     except:
    #         return 0

    def updatePreclinicalMRI(self, IDPatient, MRIType, LinkMRI):
        try:
            self.dalPreclinicalIndications.updatePreclinicalMRI(IDPatient=IDPatient, MRIType=MRIType, LinkMRI=LinkMRI)
            return 1
        except:
            return 0

    def deletePreclinicalMRI(self, IDPatient):
        try:
            self.dalPreclinicalIndications.deletePreclinicalMRI(IDPatient=IDPatient)
            return 1
        except:
            return 0

     # CTScan
    def loadPreclinicalCTScan(self, IDPatient):
        return self.dalPreclinicalIndications.selectPreclinicalCTScan(IDPatient=IDPatient)

    # def addPreclinicalCTScan(self, IDPatient, CTScanType):
    #     try:
    #         self.dalPreclinicalIndications.addPreclinicalCTScan(IDPatient=IDPatient, CTScanType=CTScanType)
    #         return 1
    #     except:
    #         return 0

    def updatePreclinicalCTScan(self, IDPatient, CTScanType, LinkCTScan):
        try:
            self.dalPreclinicalIndications.updatePreclinicalCTScan(IDPatient=IDPatient, CTScanType=CTScanType, LinkCTScan=LinkCTScan)
            return 1
        except:
            return 0

    def deletePreclinicalCTScan(self, IDPatient):
        try:
            self.dalPreclinicalIndications.deletePreclinicalCTScan(IDPatient=IDPatient)
            return 1
        except:
            return 0

    # UltraSonic
    def loadPreclinicalUltrasonic(self, IDPatient):
        return self.dalPreclinicalIndications.selectPreclinicalUltrasonic(IDPatient=IDPatient)

    # def addPreclinicalUltrasonic(self, IDPatient, UltrasonicType):
    #     try:
    #         self.dalPreclinicalIndications.addPreclinicalUltrasonic(IDPatient=IDPatient, UltrasonicType=UltrasonicType)
    #         return 1
    #     except:
    #         return 0

    def updatePreclinicalUltrasonic(self, IDPatient, UltrasonicType, LinkUltrasonic):
        try:
            self.dalPreclinicalIndications.updatePreclinicalUltrasonic(IDPatient=IDPatient, UltrasonicType=UltrasonicType, LinkUltrasonic=LinkUltrasonic)
            return 1
        except:
            return 0

    def deletePreclinicalUltrasonic(self, IDPatient):
        try:
            self.dalPreclinicalIndications.deletePreclinicalUltrasonic(IDPatient=IDPatient)
            return 1
        except:
            return 0

    # ECG
    def loadPreclinicalECG(self, IDPatient):
        return self.dalPreclinicalIndications.selectPreclinicalECG(IDPatient=IDPatient)

    # def addPreclinicalECG(self, IDPatient, ECGType):
    #     try:
    #         self.dalPreclinicalIndications.addPreclinicalECG(IDPatient=IDPatient, ECGType=ECGType)
    #         return 1
    #     except:
    #         return 0

    def updatePreclinicalECG(self, IDPatient, ECGType, LinkECG):
        try:
            self.dalPreclinicalIndications.updatePreclinicalECG(IDPatient=IDPatient, ECGType=ECGType, LinkECG=LinkECG)
            return 1
        except:
            return 0

    def deletePreclinicalECG(self, IDPatient):
        try:
            self.dalPreclinicalIndications.deletePreclinicalECG(IDPatient=IDPatient)
            return 1
        except:
            return 0

    # Test
    def loadPreclinicalTest(self, IDPatient):
        return self.dalPreclinicalIndications.selectPreclinicalTest(IDPatient=IDPatient)

    # def addPreclinicalTest(self, IDPatient, TestType):
    #     try:
    #         self.dalPreclinicalIndications.addPreclinicalTest(IDPatient=IDPatient, TestType=TestType)
    #         return 1
    #     except:
    #         return 0

    def updatePreclinicalTest(self, IDPatient, TestType, LinkTest):
        try:
            self.dalPreclinicalIndications.updatePreclinicalTest(IDPatient=IDPatient, TestType=TestType, LinkTest=LinkTest)
            return 1
        except:
            return 0

    def deletePreclinicalTest(self, IDPatient):
        try:            
            self.dalPreclinicalIndications.deletePreclinicalTest(IDPatient=IDPatient)
            return 1
        except:
            return 0
