import sys
 
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QAction
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QTextEdit,
    QMenu
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
        self.setMouseTracking(True)

    # context menu event
    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

    
    """
    mouse events:
        .button() - specific button that trigger event
        .buttons() - state of all mouse buttons 
        .globalPos() - application-global position
        .globalX() - application-global horizontal position
        .globalY() - application-global vertical Y position
        .pos() - widget-relative position as QPoint integer
        .posF() - widget-relative position as QPointF float
    """

    """
    mouse butto identifiers:
        Qt.NoButton - no button pressed , or event not related to button press
        Qt.LeftButton - left button pressed 
        Qt.RightButton - right button pressed
        Qt.MiddleButton - middle button pressed
    """
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