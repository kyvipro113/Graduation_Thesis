from DAL.DAL_Employee import DAL_Employee

class BUS_Employee():
    def __init__(self):
        self.dalEmployee = DAL_Employee()

    def loadData(self):
        return self.dalEmployee.selectAllEmployee()

    def addNewEmployee(self, dtoEmployee):
        try:
            self.dalEmployee.addEmployee(dtoEmployee=dtoEmployee)
            return 1
        except:
            return 0

    def fixEmployee(self, dtoEmployee):
        try:
            self.dalEmployee.updateEmployee(dtoEmployee=dtoEmployee)
            return 1
        except:
            return 0

    def delEmployee(self, IDEmployee):
        try:
            self.dalEmployee.deleteEmployee(IDEmployee=IDEmployee)
            return 1
        except:
            return 0


    def loadFaculty(self, IDFaculty):
        return self.dalEmployee.getFaculty(IDFaculty=IDFaculty)

    def loadPosition(self, IDPosition):
        return self.dalEmployee.getPosition(IDPosition=IDPosition)

    def loadAllFaculty(self):
        return self.dalEmployee.getAllFaculty()

    def loadAllPosition(self):
        return self.dalEmployee.getAllPosition()

    def getIDFaculty(self, FacultyName):
        return self.dalEmployee.getIDFaculty(FacultyName=FacultyName)

    def getIDPosition(self, PositionName):
        return self.dalEmployee.getIDPosition(PositionName=PositionName)

    def getImageEmployee(self, IDEmployee):
        return self.dalEmployee.getImageEmployee(IDEmployee=IDEmployee)