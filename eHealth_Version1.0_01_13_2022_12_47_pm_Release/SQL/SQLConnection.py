import pyodbc

class SQLConnection(object):
    def __init__(self, *args):
        if len(args) == 0:
            cfg_data = []
            with open("Config/sqlconnect.cfg", "r+") as file:
                for data in file:
                    cfg_data.append(data.strip())
            self.server = cfg_data[0]
            self.database = cfg_data[1]
            self.username = cfg_data[2]
            self.password = cfg_data[3]
            self.cnn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
            self.con = self.cnn.cursor()
        elif(isinstance(args[0], str) and isinstance(args[1], str)):
            self.cnn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=' + args[0] + ';DATABASE=' + args[1] + ';Trusted_Connection=yes')
            self.con = self.cnn.cursor()


    # def __init__(self, server, database):
    #     self.cnn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
    #     self.con = self.cnn.cursor()

    def setNameServer(self, server):
        self.server = server

    def setUser(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def setDataBase(self, database):
        self.database = database

    def queryDataOnly1(self, query):
        self.con.execute(query)
        self.data = self.con.fetchone()
        return self.data

    def queryData(self, query):
        self.con.execute(query)
        self.data = self.con.fetchall()
        return self.data

    def queryNoReturn(self, query):
        with self.con:
            self.con.execute(query)
