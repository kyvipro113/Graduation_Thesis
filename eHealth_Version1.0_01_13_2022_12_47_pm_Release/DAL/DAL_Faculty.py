from SQL.SQLConnection import SQLConnection

class DAL_Faculty(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectAllFaculty(self):
        data = self.queryData("Select * From Faculty")
        return data
        
    def addFaculty(self, IDFaculty, FacultyName):
        self.queryNoReturn("Insert Into Faculty Values ('{}', N'{}')".format(IDFaculty, FacultyName))

    def updateFaculty(self, IDFaculty, FacultyName):
        self.queryNoReturn("Update Faculty Set FacultyName = N'{}' Where IDFaculty = '{}'".format(FacultyName, IDFaculty))

    def deleteFaculty(self, IDFaculty):
        self.queryNoReturn("Delete From Faculty Where IDFaculty = '{}'".format(IDFaculty))

    def selectOneFaculty(self, IDFaculty):
        data = []
        dtFaculty = self.queryDataOnly1("Select * From Faculty Where IDFaculty = '{}'".format(IDFaculty))
        data.append(dtFaculty[0])
        data.append(dtFaculty[1])
        totalEmployee = self.queryDataOnly1("Select COUNT(*) From Employee Where IDFaculty = '{}'".format(IDFaculty))
        data.append(totalEmployee[0])
        return data
