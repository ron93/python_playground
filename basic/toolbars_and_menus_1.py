# QTabWidget
import sys
import os
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QToolBar,
    QStatusBar,
    QCheckBox,
    
)
from layout_colorwidget import Color

base_dir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(
            QIcon(os.path.join(base_dir, "../icons/icons/bug.png")),
            "Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action_2 = QAction(
            QIcon(os.path.join(base_dir, "../icons/icons/bug.png")),
            "Your button", self)
        button_action_2.setStatusTip("This is your button 2")
        button_action_2.triggered.connect(self.onMyToolButtonClick)
        button_action_2.setCheckable(True)
        toolbar.addAction(button_action_2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

    def onMyToolButtonClick(self, s):
        print("click", s)

app=  QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
