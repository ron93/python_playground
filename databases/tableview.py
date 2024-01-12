import os
import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication,  QMainWindow, QTableView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel

from db import db


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)
        self.model.setTable("Track")
        # index to sort by
        idx = self.model.fieldIndex("Milliseconds")
        # sort column index and Qt.AscendingOrder or Qt.DescendingOrder
        self.model.setSort(idx, Qt.DescendingOrder)
        self.model.select()
        """
        editing strategy:
            QSqlTableModel.OnFieldChange
            QSqlTableModel.OnRowChange
            QSqlTableModel.OnManualSubmit
        """
        self.model.setEditStrategy(QSqlTableModel.OnRowChange)

        self.setMinimumSize(QSize(1024, 600))

        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
