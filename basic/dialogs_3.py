# dialogs - QMessageBox
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
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a Question")
        
        dlg.setText("This is a question dialog!")
        
        """
        QMessageBox available buttons :
                QMessageBox.Ok
                QMessageBox.Open
                QMessageBox.Save
                QMessageBox.Cancel
                QMessageBox.Close
                QMessageBox.Discard
                QMessageBox.Apply
                QMessageBox.Reset
                QMessageBox.RestoreDefaults
                QMessageBox.Help
                QMessageBox.SaveAll
                QMessageBox.Yes
                QMessageBox.YesToAll
                QMessageBox.No
                QMessageBox.NoToAll
                QMessageBox.Abort
                QMessageBox.Retry
                QMessageBox.Ignore
                QMessageBox.NoButton
        """
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

            
        """
        QMessageBox icons:
                QMessageBox.Icon
                QMessageBox.Question
                QMessageBox.Information
                QMessageBox.Warning
                QMessageBox.Critical
        """
        dlg.setIcon(QMessageBox.Question)
        
        button = dlg.exec()

        if button == QMessageBox.Yes:
            print("Yes")
        else:
            print("No")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
