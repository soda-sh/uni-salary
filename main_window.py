# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.uniLogo = QtWidgets.QLabel(self.centralwidget)
        self.uniLogo.setGeometry(QtCore.QRect(30, 20, 100, 100))
        self.uniLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.uniLogo.setObjectName("uniLogo")
        self.profNameFrame = QtWidgets.QFrame(self.centralwidget)
        self.profNameFrame.setGeometry(QtCore.QRect(110, 350, 241, 45))
        self.profNameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profNameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profNameFrame.setObjectName("profNameFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.profNameFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.profNameLabel = QtWidgets.QLabel(self.profNameFrame)
        self.profNameLabel.setObjectName("profNameLabel")
        self.gridLayout.addWidget(self.profNameLabel, 0, 0, 1, 1)
        self.profName = QtWidgets.QLineEdit(self.profNameFrame)
        self.profName.setObjectName("profName")
        self.gridLayout.addWidget(self.profName, 0, 1, 1, 1)
        self.profIdFrame = QtWidgets.QFrame(self.centralwidget)
        self.profIdFrame.setGeometry(QtCore.QRect(110, 410, 235, 45))
        self.profIdFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profIdFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profIdFrame.setObjectName("profIdFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.profIdFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.profIdLabel = QtWidgets.QLabel(self.profIdFrame)
        self.profIdLabel.setObjectName("profIdLabel")
        self.gridLayout_2.addWidget(self.profIdLabel, 0, 0, 1, 1)
        self.profId = QtWidgets.QLineEdit(self.profIdFrame)
        self.profId.setObjectName("profId")
        self.gridLayout_2.addWidget(self.profId, 0, 1, 1, 1)
        self.profBaseFrame = QtWidgets.QFrame(self.centralwidget)
        self.profBaseFrame.setGeometry(QtCore.QRect(380, 350, 179, 45))
        self.profBaseFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profBaseFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profBaseFrame.setObjectName("profBaseFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.profBaseFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.profBase = QtWidgets.QComboBox(self.profBaseFrame)
        self.profBase.setObjectName("profBase")
        self.gridLayout_3.addWidget(self.profBase, 0, 1, 1, 1)
        self.profBaseLabel = QtWidgets.QLabel(self.profBaseFrame)
        self.profBaseLabel.setObjectName("profBaseLabel")
        self.gridLayout_3.addWidget(self.profBaseLabel, 0, 0, 1, 1)
        self.profGradeFrame = QtWidgets.QFrame(self.centralwidget)
        self.profGradeFrame.setGeometry(QtCore.QRect(370, 410, 179, 45))
        self.profGradeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profGradeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profGradeFrame.setObjectName("profGradeFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.profGradeFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.profGradeLabel = QtWidgets.QLabel(self.profGradeFrame)
        self.profGradeLabel.setObjectName("profGradeLabel")
        self.gridLayout_4.addWidget(self.profGradeLabel, 0, 0, 1, 1)
        self.profGrade = QtWidgets.QComboBox(self.profGradeFrame)
        self.profGrade.setObjectName("profGrade")
        self.gridLayout_4.addWidget(self.profGrade, 0, 1, 1, 1)
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchBtn.setGeometry(QtCore.QRect(610, 390, 89, 25))
        self.searchBtn.setObjectName("searchBtn")
        self.newProfBtn = QtWidgets.QPushButton(self.centralwidget)
        self.newProfBtn.setGeometry(QtCore.QRect(190, 40, 91, 61))
        self.newProfBtn.setObjectName("newProfBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.uniLogo.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:20pt;\">Logo</span></p></body></html>"))
        self.profNameLabel.setText(_translate("MainWindow", "Prof Name"))
        self.profIdLabel.setText(_translate("MainWindow", "Prof ID"))
        self.profBaseLabel.setText(_translate("MainWindow", "Prof Base"))
        self.profGradeLabel.setText(_translate("MainWindow", "Prof Grade"))
        self.searchBtn.setText(_translate("MainWindow", "Search"))
        self.newProfBtn.setText(_translate("MainWindow", "New Prof"))
