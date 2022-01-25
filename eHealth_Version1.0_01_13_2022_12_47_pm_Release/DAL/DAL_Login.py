from SQL.SQLConnection import SQLConnection

class DAL_Login(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def loginSys(self, username, password):
        data = []
        dataAcc = self.queryDataOnly1("Select IDEmployee, IDPermission From Account Where Username = '{}' And Password = '{}'".format(username, password))
        data.append(dataAcc[0])
        EmpName = self.queryDataOnly1("Select FullName From Employee Where IDEmployee = '{}'".format(dataAcc[0]))
        data.append(EmpName[0])
        data.append(dataAcc[1])
        return data
