from SQL.SQLConnection import SQLConnection

class DAL_Position(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectAllPosition(self):
        data = self.queryData("Select * From Position")
        return data

    def addPosition(self, IDPosition, PositionName):
        self.queryNoReturn("Insert Into Position Values ('{}', N'{}')".format(IDPosition, PositionName))

    def updatePosition(self, IDPosition, PositionName):
        self.queryNoReturn("Update Position Set PositionName = N'{}' Where IDPosition = '{}'".format(PositionName, IDPosition))

    def deletePosition(self, IDPosition):
        self.queryNoReturn("Delete From Position Where IDPosition = '{}'".format(IDPosition))
