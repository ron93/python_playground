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

        """# set data  header manually :
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Album (ID)")
        self.model.setHeaderData(3, Qt.Horizontal, "Media Type (ID)")
        self.model.setHeaderData(4,Qt.Horizontal, "Genre (ID)")
        self.model.setHeaderData(5, Qt.Horizontal, "Composer")
        """
        # name for  titles
        column_titles = {
            "Name": "Name",
            "AlbumId": "Album (ID)",
            "MediaTypeId": "Media Type (ID)",
            # "GenreId":"Genre (ID)",
            # "Composer": "Composer",
        }

        columns_to_remove = ["Composer","GenreID"]
        # remove columns in list -> columns_to_remove
        for cn in columns_to_remove:
            idx = self.model.fieldIndex(cn)
            self.model.removeColumns(idx, 1)

        # title look-up and setting header
        for n, t in column_titles.items():
            idx = self.model.fieldIndex(n)
            self.model.setHeaderData(idx, Qt.Horizontal,  t)

        

        self.model.select()

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
