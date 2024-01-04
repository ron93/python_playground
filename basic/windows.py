import sys
from random import randint

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
)

class AnotherWindow(QWidget):
    """
    This 'window' is a QWidget. If it has no parent, it will
    appear as  a free floating window
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window %d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.w = None # no external window  created -- used with show_new_window_old function

        # creates new window only once
        self.w = AnotherWindow()

        self.button = QPushButton("Push for Window")
        # self.button.clicked.connect(self.show_new_window)
        self.button.clicked.connect(self.toggle_window)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.w.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.input)
        container = QWidget()
        container.setLayout(layout)


        self.setCentralWidget(container)

    # def show_new_window_old(self,checked):
        # if self.w is None:
        #     # runs if another window 'w' doesn't exist
        #     self.w = AnotherWindow()
        #     self.w.show()

        # # close window
        # else:
        #     self.w.close()
        #     self.w = None # discard reference, close window
    
    # def show_new_window(self,checked):
    #     self.w.show()

    def toggle_window(self, checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()