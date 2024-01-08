from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt, QSize
 
import sys

darkPalette = QPalette()
darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
darkPalette.setColor(QPalette.WindowText, Qt.white)
darkPalette.setColor(
    QPalette.Disabled, QPalette.WindowText, QColor(127,127,  127)
)
darkPalette.setColor(QPalette.Base, QColor(42, 42, 42))
darkPalette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
darkPalette.setColor(QPalette.ToolTipText, Qt.white)
darkPalette.setColor(QPalette.Text, Qt.white)
darkPalette.setColor(
    QPalette.Disabled, QPalette.Text, QColor(127, 127, 127)
)
darkPalette.setColor(QPalette.BrightText, Qt.red)
darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
darkPalette.setColor(
    QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80)
)
darkPalette.setColor(QPalette.HighlightedText, Qt.white)
darkPalette.setColor(
    QPalette.Disabled,
    QPalette.HighlightedText,
    QColor(127, 127, 127)
)
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         #  Default value fir button_is_checked
#         # self.button_is_checked = True

#         self.setWindowTitle("My App")
#         self.button = QPushButton("Press Me!")
#         # button state
#         # button.setCheckable(True)
        
#         # clicked signal
#         self.button.clicked.connect(self.the_button_was_clicked)
#         # toggled signal
#         # button.clicked.connect(self.the_button_was_toggled)
#         # set state of button to the button_is_checked var - initial value
#         # button.setChecked(self.button_is_checked)

#         self.setMinimumSize(QSize(400, 300))
#         self.setMaximumSize(QSize(1024,800))
#         #set the central widget of the window
#         self.setCentralWidget(self.button)

#     # slot that outputs clicked! when  button is pressed
#     def the_button_was_clicked(self):
#         self.button.setText("You already clicked me!")
#         self.button.setEnabled(False)

#         # change window title.
#         self.setWindowTitle("My oneshot App")

#     # slot that outputs the checkstate of button
#     def the_button_was_toggled(self, checked):
#         # update button_is_checked state if it changes
#         self.button_is_checked = checked
#         print("Checked?", checked)
app = QApplication(sys.argv)
app.setPalette(darkPalette)

w = QMainWindow()
w.show()
app.exec()