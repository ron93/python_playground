import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt, QAbstractListModel

from MainWindow import Ui_MainWindow

class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []
        
    def data(self, index, role):
        """
        Qt.DisplayRole - The key data to be rendered in the
        form of text. QString

        Qt.DecorationRole - The data to be rendered as a
        decoration in the form of an icon.
        QColor, QIcon or QPixmap

        Qt.EditRole - The data in a form suitable for
        editing in an editor. QString

        Qt.ToolTipRole - The data displayed in the item's
        tooltip. QString

        Qt.StatusTipRole - The data displayed in the status
        bar. QString

        Qt.WhatsThisRole - The data displayed for the item in
        "What's This?" mode. QString

        Qt.SizeHintRole - The size hint for the item that will
        be supplied to views. QSize
        """
        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text
    
    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel(todos=[(False,"my first todo")])
        self.todoView.setModel(self.model)
        # connect the button
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)


    def add(self):
        """
        add an item to the list.
        gets the text from QLineEdit .todoEdit and clears it"""
        text = self.todoEdit.text()
        # remove white space from ends of string
        text = text.strip()
        if text:
            # access  the list via model
            self.model.todos.append((False,text))
            # trigger refresh
            self.model.layoutChanged.emit()
            # empty the  input
            self.todoEdit.setText("")


    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            # indexes is a single-item list in single-select mode.
            index = indexes[0]
            # remove item  and refresh
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # clear the selection (as it is no longer valid)
            self.todoView.clearSelection()

    def complete(self):
        pass

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()