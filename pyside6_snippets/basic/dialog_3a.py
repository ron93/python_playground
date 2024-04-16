# dialogs - QMessageBox without instance
# dialog_1-3 -pg118
import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QMessageBox,
    QDialog
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        """Staic methods that can be used to show message :
                QMessageBox.about(parent, title, message)
                QMessageBox.critical(parent, title, message)
                QMessageBox.information(parent, title, message)
                QMessageBox.question(parent, title, message)
                QMessageBox.warning(parent, title, message)
                
                N.B// parent is  the window which the dialog will be the chil of i.e MainWindow -> self
        """
        button = QMessageBox.question(self,"Question Dialog", "The Longer message")

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
