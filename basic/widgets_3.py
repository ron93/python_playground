import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox("This is a checkbox")
        # set checkbox state
        # ->.setChecked(True | False)
        # ->.setCheckedState(Qt.Checked | Qt.UnChecked | Qt.PartiallyChecked)
        widget.setCheckState(Qt.Checked)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)

app = QApplication(sys.argv)        
window = MainWindow()
window.show()

app.exec()
