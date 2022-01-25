import hashlib
from DAL.DAL_Login import DAL_Login

class BUS_Login():
    def __init__(self):
        self.dalLogin = DAL_Login()

    def loginSys(self, username, password):
        password = password.encode()
        password = hashlib.md5(password)
        return self.dalLogin.loginSys(username=username, password=password.hexdigest())