import sys
from PySide6.QtWidgets import (
    QApplication,
    QInputDialog,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit
)

class MainWindow(QMainWindow):
    def  __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        button1 = QPushButton("Interger")
        button1.clicked.connect(self.get_an_int)
        layout.addWidget(button1)

        button2 = QPushButton("Float")
        button2.clicked.connect(self.get_a_float)
        layout.addWidget(button2)

        button3 = QPushButton("Select")
        button3.clicked.connect(self.get_a_str_from_list)
        layout.addWidget(button3)

        button4 = QPushButton("String")
        button4.clicked.connect(self.get_a_str)
        layout.addWidget(button4)

        button5 = QPushButton("Text")
        button5.clicked.connect(self.get_text)
        layout.addWidget(button5)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_an_int(self):
        title = "Get an interger"
        label = "Enter a number"

        my_int_value, ok = QInputDialog.getInt(
            self,
            title, 
            label,
            value=0,
            minValue=-5,
            maxValue=5,
            step=1,
        )

        print("Result:", ok, my_int_value)

    def get_a_float(self):
        title = "Enter a float"
        label = "Type your float here"

        my_float_value, ok = QInputDialog.getDouble(
            self,
            title,
            label,
            value=0,
            minValue=-5.3,
            maxValue=5.7,
            decimals=2,
        )
        print("Result:", ok, my_float_value)

    def get_a_str_from_list(self):
        title = "Select a string"
        label = "Select a fruit from a list"
        items = ["apple", "pear", "orange", "grape"]

        initial_selection = 2 # orange from 0 index

        my_selected_str, ok = QInputDialog.getItem(
            self,
            title,
            label,
            items,
            current=initial_selection,
            # oprion to make dialog editable i.e add aitems
            editable=True
        )
        print("Result:", ok, my_selected_str)
    
    def get_a_str(self):
        title = "Enter a string"
        label = "Type your password"
        text = "my secret password"
        mode = QLineEdit.Password
        my_selected_str, ok = QInputDialog.getText(
            self, title, label, mode, text
        )
        print("Result:", ok, my_selected_str)
    
    def  get_text(self):
        title = "Enter text"
        label = "Type your novel here"
        text = "Once upon a time..."
        my_selected_str, ok = QInputDialog.getMultiLineText(
            self, title, label, text
        )
        print("Result:", ok, my_selected_str)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()