import sys

from  PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button1  = QPushButton("Open file")
        button1.clicked.connect(self.get_filename)

        self.setCentralWidget(button1)

    def get_filename(self):
        # file filter
        FILE_FILTERS = [
            "Portable Network Graphics File (*.png)",
            "Text files (*.txt)",
            "Comma Separated Values (*.csv)",
            "All files (*.*)",
        ]
        initial_filter = FILE_FILTERS[2] #*.csv
        filters = ';;'.join(FILE_FILTERS)
        print("Filter are:", filters)
        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            filter=filters)
        
        print("Result:", filename, selected_filter)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()