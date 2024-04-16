from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget
)

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.label = QLabel()

        self.input = QLineEdit()
        # textChanged -> signal. label -> slot to setText from input
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # set the central widget of the window
        self.setCentralWidget(container)

app = QApplication(sys.argv)        

window = MainWindow()
window.show()

app.exec()