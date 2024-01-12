import sys
import os 

from datetime import datetime
from typing import Union

from PySide6 import QtCore,QtGui,QtWidgets
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, Qt

COLORS = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0',
'#f7f7f7', '#fddbc7', '#f4a582', '#d6604d', '#b2182b', '#67001f']

base_dir = os.path.dirname(__file__)

class tableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        # super(tableModel, self).__init__()
        super().__init__()

        self._data = data

    def data(self, index, role):
        # if role == Qt.BackgroundRole and index.column() ==2:
        #     return QtGui.QColor(Qt.blue)
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
        
        # if role == Qt.ForegroundRole:
        #     value = self._data[index.row()][index.column()]
        #     if (
        #         isinstance(value, int) or isinstance(value, float)
        #     ) and value < 0:
        #         return QtGui.QColor("red")
        
        # if role ==  Qt.BackgroundRole:
        #     value = self._data[index.row()][index.column()]
        #     if isinstance(value, int) or isinstance(value, float):
        #         value = int(value) # convert to integer for index.

        #         # Limit to range -5 ... +5, convert to 0..10
        #         value = max(-5, value) # values less than < -5 become -5
        #         value = min(5, value) # values > +5 become +5
        #         value = value + 5 # -5 becomes 0, +5 becomes +10

        #         return QtGui.QColor(COLORS[value])

        if role == Qt.DecorationRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return QtGui.QIcon(
                    os.path.join(base_dir, "../icon-file/icons/calendar.png")
                )
            
            if isinstance(value, bool):
                if value:
                    return QtGui.QIcon("../icon-file/icons/tick.png")
                return QtGui.QIcon("../icon-file/icons/cross.png")
            
            if isinstance(value, int) or isinstance(value, float):
                value = int(value)

                # limit to range -5 ... +5 then convert to 0..10
                value = max(-5, value) # values < -5 become -5
                value = min(5, value) # values > +5 become +5 
                value = value + 5 # -5 becomes 0, +5 becomes +10

                return QtGui.QColor(COLORS[value])
    
        
    def rowCount(self, index) :
        return len(self._data)
    
    def columnCount(self, index):
        return len(self._data[0])
    
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QtWidgets.QTableView()
        data = [
                [True, 9, 2],
                [1, 0, -1],
                [3, 5, False],
                [3, 3, 2],
                [datetime(2019, 5, 4), 8, 9],
                ]
        
        self.model = tableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
