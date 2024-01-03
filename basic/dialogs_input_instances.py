import sys

from PySide6.QtWidgets import (
    QApplication,
    QInputDialog,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QComboBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        button1 = QPushButton("Integer")
        button1.clicked.connect(self.get_an_int)
        layout.addWidget(button1)

        button2 = QPushButton("Float")
        button2.clicked.connect(self.get_a_float)
        layout.addWidget(button2)

        button3 = QPushButton("Select")
        button3.clicked.connect(self.get_a_str_from_list)
        layout.addWidget(button3)

        button4 = QPushButton("String")
        button4.clicked.connect(self.get_str)
        layout.addWidget(button4)

        button5 = QPushButton("Text")
        button5.clicked.connect(self.get_text)
        layout.addWidget(button5)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_an_int(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter an  integer")
        dialog.setLabelText("Type your integer here")
        dialog.setIntValue(0)
        dialog.setIntMinimum(-5)
        dialog.setIntMinimum(5)
        dialog.setIntStep(1)

        ok = dialog.exec()
        print("Result:", ok, dialog.intValue())
    
    def get_a_float(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter a float")
        dialog.setLabelText("Type your float here")
        dialog.setDoubleValue(0.0)
        dialog.setDoubleMinimum(-5.3)
        dialog.setDoubleMaximum(5.4)
        dialog.setDoubleDecimals(2)

        ok = dialog.exec()
        print("Result:", ok, dialog.doubleValue())

    def get_a_str_from_list(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("select a string")
        dialog.setLabelText("select a fruit from a list")
        dialog.setComboBoxItems(["apple", "pear", "orange", "grape"])
        dialog.setTextValue("apple")

        ok = dialog.exec()

        print("Result:", ok, dialog.textValue())

    def get_str(self):
        pass

    def get_text(self):
        pass

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()