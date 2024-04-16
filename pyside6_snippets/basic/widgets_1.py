import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        # get current font from desktop
        font = widget.font()
        font.setPointSize(30)
        # set widget font
        widget.setFont(font)
        # flags for horizontal alighnement : Qt.AlignLeft, Qt.AlignRight, Qt.AlignHCenter, Qt.AlignJustify
        # flags for vertical alignment : Qt.AlignTop, Qt.AlignBottom, Qt.AlignVCenter
        # flag for alignment in both directions : Qt.AlignCenter``
        # combining flags i.e horizontal_alignment | vertical_alignment
        widget.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        self.setCentralWidget(widget)
 
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()        