import hashlib
from DAL.DAL_CreateAccount import DAL_CreateAccount

class BUS_CreateAccount():
    def __init__(self):
        self.dalCreateAccount = DAL_CreateAccount()

    def loadData(self):
        dataEmplHaveNotAcc = self.dalCreateAccount.selectEmployeeHaveNotAccount()
        dataEmpHaveAcc = self.dalCreateAccount.selectEmployeeHaveAccount()
        return dataEmplHaveNotAcc, dataEmpHaveAcc

    def loadIDEmployee(self, FullName):
        return self.dalCreateAccount.selectIDEmployee(FullName=FullName)

    def loadFullName(self, IDEmployee):
        return self.dalCreateAccount.selectFullName(IDEmployee=IDEmployee)

    def loadPermissionName(self, IDPermission):
        return self.dalCreateAccount.selectPermissName(IDPermission=IDPermission)

    def updateAccount(self, IDEmployee, username, IDPermission,  password=""):
        if(password != ""):
            print(password)
            password = password.encode()
            password = hashlib.md5(password)
            password = password.hexdigest()
        try:
            self.dalCreateAccount.updateAccount(IDEmployee=IDEmployee, username=username, password=password, IDPermission=IDPermission)
            return 1
        except:
            return 0

    def deleteAccount(self, IDEmployee):
        print(IDEmployee)
        try:
            self.dalCreateAccount.deleteAccount(IDEmployee=IDEmployee)
            return 1
        except:
            return 0