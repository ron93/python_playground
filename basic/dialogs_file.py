import sys
import os

from  PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMessageBox

)
# file filter
FILE_FILTERS = [
        "Portable Network Graphics File (*.png)",
        "Text files (*.txt)",
        "Comma Separated Values (*.csv)",
        "PDF (*.pdf)",
        "All files (*.*)",
        ]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        button1  = QPushButton("Open file")
        button1.clicked.connect(self.get_filename)
        layout.addWidget(button1)

        button2 = QPushButton("Open files")
        button2.clicked.connect(self.get_filenames)
        layout.addWidget(button2)

        button3 = QPushButton("Save file")
        button3.clicked.connect(self.get_save_filename)
        layout.addWidget(button3)

        button4 = QPushButton("Select Folder")
        button4.clicked.connect(self.get_folder)
        layout.addWidget(button4)


        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_filename(self):
        caption = ""
        initial_dir = ""
        initial_filter = FILE_FILTERS[2] #filter from FILE_FILTER list
        filters = ';;'.join(FILE_FILTERS)
        print("Filter are:", filters)
        print("Initial filter are:", initial_filter)

        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            caption=caption,
            #TODO fix directory error : AttributeError: PySide6.QtWidgets.QFileDialog.getOpenFileName(): unsupported keyword 'directory'
            # directory=initial_dir,
            filter=filters,
            # TODO fix initial value error :AttributeError: PySide6.QtWidgets.QFileDialog.getOpenFileName(): unsupported keyword 'initialFilter'
            # initialFilter = initial_filter
            )
        
        print("Result:", filename, selected_filter)
        # TODO file content read errors on PDF :UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe2 in position 10: invalid continuation byte
        if filename:
            with open(filename, "r")  as f:
                file_contents = f.read()
                print(file_contents)

    # Open multiple files
    def get_filenames(self):
        caption = "" 
        initial_dir = ""
        initial_filter =  FILE_FILTERS[1] # from list
        filters = ";;".join(FILE_FILTERS)
        print("Filters are: ", filters)
        print("Initial filter: ", initial_filter)

        filenames, selected_filter = QFileDialog.getOpenFileNames(
            self,
            caption=caption,
            # directory = initial_dir,
            filter=filters,
            # initialFilter=initial_filter
        )
        print("Result:", filenames, selected_filter)

        if filenames:
            for filename  in filenames:
                with open(filename, "r") as f:
                    file_contents = f.read()
                    print(file_contents)
    
    def get_save_filename(self):
        caption = ""
        initial_dir = ""
        initial_filter = FILE_FILTERS[3]
        filters = ";;".join(FILE_FILTERS)

        print("Filters are:", filters)
        print("Initial filters:", initial_filter)

        filename, selected_filter = QFileDialog.getSaveFileName(
            self,
            caption=caption,
            # directory=initial_dir,
            filter=filters,
            # initialFilter=initial_filter,
        )

        print("Result:", filename, selected_filter)
        
        # check file exists
        if filename:
            if os.path.exists(filename):
                write_confirned = QMessageBox(
                    self,
                    "Overwrite file?",
                    f"The file  {filename} exists. Are you sure you want to overwrite it?"
                )
            else:
                # file exists. Always conformed
                write_confirned = True
                if  write_confirned:
                    with open(filename, "w") as f:
                        file_content = "YOUR FILE CONTENT"
                        f.write(file_content)

    def get_folder(self):
        pass

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()