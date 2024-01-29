# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_thesis_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from output_dialog import Ui_Dialog_Output

# helper {{{

def qprint(msg):
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_Dialog_Output(msg)
    dialog.ui.setupUi(dialog)
    dialog.exec_()

# }}}

class Ui_newThesForm(object):
    def setupUi(self, newThesForm):
        self.newThesForm = newThesForm
        newThesForm.setObjectName("newThesForm")
        newThesForm.resize(596, 188)
        self.gridLayout = QtWidgets.QGridLayout(newThesForm)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.thesName = QtWidgets.QLineEdit(newThesForm)
        self.thesName.setObjectName("thesName")
        self.verticalLayout_8.addWidget(self.thesName)
        self.lineEdit = QtWidgets.QLineEdit(newThesForm)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_8.addWidget(self.lineEdit)
        self.thesBase = QtWidgets.QComboBox(newThesForm)
        self.thesBase.setObjectName("thesBase")
        self.verticalLayout_8.addWidget(self.thesBase)
        self.thesBase.addItem("")
        self.thesBase.addItem("")
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.thesNameLabel_2 = QtWidgets.QLabel(newThesForm)
        self.thesNameLabel_2.setObjectName("thesNameLabel_2")
        self.verticalLayout_7.addWidget(self.thesNameLabel_2)
        self.thesBaseLabel = QtWidgets.QLabel(newThesForm)
        self.thesBaseLabel.setObjectName("thesBaseLabel")
        self.verticalLayout_7.addWidget(self.thesBaseLabel)
        self.label = QtWidgets.QLabel(newThesForm)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.thesId = QtWidgets.QLineEdit(newThesForm)
        self.thesId.setObjectName("thesId")
        self.verticalLayout_6.addWidget(self.thesId)
        self.thesGrade = QtWidgets.QComboBox(newThesForm)
        self.thesGrade.setObjectName("thesGrade")
        self.thesGrade.addItem("")
        self.thesGrade.addItem("")
        self.verticalLayout_6.addWidget(self.thesGrade)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.thesIdLabel_2 = QtWidgets.QLabel(newThesForm)
        self.thesIdLabel_2.setObjectName("thesIdLabel_2")
        self.verticalLayout_5.addWidget(self.thesIdLabel_2)
        self.thesGradeLabel = QtWidgets.QLabel(newThesForm)
        self.thesGradeLabel.setObjectName("thesGradeLabel")
        self.verticalLayout_5.addWidget(self.thesGradeLabel)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cancelBtn = QtWidgets.QPushButton(newThesForm)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_6.addWidget(self.cancelBtn)
        self.confirmBtn = QtWidgets.QPushButton(newThesForm)
        self.confirmBtn.setObjectName("confirmBtn")
        self.horizontalLayout_6.addWidget(self.confirmBtn)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        # buttons {{{
        self.cancelBtn.clicked.connect(self.cancel_clicked)
        self.confirmBtn.clicked.connect(self.confirm_clicked)
        # }}}

        self.retranslateUi(newThesForm)
        QtCore.QMetaObject.connectSlotsByName(newThesForm)

    # signals {{{
    def confirm_clicked(self):
        qprint("اطلاعات ذخیرده شد")

    def cancel_clicked(self):
        self.newThesForm.close()
    # }}}

    def retranslateUi(self, newThesForm):
        _translate = QtCore.QCoreApplication.translate
        newThesForm.setWindowTitle(_translate("newThesForm", "Form"))
        self.thesBase.setItemText(0, _translate("newProfForm", "مقطع اول"))
        self.thesBase.setItemText(1, _translate("newProfForm", "مقطع دوم"))
        self.thesNameLabel_2.setText(_translate("newThesForm", "<html><head/><body><p align=\"center\">شماره دانشجویی</p></body></html>"))
        self.thesBaseLabel.setText(_translate("newThesForm", "<html><head/><body><p align=\"center\">آی‌دی استاد</p></body></html>"))
        self.label.setText(_translate("newThesForm", "<html><head/><body><p align=\"center\">مقطع پایان‌نامه</p></body></html>"))
        self.thesGrade.setItemText(0, _translate("newProfForm", "وضعیت اول"))
        self.thesGrade.setItemText(1, _translate("newProfForm", "وضعیت دوم"))
        self.thesIdLabel_2.setText(_translate("newThesForm", "<html><head/><body><p align=\"center\">نام و نام خانوادگی</p></body></html>"))
        self.thesGradeLabel.setText(_translate("newThesForm", "<html><head/><body><p align=\"center\">وضعیت پایان‌نامه</p></body></html>"))
        self.confirmBtn.setText(_translate("newThesForm", "تایید"))
        self.cancelBtn.setText(_translate("newThesForm", "انصراف"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newThesForm = QtWidgets.QWidget()
    ui = Ui_newThesForm()
    ui.setupUi(newThesForm)
    newThesForm.show()
    sys.exit(app.exec_())
