from PyQt5.QtWidgets import QMainWindow
from GUI.View.Ui_Login import Ui_Login
from GUI.Logic.Noticfication import *
from GUI.Logic.Settings import Settings
from BUS.BUS_Login import BUS_Login

from GUI.Logic.MainWindow import MainWindow

class Login(QMainWindow, Ui_Login):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

        self.btLogin.clicked.connect(self.login)
        self.btExit.clicked.connect(self.exit)
        self.btSettings.clicked.connect(self.openSettings)

    def openSettings(self):
        self.uiSettings = Settings()
        self.uiSettings.show()

    def login(self):
        try:
            busLogin = BUS_Login()
            data = busLogin.loginSys(username=self.txtUsername.text(), password=self.txtPassword.text())
            if data is not None:
                self.mainWindow = MainWindow(IDEmployee=data[0],FullName=data[1], IDPermission=data[2])
                self.mainWindow.showMaximized()
                self.hide()
        except:
            self.noticfication = Notification(title="Cảnh báo", message="Đăng nhập thất bại!", icon_type=1)

    def exit(self):
        QtWidgets.qApp.exit()