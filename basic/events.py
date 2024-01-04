import sys
 
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QTextEdit
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
        self.setMouseTracking(True)

    
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")


    def mousePressEvent(self, e):
        # self.label.setText("mousePressEvent")

        # respond to diffrent mouse buttons click i.e middle,left,right
        if e.button() == Qt.LeftButton:
            # handle left-button press
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            # handle middle_button press
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            # handle right-button press
            self.label.setText("mousePressEvent RIGHT")

        
    # calling super to pass event to the normal handler 
    # def mousePressEvent(self, e) -> None:
    #     return super().mousePressEvent(e)
        
    def mouseReleaseEvent(self, e):
        # self.label.setText("mouseReleaseEvent")
        # respond to diffrent mouse buttons click i.e middle,left,right
        if e.button() == Qt.LeftButton:
            # handle left-button press
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            # handle middle_button press
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            # handle right-button press
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        # self.label.setText("mouseDoubleClickEvent")
        # respond to diffrent mouse buttons click i.e middle,left,right
        if e.button() == Qt.LeftButton:
            # handle left-button press
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            # handle middle_button press
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            # handle right-button press
            self.label.setText("mouseDoubleClickEvent RIGHT")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()