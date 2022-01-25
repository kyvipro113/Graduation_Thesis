from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDate
from GUI.Logic.Noticfication import *
from GUI.View.Ui_Employee import Ui_Employee
from BUS.BUS_Employee import BUS_Employee
from DTO.DTO_Employee import DTO_Employee
import os
from pathlib import Path
import shutil
import cv2
import datetime

class Employee(QFrame, Ui_Employee):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        dtSet = QDate(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
        self.deDateOfBirth.setDate(dtSet)

        self.dtoEmployee = DTO_Employee()
        self.busEmployee = BUS_Employee()
        self.dtoEmployee.DateOfBirth = str(datetime.date.today().month) + "/" + str(datetime.date.today().day) + "/" + str(datetime.date.today().year)

        # Event Handle
        self.deDateOfBirth.dateChanged.connect(self.onChangeDate)
        self.btAdd.clicked.connect(self.addEmployee)
        self.btUpdate.clicked.connect(self.updateEmployee)
        self.btDel.clicked.connect(self.deleteEmployee)
        self.btRefresh.clicked.connect(self.clear)
        self.btChooseImage.clicked.connect(self.chooseImg)
        self.dataTabEmployee.cellClicked.connect(self.cellClickOnDataTabEmployee)

        self.loadData()
        self.getFaculty()
        self.getPosition()

    
    def chooseImg(self):
        #Show dialog
        #options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        dialog = QFileDialog()
        image, _ = dialog.getOpenFileName(None, "Chọn Ảnh Nhân Viên", "","Image Files (*.jpg *.jpeg *png *gif);;All Files (*)")
        if image != "":
            #print(image)
            img = cv2.imread(image)
            img = cv2.resize(img, (130, 160))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = img.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
            pixImg = convertToQtFormat.scaled(130, 160, Qt.KeepAspectRatio)
            self.lbImage.setPixmap(QtGui.QPixmap(pixImg))

            fileName = Path(image).resolve().stem   #Get file name
            fileTail =os.path.splitext(image)[1] #Get extension file tail
            self.dtoEmployee.Image = fileName + fileTail #Merge file name with extension file tail\
            #print(self.dtoEmployee.Image)
            if not (os.path.isfile("Image/" + self.dtoEmployee.Image)):
                dst_path = "Image/" + self.dtoEmployee.Image
                shutil.copy(src=image, dst=dst_path)

    def addEmployee(self):
        if(self.txtIDEmployee.text() == ""):
            IDE = 0
            with open("Config/employee.cfg", "r+") as file:
                for data in file:
                    ID = int(data.strip())
                    ID += 1
                    IDE = ID
                    if(ID > 0 and ID < 10):
                        self.dtoEmployee.IDEmployee = "NV0" + str(ID)
                    else:
                        self.dtoEmployee.IDEmployee = "NV" + str(ID)
            self.txtIDEmployee.setText(self.dtoEmployee.IDEmployee)
            self.dtoEmployee.FullName = self.txtFullName.text()
            self.dtoEmployee.Gender = self.comboGender.currentText()
            self.dtoEmployee.CitizenID = self.txtCitizenID.text()
            self.dtoEmployee.NumberPhone = self.txtNumberPhone.text()
            self.dtoEmployee.Address = self.txtAddress.text()
            self.dtoEmployee.Degree = self.txtDegree.text()
            self.getID_Faculty_Position()
            #self.dtoEmployee.IDFaculty = self.busEmployee.getIDFaculty(FacultyName=self.comboFaculty.currentText())
            #self.dtoEmployee.IDPosition = self.busEmployee.getIDPosition(PositionName=self.comboPosition.currentText())
            #self.dtoEmployee.TestPrint()
            if(self.txtFullName.text() != ""):
                result = self.busEmployee.addNewEmployee(dtoEmployee=self.dtoEmployee)
                if(result == 1):
                    with open("Config/employee.cfg", "w+") as file:
                        file.write(str(IDE) + "\n")
                    self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
                else:
                    self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Không được để trống tên nhân viên!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Nhân viên đã có trên hệ thống!", icon_type=1)
        self.loadData()
        self.clear()

    def updateEmployee(self):
        if(self.txtIDEmployee.text() != ""):
            if(self.txtFullName.text() != ""):
                self.dtoEmployee.IDEmployee = self.txtIDEmployee.text()
                self.dtoEmployee.FullName = self.txtFullName.text()
                self.dtoEmployee.Gender = self.comboGender.currentText()
                self.dtoEmployee.CitizenID = self.txtCitizenID.text()
                self.dtoEmployee.NumberPhone = self.txtNumberPhone.text()
                self.dtoEmployee.Address = self.txtAddress.text()
                self.dtoEmployee.Degree = self.txtDegree.text()
                self.getID_Faculty_Position()
                self.dtoEmployee.TestPrint() #Debug
                result = self.busEmployee.fixEmployee(dtoEmployee=self.dtoEmployee)
                if(result == 1):
                    self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
                else:
                    self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại", icon_type=1)
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Không được để trống tên nhân viên", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn nhân viên!", icon_type=1)
        self.loadData()
        self.clear()

    def deleteEmployee(self):
        if(self.txtIDEmployee.text() != ""):
            self.dtoEmployee.IDEmployee = self.txtIDEmployee.text()
            result = self.busEmployee.delEmployee(IDEmployee=self.dtoEmployee.IDEmployee)
            if(result == 1):
                self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn nhân viên để xóa!", icon_type=1)
        self.loadData()
        self.clear()

    def loadData(self):
        dataEmployee = self.busEmployee.loadData()
        self.dataTabEmployee.setRowCount(0)
        for row_number, row_data in enumerate(dataEmployee):
            self.dataTabEmployee.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabEmployee.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
                if(col_number == 8):
                    dataF = self.busEmployee.loadFaculty(IDFaculty=str(data))
                    self.dataTabEmployee.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(dataF)))
                if(col_number == 9):
                    dataP = self.busEmployee.loadPosition(IDPosition=str(data))
                    self.dataTabEmployee.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(dataP)))
        self.dataTabEmployee.resizeColumnsToContents()

    def cellClickOnDataTabEmployee(self):
        row = self.dataTabEmployee.currentRow()
        itemID = self.dataTabEmployee.item(row, 0).text()
        self.txtIDEmployee.setText(itemID)
        item = self.dataTabEmployee.item(row, 1).text()
        self.txtFullName.setText(item)
        item = self.dataTabEmployee.item(row, 2).text()
        item = item.split("-")
        dateSet = QDate(int(item[0]), int(item[1]), int(item[2]))
        self.deDateOfBirth.setDate(dateSet)
        self.onChangeDate(dateSet)
        item = self.dataTabEmployee.item(row, 3).text()
        self.comboGender.setCurrentText(item)
        item = self.dataTabEmployee.item(row, 4).text()
        self.txtCitizenID.setText(item)
        item = self.dataTabEmployee.item(row, 5).text()
        self.txtNumberPhone.setText(item)
        item = self.dataTabEmployee.item(row, 6).text()
        self.txtAddress.setText(item)
        item = self.dataTabEmployee.item(row, 7).text()
        self.txtDegree.setText(item)
        item = self.dataTabEmployee.item(row, 8).text()
        self.comboFaculty.setCurrentText(item)
        item = self.dataTabEmployee.item(row, 9).text()
        self.comboPosition.setCurrentText(item)
        self.getID_Faculty_Position()

        imgLink = self.busEmployee.getImageEmployee(IDEmployee=itemID)
        if(imgLink is not None and imgLink != ""):
            img = cv2.imread(("Image/" + imgLink))
            img = cv2.resize(img, (130, 160))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = img.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
            pixImg = convertToQtFormat.scaled(130, 160, Qt.KeepAspectRatio)
            self.lbImage.setPixmap(QtGui.QPixmap(pixImg))
            self.dtoEmployee.Image = imgLink
            #print(self.dtoEmployee.Image)
        else:
            self.lbImage.clear()
    
    def getFaculty(self):
        dataFaculty = self.busEmployee.loadAllFaculty()
        for data in dataFaculty:
            self.comboFaculty.addItem(data[0])

    def getPosition(self):
        dataPosition = self.busEmployee.loadAllPosition()
        for data in dataPosition:
            self.comboPosition.addItem(data[0])

    def getID_Faculty_Position(self):
        self.dtoEmployee.IDFaculty = self.busEmployee.getIDFaculty(FacultyName=self.comboFaculty.currentText())
        self.dtoEmployee.IDPosition = self.busEmployee.getIDPosition(PositionName=self.comboPosition.currentText())

    def onChangeDate(self, QDate):
        self.dtoEmployee.DateOfBirth = str(QDate.month()) + "/" +str(QDate.day()) + "/" +str(QDate.year())
        #print(self.dtoEmployee.DateOfBirth) #Debug

    
    def clear(self):
        self.txtIDEmployee.setText("")
        self.txtFullName.setText("")
        self.txtCitizenID.setText("")
        self.txtNumberPhone.setText("")
        self.txtAddress.setText("")
        self.txtDegree.setText("")
        self.txtAddress.setText("")
        self.lbImage.clear()