class DTO_Employee():
    def __init__(self):
        self.IDEmployee = ""
        self.FullName = ""
        self.DateOfBirth = "" #mm/dd/yyyy
        self.Gender = ""
        self.CitizenID = ""
        self.NumberPhone = ""
        self.Address = ""
        self.Degree = ""
        self.IDFaculty = ""
        self.IDPosition = ""
        self.Image = ""
    
    def TestPrint(self):
        print(self.IDEmployee)
        print(self.FullName)
        print(self.DateOfBirth)
        print(self.Gender)
        print(self.CitizenID)
        print(self.NumberPhone)
        print(self.Address)
        print(self.Degree)
        print(self.IDFaculty)
        print(self.IDPosition)
        print(self.Image)
