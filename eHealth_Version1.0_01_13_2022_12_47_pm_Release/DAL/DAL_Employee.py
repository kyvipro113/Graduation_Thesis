from SQL.SQLConnection import SQLConnection

class DAL_Employee(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectAllEmployee(self):
        data = self.queryData("Select * From Employee")
        return data

    def addEmployee(self, dtoEmployee):
        self.queryNoReturn("Insert Into Employee Values('{}', N'{}', '{}', N'{}', '{}', '{}', N'{}', N'{}', '{}', '{}', '{}')".format(dtoEmployee.IDEmployee, dtoEmployee.FullName, dtoEmployee.DateOfBirth, dtoEmployee.Gender, dtoEmployee.CitizenID, dtoEmployee.NumberPhone, dtoEmployee.Address, dtoEmployee.Degree, dtoEmployee.IDFaculty, dtoEmployee.IDPosition, dtoEmployee.Image))
        self.queryNoReturn("Insert Into Account Values('{}', NULL, NULL, NULL)".format(dtoEmployee.IDEmployee))

    def updateEmployee(self, dtoEmployee):
        self.queryNoReturn("Update Employee Set FullName = N'{}', DateOfBirth = '{}', Gender = N'{}', CitizenID = '{}', NumberPhone = '{}', Address = N'{}', Degree = N'{}', IDFaculty = '{}', IDPosition = '{}', Image = '{}' Where IDEmployee = '{}'".format(dtoEmployee.FullName, dtoEmployee.DateOfBirth, dtoEmployee.Gender, dtoEmployee.CitizenID, dtoEmployee.NumberPhone, dtoEmployee.Address, dtoEmployee.Degree, dtoEmployee.IDFaculty, dtoEmployee.IDPosition, dtoEmployee.Image, dtoEmployee.IDEmployee))

    def deleteEmployee(self, IDEmployee):
        self.queryNoReturn("Delete From Account Where IDEmployee = '{}'".format(IDEmployee))
        self.queryNoReturn("Delete From Employee Where IDEmployee = '{}'".format(IDEmployee))
        self.queryNoReturn("Delete From ListID Where IDEmployee = '{}'".format(IDEmployee))

    def getFaculty(self, IDFaculty):
        data = self.queryDataOnly1("Select FacultyName From Faculty Where IDFaculty = '{}'".format(IDFaculty))
        return data[0]

    def getPosition(self, IDPosition):
        data = self.queryDataOnly1("Select PositionName From Position Where IDPosition = '{}'".format(IDPosition))
        return data[0]

    def getAllFaculty(self):
        data = self.queryData("Select FacultyName From Faculty")
        return data
    
    def getAllPosition(self):
        data = self.queryData("Select PositionName From Position")
        return data

    def getIDFaculty(self, FacultyName):
        data = self.queryDataOnly1("Select IDFaculty From Faculty Where FacultyName = N'{}'".format(FacultyName))
        return data[0]

    def getIDPosition(self, PositionName):
        data = self.queryDataOnly1("Select IDPosition From Position Where PositionName = N'{}'".format(PositionName))
        return data[0]
    
    def getImageEmployee(self, IDEmployee):
        data = self.queryDataOnly1("Select Image From Employee Where IDEmployee = '{}'".format(IDEmployee))
        return data[0]