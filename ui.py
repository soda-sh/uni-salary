# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from resources import logo_rc
from os.path import isfile

# dialog boxes
from output_dialog import Ui_Dialog_Output as q
import prompt
import profInsertionForm

# init the wrapper
from excel import Excel
import openpyxl
ss = Excel()


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(890, 707)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 161, 181))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/uni-logo/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.outputTable = QtWidgets.QTableView(self.centralwidget)
        self.outputTable.setGeometry(QtCore.QRect(10, 380, 851, 241))
        self.outputTable.setObjectName("outputTable")
        self.model = QtGui.QStandardItemModel() # Create a QStandardItemModel
        self.outputTable.setModel(self.model)
        self.outputTable.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.profSelectionFrame = QtWidgets.QFrame(self.centralwidget)
        self.profSelectionFrame.setGeometry(QtCore.QRect(530, 60, 301, 45))
        self.profSelectionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profSelectionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profSelectionFrame.setObjectName("profSelectionFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.profSelectionFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.profPrimaryKey = QtWidgets.QLineEdit(self.profSelectionFrame)
        self.profPrimaryKey.setObjectName("profPrimaryKey")
        self.gridLayout.addWidget(self.profPrimaryKey, 0, 0, 1, 1)
        self.profSelectionLabel = QtWidgets.QLabel(self.profSelectionFrame)
        self.profSelectionLabel.setObjectName("profSelectionLabel")
        self.gridLayout.addWidget(self.profSelectionLabel, 0, 1, 1, 1)
        self.profSelectionConfirmBtn = QtWidgets.QPushButton(self.centralwidget)
        self.profSelectionConfirmBtn.setGeometry(QtCore.QRect(540, 120, 89, 25))
        self.profSelectionConfirmBtn.setObjectName("profSelectionConfirmBtn")
        self.profDetailsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.profDetailsBox.setGeometry(QtCore.QRect(190, 50, 281, 121))
        self.profDetailsBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.profDetailsBox.setObjectName("profDetailsBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.profDetailsBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.profBaseLabel = QtWidgets.QLabel(self.profDetailsBox)
        self.profBaseLabel.setObjectName("profBaseLabel")
        self.gridLayout_2.addWidget(self.profBaseLabel, 2, 0, 1, 1)
        self.profBase = QtWidgets.QLabel(self.profDetailsBox)
        self.profBase.setText("")
        self.profBase.setObjectName("profBase")
        self.gridLayout_2.addWidget(self.profBase, 2, 1, 1, 1)
        self.profGradeLabel = QtWidgets.QLabel(self.profDetailsBox)
        self.profGradeLabel.setObjectName("profGradeLabel")
        self.gridLayout_2.addWidget(self.profGradeLabel, 1, 0, 1, 1)
        self.profGrade = QtWidgets.QLabel(self.profDetailsBox)
        self.profGrade.setText("")
        self.profGrade.setObjectName("profGrade")
        self.gridLayout_2.addWidget(self.profGrade, 1, 1, 1, 1)
        self.profNameLabel = QtWidgets.QLabel(self.profDetailsBox)
        self.profNameLabel.setObjectName("profNameLabel")
        self.gridLayout_2.addWidget(self.profNameLabel, 0, 0, 1, 1)
        self.profName = QtWidgets.QLabel(self.profDetailsBox)
        self.profName.setText("")
        self.profName.setObjectName("profName")
        self.gridLayout_2.addWidget(self.profName, 0, 1, 1, 1)
        self.profGradeLabel = QtWidgets.QLabel(self.profDetailsBox)
        self.profGradeLabel.setObjectName("profGradeLabel")
        self.gridLayout_2.addWidget(self.profGradeLabel, 1, 0, 1, 1)
        self.profGrade = QtWidgets.QLabel(self.profDetailsBox)
        self.profGrade.setText("")
        self.profGrade.setObjectName("profGrade")
        self.gridLayout_2.addWidget(self.profGrade, 1, 1, 1, 1)
        self.profBaseLabel = QtWidgets.QLabel(self.profDetailsBox)
        self.profBaseLabel.setObjectName("profBaseLabel")
        self.gridLayout_2.addWidget(self.profBaseLabel, 2, 0, 1, 1)
        self.profBase = QtWidgets.QLabel(self.profDetailsBox)
        self.profBase.setText("")
        self.profBase.setObjectName("profBase")
        self.gridLayout_2.addWidget(self.profBase, 2, 1, 1, 1)
        self.thesisInsertionBox = QtWidgets.QGroupBox(self.centralwidget)
        self.thesisInsertionBox.setGeometry(QtCore.QRect(10, 210, 861, 121))
        self.thesisInsertionBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.thesisInsertionBox.setObjectName("thesisInsertionBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.thesisInsertionBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.studentName = QtWidgets.QLineEdit(self.thesisInsertionBox)
        self.studentName.setObjectName("studentName")
        self.gridLayout_3.addWidget(self.studentName, 0, 1, 1, 1)
        self.studentNameLabel = QtWidgets.QLabel(self.thesisInsertionBox)
        self.studentNameLabel.setObjectName("studentNameLabel")
        self.gridLayout_3.addWidget(self.studentNameLabel, 0, 0, 1, 1)
        self.profPositionLabel = QtWidgets.QLabel(self.thesisInsertionBox)
        self.profPositionLabel.setObjectName("profPositionLabel")
        self.gridLayout_3.addWidget(self.profPositionLabel, 0, 4, 1, 1)
        self.activityTitleLabel = QtWidgets.QLabel(self.thesisInsertionBox)
        self.activityTitleLabel.setObjectName("activityTitleLabel")
        self.gridLayout_3.addWidget(self.activityTitleLabel, 0, 2, 1, 1)
        self.profPosition = QtWidgets.QComboBox(self.thesisInsertionBox)
        self.profPosition.setObjectName("profPosition")
        self.profPosition.addItem("")
        self.profPosition.addItem("")
        self.profPosition.addItem("")
        self.profPosition.addItem("")
        self.profPosition.addItem("")
        self.profPosition.addItem("")
        self.profPosition.addItem("")
        self.profPosition.addItem("")
        self.gridLayout_3.addWidget(self.profPosition, 0, 5, 1, 1)
        self.activityTitleLabel = QtWidgets.QLabel(self.thesisInsertionBox)
        self.activityTitleLabel.setObjectName("activityTitleLabel")
        self.gridLayout_3.addWidget(self.activityTitleLabel, 0, 2, 1, 1)
        self.studentNameLabel = QtWidgets.QLabel(self.thesisInsertionBox)
        self.studentNameLabel.setObjectName("studentNameLabel")
        self.gridLayout_3.addWidget(self.studentNameLabel, 0, 0, 1, 1)
        self.activityTitle = QtWidgets.QComboBox(self.thesisInsertionBox)
        self.activityTitle.setObjectName("activityTitle")
        self.activityTitle.addItem("")
        self.activityTitle.addItem("")
        self.activityTitle.addItem("")
        self.gridLayout_3.addWidget(self.activityTitle, 0, 3, 1, 1)
        self.unitCountFrame = QtWidgets.QFrame(self.thesisInsertionBox)
        self.unitCountFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.unitCountFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.unitCountFrame.setObjectName("unitCountFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.unitCountFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.unitCount = QtWidgets.QSpinBox(self.unitCountFrame)
        self.unitCount.setObjectName("unitCount")
        self.gridLayout_4.addWidget(self.unitCount, 0, 1, 1, 1)
        self.unitCountLabel = QtWidgets.QLabel(self.unitCountFrame)
        self.unitCountLabel.setObjectName("unitCountLabel")
        self.gridLayout_4.addWidget(self.unitCountLabel, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.unitCountFrame, 1, 3, 1, 1)
        self.addThesisBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addThesisBtn.setGeometry(QtCore.QRect(360, 340, 141, 31))
        self.addThesisBtn.setObjectName("addThesisBtn")
        self.confirmThesesBtn = QtWidgets.QPushButton(self.centralwidget)
        self.confirmThesesBtn.setGeometry(QtCore.QRect(390, 630, 89, 25))
        self.confirmThesesBtn.setObjectName("confirmThesesBtn")
        self.importFilesBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importFilesBtn.setGeometry(QtCore.QRect(540, 20, 90, 28))
        self.importFilesBtn.setObjectName("importFilesBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 30, 161, 16))
        self.label.setObjectName("label")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 23))
        self.menubar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionAppendProf = QtWidgets.QAction(mainWindow)
        self.actionAppendProf.setObjectName("actionAppendProf")
        self.menu.addAction(self.actionAppendProf)
        self.menubar.addAction(self.menu.menuAction())

        # init the table {{{
        self.tableViewCols = [
            "نام دانشجو",
            "عنوان فعالیت",
            "سمت استاد",
            "تعداد واحد",
            "نرخ",
        ]

        self.model.setHorizontalHeaderLabels(self.tableViewCols)
        # }}}

        # buttons {{{
        self.profSelectionConfirmBtn.clicked.connect(self.search_prof)
        self.addThesisBtn.clicked.connect(self.add_thesis)
        self.confirmThesesBtn.clicked.connect(self.write_down)
        self.importFilesBtn.clicked.connect(self.import_files)
        # }}}

        # menu {{{
        # check this
        # pj: done
        self.actionAppendProf.triggered.connect(self.appendProfForm)
        # }}}

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    # check this, doesn't show the window
    # pj: done
    def appendProfForm(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = profInsertionForm.Ui_profInsertionForm()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    # checkInputFiles {{{
    def checkInputFiles(self):
        try:
            file = open('inputFilesPath.txt', 'r')
        except FileNotFoundError:
            q.tprint('لطفا فایل های ورودی را انتخاب کنید')
            return False
        else:
            lines = file.readlines()
            self.profList = lines[0]
            self.profSalary = lines[1].strip()
            self.profSalary2 = lines[2].strip()
            self.profFormula = lines[3].strip()
            file.close()
            return True
    # }}}

    # import_files {{{
    def import_files(self):
        inputFilesPrompt = QtWidgets.QWidget()
        ui = prompt.Ui_inputFilesPrompt()
        ui.setupUi(inputFilesPrompt)
        inputFilesPrompt.show()
    # }}}

    # search_prof {{{
    def search_prof(self):
        if self.checkInputFiles():
            tmp = self.profPrimaryKey.text()

            if tmp == '' or tmp == None:
                q.tprint("نام استاد را وارد کنید")
                return False
            else:
                getProfColumn = ss.listSearch(self.profList.strip(), "نام", tmp)

            if getProfColumn:
                self.tmp_database = [
                    str(getProfColumn[0].value),  # name
                    str(getProfColumn[1].value),  # grade
                    str(getProfColumn[2].value),  # base
                ]
            else:
                return False

            # first and second "guide" shits
            _profPosition = self.profPosition.currentText().split(" - ")
            self.variable_profPosition = _profPosition[0]
            self.variable_activityTitle = self.activityTitle.currentText()
            self.variable_units = self.unitCount.value()

            if len(_profPosition) == 2:
                self.variable_profPosition = f"{_profPosition[0]} {_profPosition[1]}"

            self.variable_studentName = self.studentName.text()

            _conditions = [
                self.variable_profPosition.find("استاد راهنما"),
                self.variable_profPosition.find("استاد مشاور")
            ]

            # True when those are selected
            if _conditions[0] == 0 or _conditions[1] == 0:
                self.variable_price = ss.tableSearch(self.profSalary, "", self.tmp_database[2], int(self.tmp_database[1]))
                print(self.variable_price.value)
            else:

                if self.tmp_database[2].find("مربی") != -1:
                    self._tmp_profGrade = "مربی"
                self.variable_price = ss.tableSearch(self.profSalary2, "", self.variable_profPosition, self._tmp_profGrade)
                print(self.variable_price.value)

            # Do the shit with `self.withFormula here

            self.profName.setText(self.tmp_database[0])
            self.profBase.setText(self.tmp_database[1])
            self.profGrade.setText(self.tmp_database[2])
    # }}}

    # add_thesis {{{
    def add_thesis(self):
        _stat = self.search_prof()

        if _stat:
            if self.variable_units == 0:
                q.tprint("واحد درس نمیتواند صفر باشد")
                return

            # comes from sheets
            table = [[
                self.variable_studentName,
                self.variable_activityTitle,
                self.variable_profPosition,
                self.variable_units,
                self.variable_price.value,
            ],]

            self.add_items_to_model(table, self.tableViewCols)
        else:
            return False

        # # uncomment this for GUI output dialog box
        # q.tprint(f"search: {tmp}")

    # }}}

    # write_down {{{
    def write_down(self):
        print("Test")

        # store the latest table from UI to list
        updated_data = []
        for row in range(self.model.rowCount()):
            row_data = []
            for column in range(self.model.columnCount()):
                item = self.model.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    q.tprint(f"مقدار ({row}: {column}) نمیتوانند خالی باشند")
                    return
            updated_data.append(row_data[::-1])

        if updated_data == []:
            q.tprint("هیچ جدولی ساخته نشده است")
            return
        else:
            filePath = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', '', 'Excel Files (*.xlsx)')
            currentWorkbook = ss.createWorkbook(filePath[0])

            # write data to output file

            _key = [
                self.tmp_database[2],
                "پایه",
                self.tmp_database[1],
                "مرتبه",
                self.tmp_database[0],
                "نام",
            ]
            ss.append(currentWorkbook, _key)

            ss.append(currentWorkbook, [''])

            _key = [
                "نرخ",
                "تعداد واحد",
                "سمت استاد",
                "عنوان فعالیت",
                "نام و نام خانوادگی دانشچو",
            ]
            ss.append(currentWorkbook, _key)

            for key in updated_data:
                ss.append(currentWorkbook, key)

    # }}}

    # add_items_to_model {{{
    def add_items_to_model(self, table, cols):
        # Add items to the model
        # self.model.clear()
        self.model.setHorizontalHeaderLabels(cols)
        x = []
        rows = []
        # tmp = db.table_sort(f"{name}", "*", "id")
        for i in table:
            x.append(list(i))
        for i in range(len(x)):
            for j in range(len(x[i])):
                x[i][j] = QtGui.QStandardItem(str(x[i][j]))
            rows.append(x[i])
            self.model.appendRow(x[i])

        self.outputTable.setModel(self.model)
    # }}}

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "حقوق اساتید"))
        self.profSelectionLabel.setText(_translate("mainWindow", "نام استاد"))
        self.profSelectionConfirmBtn.setStatusTip(_translate("mainWindow", "انتخاب یک استاد برای ایجاد لیست حق التدریس"))
        self.profSelectionConfirmBtn.setText(_translate("mainWindow", "انتخاب استاد"))
        self.profDetailsBox.setTitle(_translate("mainWindow", "مشخصات استاد"))
        self.profBaseLabel.setText(_translate("mainWindow", "پایه استاد:"))
        self.profGradeLabel.setText(_translate("mainWindow", "رتبه استاد:"))
        self.profNameLabel.setText(_translate("mainWindow", "نام استاد:"))
        self.profGradeLabel.setText(_translate("mainWindow", "رتبه استاد:"))
        self.profBaseLabel.setText(_translate("mainWindow", "پایه استاد:"))
        self.thesisInsertionBox.setTitle(_translate("mainWindow", "اضافه کردن پایان‌نامه"))
        self.studentNameLabel.setText(_translate("mainWindow", "نام دانشجو"))
        self.profPositionLabel.setText(_translate("mainWindow", "سمت استاد"))
        self.activityTitleLabel.setText(_translate("mainWindow", "عنوان فعالیت"))
        self.profPosition.setItemText(0, _translate("mainWindow", "استاد راهنما"))
        self.profPosition.setItemText(1, _translate("mainWindow", "استاد راهنما - مشترک اول"))
        self.profPosition.setItemText(2, _translate("mainWindow", "استاد راهنما - مشترک دوم"))
        self.profPosition.setItemText(3, _translate("mainWindow", "استاد مشاور"))
        self.profPosition.setItemText(4, _translate("mainWindow", "استاد مشاور - مشترک اول"))
        self.profPosition.setItemText(5, _translate("mainWindow", "استاد مشاور - مشترک دوم"))
        self.profPosition.setItemText(6, _translate("mainWindow", "ناظر تحصیلات تکمیلی"))
        self.profPosition.setItemText(7, _translate("mainWindow", "داور"))
        self.activityTitleLabel.setText(_translate("mainWindow", "عنوان فعالیت"))
        self.studentNameLabel.setText(_translate("mainWindow", "نام دانشجو"))
        self.activityTitle.setItemText(0, _translate("mainWindow", "دفاع پایان نامه کارشناسی ارشد"))
        self.activityTitle.setItemText(1, _translate("mainWindow", "دفاع از پروپوزال دکتری"))
        self.activityTitle.setItemText(2, _translate("mainWindow", "دفاع نهایی رساله دکتری"))
        self.unitCountLabel.setText(_translate("mainWindow", "تعداد واحد پایان‌نامه"))
        self.addThesisBtn.setStatusTip(_translate("mainWindow", "افزودن پایان‌نامه به جدول زیر"))
        self.addThesisBtn.setText(_translate("mainWindow", "افزودن پایان‌نامه"))
        self.confirmThesesBtn.setStatusTip(_translate("mainWindow", "ایجاد فایل خروجی با محتوای جدول"))
        self.confirmThesesBtn.setText(_translate("mainWindow", "تایید"))
        self.importFilesBtn.setStatusTip(_translate("mainWindow", "انتخاب فایل های ورودی برنامه"))
        self.importFilesBtn.setText(_translate("mainWindow", "افزودن"))
        self.label.setText(_translate("mainWindow", "فایل‌های ورودی"))
        self.menu.setTitle(_translate("mainWindow", "منو"))
        self.actionAppendProf.setText(_translate("mainWindow", "افزودن استاد"))
        self.actionAppendProf.setStatusTip(_translate("mainWindow", "افزودن استاد به فایل اساتید"))
        self.actionAppendProf.setShortcut(_translate("mainWindow", "Ctrl+A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    ui.checkInputFiles()
    sys.exit(app.exec_())
