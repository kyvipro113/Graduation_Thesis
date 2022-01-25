from SQL.SQLConnection import SQLConnection

class DAL_CreateAccount(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectEmployeeHaveNotAccount(self):
        data = self.queryData("Select Employee.IDEmployee, Employee.FullName From Employee, Account Where Employee.IDEmployee = Account.IDEmployee And Account.Username is NULL")
        return data
    
    def selectEmployeeHaveAccount(self):
        data = self.queryData("Select IDEmployee, Username, IDPermission From Account Where Username is not NULL")
        return data
    
    def selectIDEmployee(self, FullName):
        data = self.queryDataOnly1("Select Account.IDEmployee From Account, Employee Where Account.IDEmployee = Employee.IDEmployee And Employee.FullName = N'{}'".format(FullName))
        return data

    def selectFullName(self, IDEmployee):
        data = self.queryDataOnly1("Select FullName From Employee Where IDEmployee = '{}'".format(IDEmployee))
        return data

    def selectPermissName(self, IDPermission):
        data = self.queryDataOnly1("Select PermissionName From Permission Where IDPermission = {}".format(IDPermission))
        return data

    def updateAccount(self, IDEmployee, username, password, IDPermission):
        self.queryNoReturn("Update Account Set Username = '{}', Password = '{}', IDPermission = {} Where IDEmployee = '{}'".format(username, password, IDPermission, IDEmployee))

    def deleteAccount(self, IDEmployee):
        self.queryNoReturn("Update Account Set Username = NULL, Password = NULL Where IDEmployee = '{}'".format(IDEmployee))

    
