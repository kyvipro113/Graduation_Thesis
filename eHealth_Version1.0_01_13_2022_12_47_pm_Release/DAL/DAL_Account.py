from SQL.SQLConnection import SQLConnection

class DAL_Account(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def updatePassword(self, IDEmployee, password):
        self.queryNoReturn("Update Account Set Password = '{}' Where IDEmployee = '{}'".format(password, IDEmployee))

    def selectOldPassword(self, IDEmployee):
        data = self.queryDataOnly1("Select Password From Account Where IDEmployee = '{}'".format(IDEmployee))
        return data