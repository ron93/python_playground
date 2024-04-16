import os
import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
basedir = os.path.dirname(__file__)

class MainUI(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load(
            os.path.join(basedir, "mainwindow.ui"), None
        )
        self.ui.setWindowTitle("Main Window Title")
        self.ui.show()

app = QtWidgets.QApplication(sys.argv)
ui = MainUI()
app.exec()