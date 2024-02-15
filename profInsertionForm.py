# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profInsertionForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from output_dialog import Ui_Dialog_Output as q
from excel import Excel


class Ui_profInsertionForm(QtWidgets.QWidget):
    def setupUi(self, profInsertionForm):
        profInsertionForm.setObjectName("profInsertionForm")
        profInsertionForm.resize(779, 288)
        self.profNameFrame = QtWidgets.QFrame(profInsertionForm)
        self.profNameFrame.setGeometry(QtCore.QRect(370, 90, 371, 45))
        self.profNameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profNameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profNameFrame.setObjectName("profNameFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.profNameFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.profNameLabel = QtWidgets.QLabel(self.profNameFrame)
        self.profNameLabel.setObjectName("profNameLabel")
        self.gridLayout.addWidget(self.profNameLabel, 0, 2, 1, 1)
        self.profName = QtWidgets.QLineEdit(self.profNameFrame)
        self.profName.setObjectName("profName")
        self.gridLayout.addWidget(self.profName, 0, 1, 1, 1)
        self.profGradeFrame = QtWidgets.QFrame(profInsertionForm)
        self.profGradeFrame.setGeometry(QtCore.QRect(40, 90, 291, 45))
        self.profGradeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profGradeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profGradeFrame.setObjectName("profGradeFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.profGradeFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.profGrade = QtWidgets.QComboBox(self.profGradeFrame)
        self.profGrade.setObjectName("profGrade")
        self.profGrade.addItem("")
        self.profGrade.addItem("")
        self.profGrade.addItem("")
        self.profGrade.addItem("")
        self.profGrade.addItem("")
        self.profGrade.addItem("")
        self.profGrade.addItem("")
        self.gridLayout_2.addWidget(self.profGrade, 0, 0, 1, 1)
        self.profGradeLabel = QtWidgets.QLabel(self.profGradeFrame)
        self.profGradeLabel.setObjectName("profGradeLabel")
        self.gridLayout_2.addWidget(self.profGradeLabel, 0, 1, 1, 1)
        self.profBaseFrame = QtWidgets.QFrame(profInsertionForm)
        self.profBaseFrame.setGeometry(QtCore.QRect(580, 150, 161, 45))
        self.profBaseFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profBaseFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profBaseFrame.setObjectName("profBaseFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.profBaseFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.profBase = QtWidgets.QComboBox(self.profBaseFrame)
        self.profBase.setObjectName("profBase")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.profBase.addItem("")
        self.gridLayout_3.addWidget(self.profBase, 0, 0, 1, 1)
        self.profBaseLabel = QtWidgets.QLabel(self.profBaseFrame)
        self.profBaseLabel.setObjectName("profBaseLabel")
        self.gridLayout_3.addWidget(self.profBaseLabel, 0, 1, 1, 1)
        self.statusFrame = QtWidgets.QFrame(profInsertionForm)
        self.statusFrame.setGeometry(QtCore.QRect(110, 150, 221, 45))
        self.statusFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.statusFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statusFrame.setObjectName("statusFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.statusFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.status = QtWidgets.QComboBox(self.statusFrame)
        self.status.setObjectName("status")
        self.status.addItem("")
        self.status.addItem("")
        self.gridLayout_4.addWidget(self.status, 0, 0, 1, 1)
        self.statusLabel = QtWidgets.QLabel(self.statusFrame)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout_4.addWidget(self.statusLabel, 0, 1, 1, 1)
        self.appendProfBtn = QtWidgets.QPushButton(profInsertionForm)
        self.appendProfBtn.setGeometry(QtCore.QRect(340, 230, 101, 31))
        self.appendProfBtn.setObjectName("appendProfBtn")
        self.profListSelectionFrame = QtWidgets.QFrame(profInsertionForm)
        self.profListSelectionFrame.setGeometry(QtCore.QRect(40, 20, 701, 51))
        self.profListSelectionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profListSelectionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profListSelectionFrame.setObjectName("profListSelectionFrame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.profListSelectionFrame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.profListExploreBtn = QtWidgets.QPushButton(self.profListSelectionFrame)
        self.profListExploreBtn.setObjectName("profListExploreBtn")
        self.gridLayout_6.addWidget(self.profListExploreBtn, 0, 0, 1, 1)
        self.profListPath = QtWidgets.QLineEdit(self.profListSelectionFrame)
        self.profListPath.setObjectName("profListPath")
        self.gridLayout_6.addWidget(self.profListPath, 0, 1, 1, 1)
        self.profListSelectionLabel = QtWidgets.QLabel(self.profListSelectionFrame)
        self.profListSelectionLabel.setObjectName("profListSelectionLabel")
        self.gridLayout_6.addWidget(self.profListSelectionLabel, 0, 2, 1, 1)

        self.profListExploreBtn.clicked.connect(lambda: self.browseFiles('profListPath'))
        self.appendProfBtn.clicked.connect(self.appendProf)

        self.retranslateUi(profInsertionForm)
        QtCore.QMetaObject.connectSlotsByName(profInsertionForm)

    def browseFiles(self, lineEdit):
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, 'Choose File', '', 'Excel Files (*.xlsx)')
        getattr(self, lineEdit).setText(filePath[0])

    def appendProf(self):
        # error handling (change to persian)
        if self.profListPath.text() == '':
            q.tprint('لطفا فایل اساتید را انتخاب کنید')
            return
        if self.profName.text() == '':
            q.tprint('لطفا نام استاد را وارد کنید')
            return

        # appending prof to the file
        excel = Excel()
        prof = []
        prof.append(self.status.currentText())
        prof.append(self.profBase.currentText())
        prof.append(self.profGrade.currentText())
        prof.append(self.profName.text())
        excel.append(self.profListPath.text(), prof)
        q.tprint('استاد به لیست اضافه شد')

    def retranslateUi(self, profInsertionForm):
        _translate = QtCore.QCoreApplication.translate
        profInsertionForm.setWindowTitle(_translate("profInsertionForm", "Form"))
        self.profNameLabel.setText(_translate("profInsertionForm", "نام استاد"))
        self.profGrade.setItemText(0, _translate("profInsertionForm", "مربی آموزشیار (لیسانس)"))
        self.profGrade.setItemText(1, _translate("profInsertionForm", "مربی آموزشیار (فوق لیسانس)"))
        self.profGrade.setItemText(2, _translate("profInsertionForm", "مربی (فوق لیسانس)"))
        self.profGrade.setItemText(3, _translate("profInsertionForm", "مربی (دکتر)"))
        self.profGrade.setItemText(4, _translate("profInsertionForm", "استادیار"))
        self.profGrade.setItemText(5, _translate("profInsertionForm", "دانشیار"))
        self.profGrade.setItemText(6, _translate("profInsertionForm", "استاد"))
        self.profGradeLabel.setText(_translate("profInsertionForm", "مرتبه استاد"))
        self.profBase.setItemText(0, _translate("profInsertionForm", "1"))
        self.profBase.setItemText(1, _translate("profInsertionForm", "2"))
        self.profBase.setItemText(2, _translate("profInsertionForm", "3"))
        self.profBase.setItemText(3, _translate("profInsertionForm", "4"))
        self.profBase.setItemText(4, _translate("profInsertionForm", "5"))
        self.profBase.setItemText(5, _translate("profInsertionForm", "6"))
        self.profBase.setItemText(6, _translate("profInsertionForm", "7"))
        self.profBase.setItemText(7, _translate("profInsertionForm", "8"))
        self.profBase.setItemText(8, _translate("profInsertionForm", "9"))
        self.profBase.setItemText(9, _translate("profInsertionForm", "10"))
        self.profBase.setItemText(10, _translate("profInsertionForm", "11"))
        self.profBase.setItemText(11, _translate("profInsertionForm", "12"))
        self.profBase.setItemText(12, _translate("profInsertionForm", "13"))
        self.profBase.setItemText(13, _translate("profInsertionForm", "14"))
        self.profBase.setItemText(14, _translate("profInsertionForm", "15"))
        self.profBase.setItemText(15, _translate("profInsertionForm", "16"))
        self.profBase.setItemText(16, _translate("profInsertionForm", "17"))
        self.profBase.setItemText(17, _translate("profInsertionForm", "18"))
        self.profBase.setItemText(18, _translate("profInsertionForm", "19"))
        self.profBase.setItemText(19, _translate("profInsertionForm", "20"))
        self.profBase.setItemText(20, _translate("profInsertionForm", "21"))
        self.profBase.setItemText(21, _translate("profInsertionForm", "22"))
        self.profBase.setItemText(22, _translate("profInsertionForm", "23"))
        self.profBase.setItemText(23, _translate("profInsertionForm", "24"))
        self.profBase.setItemText(24, _translate("profInsertionForm", "25"))
        self.profBase.setItemText(25, _translate("profInsertionForm", "26"))
        self.profBase.setItemText(26, _translate("profInsertionForm", "27"))
        self.profBase.setItemText(27, _translate("profInsertionForm", "28"))
        self.profBase.setItemText(28, _translate("profInsertionForm", "29"))
        self.profBase.setItemText(29, _translate("profInsertionForm", "30"))
        self.profBaseLabel.setText(_translate("profInsertionForm", "پایه استاد"))
        self.status.setItemText(0, _translate("profInsertionForm", "هیئت علمی"))
        self.status.setItemText(1, _translate("profInsertionForm", "مدعو"))
        self.statusLabel.setText(_translate("profInsertionForm", "وضعیت استاد"))
        self.appendProfBtn.setText(_translate("profInsertionForm", "افزودن استاد"))
        self.profListExploreBtn.setText(_translate("profInsertionForm", "جستجو"))
        self.profListSelectionLabel.setText(_translate("profInsertionForm", "فایل اساتید"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profInsertionForm = QtWidgets.QWidget()
    ui = Ui_profInsertionForm()
    ui.setupUi(profInsertionForm)
    profInsertionForm.show()
    sys.exit(app.exec_())
