from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

import sys

# one QApplication per appication
# pass in sys.argv(list of command line arguments passed to the app) to allow arguments for your app
# App works without command line arguments QApplication([])

# ?subclass QMainWindow to customize apps main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #  Default value fir button_is_checked
        # self.button_is_checked = True

        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        # button state
        # button.setCheckable(True)
        
        # clicked signal
        self.button.clicked.connect(self.the_button_was_clicked)
        # toggled signal
        # button.clicked.connect(self.the_button_was_toggled)
        # set state of button to the button_is_checked var - initial value
        # button.setChecked(self.button_is_checked)

        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(1024,800))
        #set the central widget of the window
        self.setCentralWidget(self.button)

    # slot that outputs clicked! when  button is pressed
    def the_button_was_clicked(self):
        self.button.setText("You already clicked me!")
        self.button.setEnabled(False)

        # change window title.
        self.setWindowTitle("My oneshot App")

    # slot that outputs the checkstate of button
    def the_button_was_toggled(self, checked):
        # update button_is_checked state if it changes
        self.button_is_checked = checked
        print("Checked?", checked)

app = QApplication(sys.argv)

#create QWidget - app window
window = MainWindow()
window.show() # !IMPORTANT - windows hidden by default

# start the event loop
app.exec()

