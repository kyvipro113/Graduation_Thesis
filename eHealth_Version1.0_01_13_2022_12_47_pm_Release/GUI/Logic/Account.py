from PyQt5.QtWidgets import QFrame
from GUI.View.Ui_Account import Ui_Account
from GUI.Logic.Noticfication import Notification
from BUS.BUS_Account import BUS_Account

class Account(QFrame, Ui_Account):
    def __init__(self, IDEmployee, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.IDEmployee = IDEmployee
        self.busAccount = BUS_Account()

        # Event Handle
        self.btChangePassword.clicked.connect(self.changePassword)

    def checkEmpty(self):
        if(self.txtPasswordOld.text() == ""):
            return False
        if(self.txtPasswordNew.text() == ""):
            return False
        if(self.txtPasswordNewVerify.text() == ""):
            return False
        return True

    def changePassword(self):
        if(self.checkEmpty()):
            if(self.txtPasswordNew.text() == self.txtPasswordNewVerify.text()):
                result = self.busAccount.updatePassword(IDEmployee=self.IDEmployee, passwordOld=self.txtPasswordOld.text(), passwordNew=self.txtPasswordNew.text())
                if(result == 1):
                    self.noticfication = Notification(title="Thông báo", message="Thay Đổi Mật Khẩu Thành Công!")
                elif(result == 0):
                    self.noticfication = Notification(title="Cảnh báo", message="Thao Tác Thực Hiện Thất Bại!", icon_type=1)
                else:
                    self.noticfication = Notification(title="Cảnh báo", message="Mật Khẩu Cũ Không Đúng!", icon_type=1)    
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Xác Nhận Mật Khẩu Mới Khồng Trùng Khớp!", icon_type=1)
            self.txtPasswordOld.clear()
            self.txtPasswordNew.clear()
            self.txtPasswordNewVerify.clear()
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Không Được Để Trống Các Trường!", icon_type=1)