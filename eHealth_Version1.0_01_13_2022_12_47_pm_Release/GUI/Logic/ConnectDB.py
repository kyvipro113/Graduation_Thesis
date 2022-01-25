from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QMainWindow
from GUI.View.Ui_ConnectDB import Ui_ConnectDB
from GUI.Logic.Noticfication import *
from PyQt5 import QtWidgets
import platform
from SQL.SQLConnection import SQLConnection

class Connect_DB(QMainWindow, Ui_ConnectDB):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

        # Get Server Name and Database Name in localhost
        sql = SQLConnection(platform.node(), "master")
        #sql.setNameServer(server=platform.node())
        #sql.setDataBase(database="master")

        dbNames = sql.queryData("Select name From sys.databases")
        for dbName in dbNames:
            self.comboDBName.addItem(dbName[0])
        
        try:
            dataFile = []
            with open("Config/sqlconnect.cfg", "r+") as file:
                for data in file:
                    dataFile.append(data.strip())
            self.txtServerName.setText(dataFile[0])
            self.comboDBName.setCurrentText(dataFile[1])
            self.txtUsername.setText(dataFile[2])
            self.txtPassword.setText(dataFile[3])
        except:
            pass

        self.txtServerName.setText(platform.node())

        # Event Handle
        self.btConnect.clicked.connect(self.connectDataBase)
        self.btExit.clicked.connect(self.exit)
        self.checkTypeConn.stateChanged.connect(self.stateCheck)

        #self.txtServerName.installEventFilter(self)
        #self.txtServerName.textEdited.connect(self.printTest)
    
    def connectDataBase(self):
        try:
            db_connect_config = [self.txtServerName.text(), self.comboDBName.currentText(), self.txtUsername.text(), self.txtPassword.text()]
            with open("Config/sqlconnect.cfg", "w+") as file:
                for data in db_connect_config:
                    file.write(data + "\n")
            self.noticfication = Notification(title="Thông báo", message="Thay đổi CSDL thành công!")
        except:
            self.noticfication = Notification(title="Cảnh báo", message="Thay đổi CSDL thất bại!", icon_type=1)

    def exit(self):
        self.close()

    # def eventFilter(self, source, event):
    #     if(event.type() == QEvent.KeyPress and source is self.txtServerName):
    #         print("Yes")
    #     return super(Connect_DB, self).eventFilter(source, event)

    def stateCheck(self):
        if self.checkTypeConn.isChecked():
            sql = SQLConnection()
            sql.setNameServer(server=self.txtServerName.text())
            sql.setDataBase(database="master")
            dbNames = sql.queryData("Select name From sys.databases")

            self.comboDBName.clear()
            self.txtUsername.setText("")
            self.txtPassword.setText("")
            for dbName in dbNames:
                self.comboDBName.addItem(dbName[0])
        else:
            pass