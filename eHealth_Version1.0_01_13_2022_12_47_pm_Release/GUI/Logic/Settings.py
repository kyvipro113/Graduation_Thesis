from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from GUI.View.Ui_Settings import Ui_Settings
from GUI.Logic.ConnectDB import Connect_DB
from GUI.Logic.Noticfication import Notification
import hashlib

class Settings(QMainWindow, Ui_Settings):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

        # Event Handle
        self.btOK.clicked.connect(self.openSettings)
        self.btExit.clicked.connect(self.exit)

    def openSettings(self):
        if(self.txtSystemPIN.text() != ""):
            truePIN = ""
            with open("Config/syspin.cfg", "r+") as file:
                for data in file:
                    truePIN = data
            PINInTxt = self.txtSystemPIN.text()
            PINInTxt = PINInTxt.encode()
            PINInTxt = hashlib.md5(PINInTxt)
            PINInTxt = PINInTxt.hexdigest()
            if(PINInTxt == truePIN):
                self.uiConnectDB = Connect_DB()
                self.uiConnectDB.show()
                self.hide()
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Mã PIN Nhập Vào Không Đúng!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Không Được Để Trống Mã PIN!", icon_type=1)

    def exit(self):
        self.hide()