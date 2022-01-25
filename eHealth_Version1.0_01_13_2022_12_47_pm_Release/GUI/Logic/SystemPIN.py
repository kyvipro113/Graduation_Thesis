import hashlib
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFrame
from GUI.View.Ui_SystemPIN import Ui_SystemPIN
from GUI.Logic.Noticfication import Notification

class SystemPIN(QFrame, Ui_SystemPIN):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        # Event Handle
        self.btChangePIN.clicked.connect(self.changeSysPIN)

    def checkEmpty(self):
        if(self.txtOldPIN.text() == ""):
            return False
        elif(self.txtNewPIN.text() == ""):
            return False
        elif(self.txtNewPINVerify.text() == ""):
            return False
        return True

    def changeSysPIN(self):
        if(self.checkEmpty()):
            oldPIN = ""
            with open("Config/syspin.cfg", "r+") as file:
                for data in file:
                    oldPIN = data

            PINInTxt = self.txtOldPIN.text()
            PINInTxt = PINInTxt.encode()
            PINInTxt = hashlib.md5(PINInTxt)
            PINInTxt = PINInTxt.hexdigest()

            if(self.txtNewPIN.text() == self.txtNewPINVerify.text()):
                if(oldPIN == PINInTxt):
                    newPIN = self.txtNewPIN.text()
                    newPIN = newPIN.encode()
                    newPIN = hashlib.md5(newPIN)
                    newPIN = newPIN.hexdigest()
                    with open("Config/syspin.cfg", "r+") as file:
                        file.write(newPIN)
                    self.noticfication = Notification(title="Thông báo", message="Thay Đổi Mã PIN Thành Công!")
                else:
                    self.noticfication = Notification(title="Cảnh báo", message="Mã PIN Cũ Không Đúng!", icon_type=1)
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Mã PIN Mới Không Trùng Khớp!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Không Được Để Trống Các Trường!", icon_type=1)

        
    