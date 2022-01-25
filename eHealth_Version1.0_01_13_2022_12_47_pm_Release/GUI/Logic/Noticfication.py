from PyQt5 import QtWidgets, QtCore, QtGui

class Notification(object):
    def __init__(self, title, message, icon_type=0):
        icon = 0
        if icon_type == 0:
            icon = QtWidgets.QMessageBox.Information
        elif icon_type == 1:
            icon = QtWidgets.QMessageBox.Warning
        elif icon_type == 2:
            icon = QtWidgets.QMessageBox.Critical
        msg = QtWidgets.QMessageBox()
        msg.setIcon(icon)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        msg.exec_()
