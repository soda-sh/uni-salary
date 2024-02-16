# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from output_dialog import Ui_Dialog_Output as q


# window to get input files from the user and save the file paths in inputFilesPath.txt
# sample input files are inside input-excel-files directory
class Ui_inputFilesPrompt(QtWidgets.QWidget):
    def setupUi(self, inputFilesPrompt):
        self.inputFilesPrompt = inputFilesPrompt
        inputFilesPrompt.setObjectName("inputFilesPrompt")
        inputFilesPrompt.resize(675, 265)
        self.profSalaryFrame = QtWidgets.QFrame(inputFilesPrompt)
        self.profSalaryFrame.setGeometry(QtCore.QRect(140, 110, 511, 51))
        self.profSalaryFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profSalaryFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profSalaryFrame.setObjectName("profSalaryFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.profSalaryFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.profSalaryPath = QtWidgets.QLineEdit(self.profSalaryFrame)
        self.profSalaryPath.setObjectName("profSalaryPath")
        self.gridLayout_2.addWidget(self.profSalaryPath, 0, 1, 1, 1)
        self.profSalaryExploreBtn = QtWidgets.QPushButton(self.profSalaryFrame)
        self.profSalaryExploreBtn.setObjectName("profSalaryExploreBtn")
        self.gridLayout_2.addWidget(self.profSalaryExploreBtn, 0, 0, 1, 1)
        self.profSalaryLabel = QtWidgets.QLabel(self.profSalaryFrame)
        self.profSalaryLabel.setObjectName("profSalaryLabel")
        self.gridLayout_2.addWidget(self.profSalaryLabel, 0, 3, 1, 1)
        self.profListFrame = QtWidgets.QFrame(inputFilesPrompt)
        self.profListFrame.setGeometry(QtCore.QRect(140, 50, 511, 51))
        self.profListFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profListFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profListFrame.setObjectName("profListFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.profListFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.profListPath = QtWidgets.QLineEdit(self.profListFrame)
        self.profListPath.setObjectName("profListPath")
        self.gridLayout.addWidget(self.profListPath, 0, 1, 1, 1)
        self.profListLabel = QtWidgets.QLabel(self.profListFrame)
        self.profListLabel.setObjectName("profListLabel")
        self.gridLayout.addWidget(self.profListLabel, 0, 3, 1, 1)
        self.profListExploreBtn = QtWidgets.QPushButton(self.profListFrame)
        self.profListExploreBtn.setObjectName("profListExploreBtn")
        self.gridLayout.addWidget(self.profListExploreBtn, 0, 0, 1, 1)
        self.confirmFilesBtn = QtWidgets.QPushButton(inputFilesPrompt)
        self.confirmFilesBtn.setGeometry(QtCore.QRect(20, 120, 91, 41))
        self.confirmFilesBtn.setObjectName("confirmFilesBtn")
        self.profSalaryFrame2 = QtWidgets.QFrame(inputFilesPrompt)
        self.profSalaryFrame2.setGeometry(QtCore.QRect(140, 170, 511, 51))
        self.profSalaryFrame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profSalaryFrame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profSalaryFrame2.setObjectName("profSalaryFrame2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.profSalaryFrame2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.profSalaryPath2 = QtWidgets.QLineEdit(self.profSalaryFrame2)
        self.profSalaryPath2.setObjectName("profSalaryPath2")
        self.gridLayout_3.addWidget(self.profSalaryPath2, 0, 1, 1, 1)
        self.profSalaryLabel2 = QtWidgets.QLabel(self.profSalaryFrame2)
        self.profSalaryLabel2.setObjectName("profSalaryLabel2")
        self.gridLayout_3.addWidget(self.profSalaryLabel2, 0, 3, 1, 1)
        self.profSalaryExploreBtn2 = QtWidgets.QPushButton(self.profSalaryFrame2)
        self.profSalaryExploreBtn2.setObjectName("profSalaryExploreBtn2")
        self.gridLayout_3.addWidget(self.profSalaryExploreBtn2, 0, 0, 1, 1)

        # button press handling
        self.confirmFilesBtn.clicked.connect(self.confirmFiles)
        self.profSalaryExploreBtn.clicked.connect(lambda: self.browseFiles('profSalaryPath'))
        self.profSalaryExploreBtn2.clicked.connect(lambda: self.browseFiles('profSalaryPath2'))
        self.profListExploreBtn.clicked.connect(lambda: self.browseFiles('profListPath'))

        self.retranslateUi(inputFilesPrompt)
        QtCore.QMetaObject.connectSlotsByName(inputFilesPrompt)

    def retranslateUi(self, inputFilesPrompt):
        _translate = QtCore.QCoreApplication.translate
        inputFilesPrompt.setWindowTitle(_translate("inputFilesPrompt", "Form"))
        self.profSalaryExploreBtn.setText(_translate("inputFilesPrompt", "جستجو"))
        self.profSalaryLabel.setText(_translate("inputFilesPrompt", "فایل حق‌التدریس"))
        self.profListLabel.setText(_translate("inputFilesPrompt", "فایل اساتید"))
        self.profListExploreBtn.setText(_translate("inputFilesPrompt", "جستجو"))
        self.confirmFilesBtn.setText(_translate("inputFilesPrompt", "تایید فایل‌ها"))
        self.profSalaryLabel2.setText(_translate("inputFilesPrompt", "فایل حقوق ثابت"))
        self.profSalaryExploreBtn2.setText(_translate("inputFilesPrompt", "جستجو"))

    # opens a file browser for the user, then writes the file path to the corresponding line edit
    def browseFiles(self, lineEdit):
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, 'Choose File', '', 'Excel Files (*.xlsx)')
        getattr(self, lineEdit).setText(filePath[0])

    def confirmFiles(self):
        # error handling, checking for empty fields
        err = 0
        if self.profListPath.text() == '':
            err += 1

        if self.profSalaryPath.text() == '':
            err += 1

        if self.profSalaryPath2.text() == '':
            err += 1

        # err == 0 means everything is ok, no errors
        if err == 0:
            # saving file paths inside inputFilesPath.txt for later usage
            with open('inputFilesPath.txt', 'w') as file:
                file.write(f'{self.profListPath.text()}\n')
                file.write(f'{self.profSalaryPath.text()}\n')
                file.write(f'{self.profSalaryPath2.text()}\n')

            self.inputFilesPrompt.close()

        # informing the user of the error
        else:
            q.tprint('لطفا تمام فایل ها را انتخاب کنید')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inputFilesPrompt = QtWidgets.QWidget()
    ui = Ui_inputFilesPrompt()
    ui.setupUi(inputFilesPrompt)
    inputFilesPrompt.show()
    sys.exit(app.exec_())
