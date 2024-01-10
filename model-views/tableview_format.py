import sys
from datetime import datetime
from typing import Union

from PySide6 import QtCore,QtGui,QtWidgets
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, Qt

class tableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        # super(tableModel, self).__init__()
        super().__init__()

        self._data = data

    def data(self, index, role):
        if role == Qt.BackgroundRole and index.column() ==2:
            return QtGui.QColor(Qt.blue)
        if role == Qt.DisplayRole:
            # get raw value
            value = self._data[index.row()][index.column()]

            # perform per-type checks and render accordingly.
            if isinstance(value, datetime):
                # render time to yyy-md-dd
                return value.strftime("%Y-%m-%d")
            
            if isinstance(value, float):
                # render float to dp
                return "%.2f" % value
            
            if  isinstance(value, str):
                # render strings with quotes
                return '"%s' % value
            
            # default (anything not captured above: eg int)
            return value
        
        if role == Qt.TextAlignmentRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, int) or isinstance(value, float):
                # align  right, vertical middle.
                return Qt.AlignVCenter | Qt.AlignRight
        
        if role == Qt.ForegroundRole:
            value = self._data[index.row()][index.column()]
            if (
                isinstance(value, int) or isinstance(value, float)
            ) and value < 0:
                return QtGui.QColor("red")
    
        
    def rowCount(self, index) :
        return len(self._data)
    
    def columnCount(self, index):
        return len(self._data[0])
    
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QtWidgets.QTableView()
        data = [
                [4, 9, 2],
                [1, -1, 'hello'],
                [3.023, 5, -5],
                [3, 3, datetime(2017,10,1)],
                [7.555, 8, 9],
                ]
        self.model = tableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
