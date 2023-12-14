from PySide6.QtWidgets import QApplication, QWidget

import sys

# one QApplication per appication
# pass in sys.argv to allow arguments for your app
# App works without command line arguments QApplication([])

app = QApplication(sys.argv)

#create QWidget - app window
window = QWidget()
window.show() # !IMPORTANT - windows hidden by default

# start the event loop
app.exec()

