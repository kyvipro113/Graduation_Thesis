from DAL.DAL_Position import DAL_Position

class BUS_Position():
    def __init__(self):
        self.dalPosition = DAL_Position()

    def loadData(self):
        return self.dalPosition.selectAllPosition()
    
    def addNewPosition(self, IDPosition, PositionName):
        try:
            self.dalPosition.addPosition(IDPosition=IDPosition, PositionName=PositionName)
            return 1
        except:
            return 0

    def fixPosition(self, IDPosition, PositionName):
        try:
            self.dalPosition.updatePosition(IDPosition=IDPosition, PositionName=PositionName)
            return 1
        except:
            return 0

    def delPosition(self, IDPosition):
        try:
            self.dalPosition.deletePosition(IDPosition=IDPosition)
            return 1
        except:
            return 0