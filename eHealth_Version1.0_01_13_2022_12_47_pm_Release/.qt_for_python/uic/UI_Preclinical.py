# Form implementation generated from reading ui file 'e:\A_Do_An_Endgames\Dev\eHealth_Version1.0_11_19_2021_1_58_pm_Debug\GUI\Design\UI_Preclinical.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Preclinical(object):
    def setupUi(self, Preclinical):
        Preclinical.setObjectName("Preclinical")
        Preclinical.resize(754, 590)
        Preclinical.setMinimumSize(QtCore.QSize(555, 540))
        font = QtGui.QFont()
        font.setPointSize(12)
        Preclinical.setFont(font)
        Preclinical.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Preclinical)
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Preclinical)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabPreclinical = QtWidgets.QTabWidget(Preclinical)
        self.tabPreclinical.setMinimumSize(QtCore.QSize(0, 26))
        self.tabPreclinical.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabPreclinical.setFont(font)
        self.tabPreclinical.setObjectName("tabPreclinical")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabPreclinical.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabPreclinical.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabPreclinical.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabPreclinical.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabPreclinical.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabPreclinical.addTab(self.tab_6, "")
        self.verticalLayout.addWidget(self.tabPreclinical)
        self.mainFrame = QtWidgets.QFrame(Preclinical)
        self.mainFrame.setMinimumSize(QtCore.QSize(540, 353))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mainFrame.setFont(font)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.verticalLayout_2.addLayout(self.mainLayout)
        self.verticalLayout.addWidget(self.mainFrame)
        self.verticalLayout.setStretch(2, 9)

        self.retranslateUi(Preclinical)
        self.tabPreclinical.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Preclinical)

    def retranslateUi(self, Preclinical):
        _translate = QtCore.QCoreApplication.translate
        Preclinical.setWindowTitle(_translate("Preclinical", "Cận Lâm Sàng - IDPatient - FullName"))
        self.label.setText(_translate("Preclinical", "Cận Lâm Sàng"))
        self.tabPreclinical.setTabText(self.tabPreclinical.indexOf(self.tab), _translate("Preclinical", "X-Quang"))
        self.tabPreclinical.setTabText(self.tabPreclinical.indexOf(self.tab_2), _translate("Preclinical", "CT Scan"))
        self.tabPreclinical.setTabText(self.tabPreclinical.indexOf(self.tab_3), _translate("Preclinical", "MRI"))
        self.tabPreclinical.setTabText(self.tabPreclinical.indexOf(self.tab_4), _translate("Preclinical", "Siêu Âm"))
        self.tabPreclinical.setTabText(self.tabPreclinical.indexOf(self.tab_5), _translate("Preclinical", "Xét Nghiệm"))
        self.tabPreclinical.setTabText(self.tabPreclinical.indexOf(self.tab_6), _translate("Preclinical", "Điện Đồ"))
