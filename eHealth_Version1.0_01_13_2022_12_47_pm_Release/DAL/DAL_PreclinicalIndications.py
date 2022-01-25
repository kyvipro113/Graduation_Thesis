from SQL.SQLConnection import SQLConnection

class DAL_PreclinicalIndications(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    # XRAYS
    def selectPreclinicalXray(self, IDPatient):
        data = self.queryDataOnly1("Select XRayType From XRay Where IDPatient = '{}'".format(IDPatient))
        return data

    # def addPreclinicalXray(self, IDPatient, XrayType):
    #     self.queryNoReturn("Insert Into Xray Values('{}', N'{}',  NULL)",format(IDPatient, XrayType))

    def updatePreclinicalXray(self, IDPatient, XrayType, LinkXray):
        self.queryNoReturn("Update Xray Set XrayType = N'{}', LinkXray = '{}' Where IDPatient = '{}'".format(XrayType, LinkXray, IDPatient))

    def deletePreclinicalXray(self, IDPatient):
        self.queryNoReturn("Update Xray Set XRayType = NULL Where IDPatient = '{}'".format(IDPatient))

    #MRI
    def selectPreclinicalMRI(self, IDPatient):
        data = self.queryDataOnly1("Select MRIType From MRI Where IDPatient = '{}'".format(IDPatient))
        return data
    # def addPreclinicalMRI(self, IDPatient, MRIType):
    #     self.queryNoReturn("Insert Into MRI Values('{}', N'{}',  NULL)",format(IDPatient, MRIType))

    def updatePreclinicalMRI(self, IDPatient, MRIType, LinkMRI):
        self.queryNoReturn("Update MRI Set MRIType = N'{}', LinkMRI = '{}' Where IDPatient = '{}'".format(MRIType, LinkMRI, IDPatient))

    def deletePreclinicalMRI(self, IDPatient):
        self.queryNoReturn("Update MRI Set MRIType = NULL Where IDPatient = '{}'".format(IDPatient))

    # CTScan
    def selectPreclinicalCTScan(self, IDPatient):
        data = self.queryDataOnly1("Select CTScanType From CTScan Where IDPatient = '{}'".format(IDPatient))
        return data
    # def addPreclinicalCTScan(self, IDPatient, CTScanType):
    #     self.queryNoReturn("Insert Into CTScan Values('{}', N'{}',  NULL)",format(IDPatient, CTScanType))

    def updatePreclinicalCTScan(self, IDPatient, CTScanType, LinkCTScan):
        self.queryNoReturn("Update CTScan Set CTScanType = N'{}', LinkCTScan = '{}' Where IDPatient = '{}'".format(CTScanType, LinkCTScan, IDPatient))

    def deletePreclinicalCTScan(self, IDPatient):
        self.queryNoReturn("Update CTScan Set CTScanType = NULL Where IDPatient = '{}'".format(IDPatient))

    # UltraSonic
    def selectPreclinicalUltrasonic(self, IDPatient):
        data = self.queryDataOnly1("Select UltrasonicType From Ultrasonic Where IDPatient = '{}'".format(IDPatient))
        return data
    def addPreclinicalUltrasonic(self, IDPatient, UltrasonicType):
        self.queryNoReturn("Insert Into Ultrasonic Values('{}', N'{}',  NULL)",format(IDPatient, UltrasonicType))

    def updatePreclinicalUltrasonic(self, IDPatient, UltrasonicType, LinkUltrasonic):
        self.queryNoReturn("Update Ultrasonic Set UltrasonicType = N'{}', LinkUltrasonic = '{}' Where IDPatient = '{}'".format(UltrasonicType, LinkUltrasonic, IDPatient))

    def deletePreclinicalUltrasonic(self, IDPatient):
        self.queryNoReturn("Update Ultrasonic Set UltrasonicType = NULL Where IDPatient = '{}'".format(IDPatient))

    # ECG
    def selectPreclinicalECG(self, IDPatient):
        data = self.queryDataOnly1("Select ECGType From ECG Where IDPatient = '{}'".format(IDPatient))
        return data
    # def addPreclinicalECG(self, IDPatient, ECGType):
    #     self.queryNoReturn("Insert Into ECG Values('{}', N'{}',  NULL)",format(IDPatient, ECGType))

    def updatePreclinicalECG(self, IDPatient, ECGType, LinkECG):
        self.queryNoReturn("Update ECG Set ECGType = N'{}', LinkECG = '{}' Where IDPatient = '{}'".format(ECGType, LinkECG, IDPatient))

    def deletePreclinicalECG(self, IDPatient):
        self.queryNoReturn("Update ECG Set ECGType = NULL Where IDPatient = '{}'".format(IDPatient))


    # Test
    def selectPreclinicalTest(self, IDPatient):
        data = self.queryDataOnly1("Select TestType From Test Where IDPatient = '{}'".format(IDPatient))
        return data
    # def addPreclinicalTest(self, IDPatient, TestType):
    #     self.queryNoReturn("Insert Into Test Values('{}', N'{}',  NULL)",format(IDPatient, TestType))

    def updatePreclinicalTest(self, IDPatient, TestType, LinkTest):
        self.queryNoReturn("Update Test Set TestType = N'{}', LinkTest = '{}' Where IDPatient = '{}'".format(TestType, LinkTest, IDPatient))

    def deletePreclinicalTest(self, IDPatient):
        self.queryNoReturn("Update Test Set TestType = NULL Where IDPatient = '{}'".format(IDPatient))