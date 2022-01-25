from PyQt5 import QtWidgets
from GUI.Logic.Login import Login
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    styleSheetFile = "GUI/Design/Style/Darkeum/Darkeum.qss"
    with open(styleSheetFile, "r") as ssF:
        app.setStyleSheet(ssF.read())
    login = Login()
    login.show()
    sys.exit(app.exec_())
