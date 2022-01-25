from DAL.DAL_Account import DAL_Account
import hashlib

class BUS_Account():
    def __init__(self):
        self.dalAccount = DAL_Account()

    def updatePassword(self, IDEmployee, passwordOld, passwordNew):
        passwordOld = passwordOld.encode()
        passwordOld = hashlib.md5(passwordOld)
        passwordOld = passwordOld.hexdigest()
        dataPass = self.dalAccount.selectOldPassword(IDEmployee=IDEmployee)
        if(dataPass is not None and dataPass != ""):
            if(passwordOld == dataPass[0]):
                passwordNew = passwordNew.encode()
                passwordNew = hashlib.md5(passwordNew)
                passwordNew = passwordNew.hexdigest()
                try:
                    self.dalAccount.updatePassword(IDEmployee=IDEmployee, password=passwordNew)
                    return 1
                except:
                    return 0
            else:
                return 2
        else:
            return 0