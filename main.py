from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette, QColor
import sys
import main_window

class ExampleApp(QtWidgets.QMainWindow, main_window.Ui_mainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    
    # theme {{{
    # palette to switch to dark colors:
    palette = QPalette()
    theme = ''
    if theme == 'dark':
        app.setStyle("gtk2")
        Qt.fg = QColor(255, 255, 255)
        Qt.bg = QColor(0, 0, 0)
        Qt.alert = QColor(255, 0, 0)
        Qt.window = QColor(53, 53, 53)
        Qt.base = QColor(25, 25, 25)
        Qt.link = QColor(42, 130, 218)
    else:
        app.setStyle("")
        Qt.bg = QColor(255, 255, 255)
        Qt.fg = QColor(0, 0, 0)
        Qt.alert = QColor(255, 0, 0)
        Qt.window = QColor(253, 253, 253)
        Qt.base = QColor(225, 225, 225)
        Qt.link = QColor(42, 130, 218)
    palette.setColor(QPalette.Window, Qt.window)
    palette.setColor(QPalette.WindowText, Qt.fg)
    palette.setColor(QPalette.Base, Qt.base)
    palette.setColor(QPalette.AlternateBase, Qt.window)
    palette.setColor(QPalette.ToolTipBase, Qt.bg)
    # palette.setColor(QPalette.GroupBox, Qt.bg)
    palette.setColor(QPalette.ToolTipText, Qt.fg)
    palette.setColor(QPalette.Text, Qt.fg)
    palette.setColor(QPalette.Button, Qt.window)
    palette.setColor(QPalette.ButtonText, Qt.fg)
    palette.setColor(QPalette.BrightText, Qt.alert)
    palette.setColor(QPalette.Link, Qt.link)
    palette.setColor(QPalette.Highlight, Qt.link)
    palette.setColor(QPalette.HighlightedText, Qt.bg)
    app.setPalette(palette)
    # }}}

    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
