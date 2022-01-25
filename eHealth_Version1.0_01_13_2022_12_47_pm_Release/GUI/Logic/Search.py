from PyQt5.QtWidgets import QFrame
from PyQt5 import QtWidgets
from GUI.View.Ui_Search import Ui_Search
from GUI.Logic.Noticfication import Notification
from BUS.BUS_Search import BUS_Search

class Search(QFrame, Ui_Search):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.busSearch = BUS_Search()
        self.state = 2
        self.chooseType = 2
        
        # Event Handle
        self.radioBTID.toggled.connect(self.selectID)
        self.radioBTFullName.toggled.connect(self.selectFullName)
        self.radioBTEmployee.toggled.connect(self.selectEmployee)
        self.radioBTPatient.toggled.connect(self.selectPatient)
        self.btSearch.clicked.connect(self.search)

    def showDataEmployee(self, dataEmp):
        self.dataTab.setColumnCount(7)
        self.dataTab.setRowCount(0)
        self.dataTab.setHorizontalHeaderLabels("Mã Nhân Viên;Họ Tên;Ngày Sinh;Giới Tính;Số Căn Cước;Số Điện Thoại;Địa Chỉ".split(";"))
        for row_number, row_data in enumerate(dataEmp):
            self.dataTab.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTab.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
        self.dataTab.resizeColumnsToContents()

    def showDataPatient(self, dataPat):
        self.dataTab.setColumnCount(10)
        self.dataTab.setRowCount(0)
        self.dataTab.setHorizontalHeaderLabels("Mã Bệnh Nhân;Họ Tên;Tuổi;Giới Tính;Dân Tộc;Nghề Nghiệp;Địa Chỉ;Số Điện Thoại;Số Căn Cước;Số BHYT".split(";"))
        for row_number, row_data in enumerate(dataPat):
            self.dataTab.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTab.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
        self.dataTab.resizeColumnsToContents()

    def selectID(self, selected):
        if selected:
            self.state = 1

    def selectFullName(self, selected):
        if selected:
            self.state = 0

    def selectEmployee(self, selected):
        if selected:
            self.chooseType = 1

    def selectPatient(self, selected):
        if selected:
            self.chooseType = 0

    def search(self):
        if(self.chooseType == 1):
            if(self.state == 1):
                data = self.busSearch.searchEmployee(State=self.state, IDEmployee=self.txtSearch.text())
                self.showDataEmployee(dataEmp=data)
            elif(self.state == 0):
                data = self.busSearch.searchEmployee(State=self.state, FullName=self.txtSearch.text())
                self.showDataEmployee(dataEmp=data)
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Chưa Chọn Tìm Kiếm Theo ID Hay Họ Tên!", icon_type=1)
        elif(self.chooseType == 0):
            if(self.state == 1):
                data = self.busSearch.searchPatient(State=self.state, IDPatient=self.txtSearch.text())
                self.showDataPatient(dataPat=data)
            elif(self.state == 0):
                data = self.busSearch.searchPatient(State=self.state, FullName=self.txtSearch.text())
                self.showDataPatient(dataPat=data)
            else:
                self.noticfication = Notification(title="Chưa Chọn Tìm Kiếm Theo ID Hay Họ Tên!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa Chọn Loại Tìm Kiếm!", icon_type=1)