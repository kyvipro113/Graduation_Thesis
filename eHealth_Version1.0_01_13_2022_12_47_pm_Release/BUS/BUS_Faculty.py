from DAL.DAL_Faculty import DAL_Faculty

class BUS_Faculty():
    def __init__(self):
        self.dalFaculty = DAL_Faculty()

    def loadData(self):
        return self.dalFaculty.selectAllFaculty()

    def addNewFaculty(self, IDFaculty, FacultyName):
        try:
            self.dalFaculty.addFaculty(IDFaculty=IDFaculty, FacultyName=FacultyName)
            return 1
        except:
            return 0

    def fixFaculty(self, IDFaculty, FacultyName):
        try:
            self.dalFaculty.updateFaculty(IDFaculty=IDFaculty, FacultyName=FacultyName)
            return 1
        except:
            return 0

    def delFaculty(self, IDFaculty):
        try:
            self.dalFaculty.deleteFaculty(IDFaculty=IDFaculty)
            return 1
        except:
            return 0

    def cellClickFaculty(self, IDFaculty):
        return self.dalFaculty.selectOneFaculty(IDFaculty=IDFaculty)