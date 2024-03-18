import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QSizePolicy, QSpacerItem, QProgressBar
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon
import time
import argparse
from pyaligner.scripts import aligner
import pyaligner


class PyalignerGUI(QMainWindow):

    progress_signal = pyqtSignal(int)
    error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyaligner")
        
        # Set window icon
        icon_path = os.path.join(pyaligner.__path__[0], '..', 'docs', 
                                 'images', 'favicon-192x192.png')
        self.setWindowIcon(QIcon(icon_path))

        self.input_folder = None

        central_widget = QWidget()
        layout = QVBoxLayout()
        self.args = argparse.Namespace()
        self.args.input_folder = None
        self.args.language = 'spanish_mfa'
        self.args.overwrite = False
        self.args.verbose = False

        self.folder_label = QLabel("Selected Folder: None")
        # Set word wrap to True to wrap text if it exceeds the width of the label
        self.folder_label.setWordWrap(True)
        self.folder_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        layout.addWidget(self.folder_label)

        self.select_button = QPushButton("Select Folder")
        self.select_button.clicked.connect(self.select_folder)
        layout.addWidget(self.select_button)

        self.confirmation_label = QLabel("")
        layout.addWidget(self.confirmation_label)

        self.align_button = QPushButton("Align")
        self.align_button.clicked.connect(self.align)
        layout.addWidget(self.align_button)

        self.transcribe_button = QPushButton("Transcribe")
        self.transcribe_button.clicked.connect(self.transcribe)
        layout.addWidget(self.transcribe_button)

        self.auto_button = QPushButton("Transcribe + align")
        self.auto_button.clicked.connect(self.auto)
        layout.addWidget(self.auto_button)

        self.back_button = QPushButton("Go Back")
        self.back_button.clicked.connect(self.go_back)
        layout.addWidget(self.back_button)

        self.progress_label = QLabel("")
        layout.addWidget(self.progress_label)
        # self.progress_label.setWordWrap(True)
        # self.progress_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)
        self.progress_bar.hide()
        self.progress_label.hide()

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Initialize thread for aligner
        # self.aligner = AlignerThread(self.input_folder)
        # self.aligner.updateProgress.connect(self.update_progress)

        # Connect signals to update progress bar and display error messages
        self.progress_signal.connect(self.update_progress)
        self.error_signal.connect(self.display_error)


    def select_folder(self):
        options = QFileDialog.Options()
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", options=options)
        if folder_path:
            self.input_folder = folder_path
            self.folder_label.setText(f"Selected Folder: {self.input_folder}")
            # ! Get correct number of files
            num_files = len([name for name in os.listdir(self.input_folder) if os.path.isfile(os.path.join(self.input_folder, name))])
            self.confirmation_label.setText(f"Number of files: {num_files}")
            self.args.input_folder = self.input_folder

    def align(self):
        if self.input_folder:
            self.progress_label.show()
            self.progress_label.setText("")
            self.progress_bar.show()
            QApplication.processEvents()

            # Start aligner thread
            # self.aligner.folder_path = self.input_folder
            # self.aligner.start()

            aligner.align_action(self.args, 
                                        self.progress_signal, 
                                        self.error_signal)

    def auto(self):
        if self.input_folder:
            self.progress_label.show()
            self.progress_label.setText("")
            self.progress_bar.show()

            self.transcribe()
            self.align()
            # Call auto_action function from aligner.py
            # aligner.auto_action(self.args, 
            #                            self.progress_signal, 
            #                            self.error_signal)


    def transcribe(self):
        if self.input_folder:
            self.progress_label.show()
            self.progress_label.setText("")
            self.progress_bar.show()
            QApplication.processEvents()

            # Call transcribe_action function from aligner.py
            aligner.transcribe_action(self.args, 
                                             self.progress_signal, 
                                             self.error_signal)

            
    def go_back(self):
        self.input_folder = None
        self.folder_label.setText("Selected Folder: None")
        self.confirmation_label.setText("")
        # Hide progress bar and label
        self.progress_label.hide()
        self.progress_bar.hide()
        QApplication.processEvents()
        self.adjustSize()

    def update_progress(self, value):
        self.progress_bar.setValue(value)
        # if value == 100:
        #     self.progress_label.setText("Done!")

    def display_error(self, message):
        self.progress_label.setText(f"{message}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = PyalignerGUI()
    gui.show()
    sys.exit(app.exec_())
