from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import *

from GUI.View.Ui_StatisticCovid import Ui_StatisticCovid

class StatisticCovid(QFrame, Ui_StatisticCovid):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.webEngine = QWebEngineView()
        self.mainLayout.addWidget(self.webEngine)
        self.webEngine.load(QUrl("https://corona.kompa.ai"))