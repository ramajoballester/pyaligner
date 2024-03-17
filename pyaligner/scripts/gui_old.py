import sys
import os
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QSizePolicy, QSpacerItem, QProgressBar

class PyalignerGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyaligner")

        self.folder_path = None

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.folder_label = QLabel("Selected Folder: None")
        # Set word wrap to True to wrap text if it exceeds the width of the label
        self.folder_label.setWordWrap(True)
        # Set maximum width to 300 pixels
        # self.folder_label.setMaximumWidth(500)
        # Allow to stretch the window to fit the label
        # self.folder_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # Allow to strech window only vertically
        self.folder_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        layout.addWidget(self.folder_label)
        # spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        # layout.addItem(spacer_bottom)

        self.select_button = QPushButton("Select Folder")
        self.select_button.clicked.connect(self.select_folder)
        layout.addWidget(self.select_button)

        self.confirmation_label = QLabel("")
        layout.addWidget(self.confirmation_label)

        self.align_button = QPushButton("Align")
        self.align_button.clicked.connect(self.align)
        layout.addWidget(self.align_button)

        self.auto_button = QPushButton("Auto")
        self.auto_button.clicked.connect(self.auto)
        layout.addWidget(self.auto_button)

        # self.progress_bar = QProgressBar()

        self.back_button = QPushButton("Go Back")
        self.back_button.clicked.connect(self.go_back)
        layout.addWidget(self.back_button)

        self.progress_label = QLabel("")
        layout.addWidget(self.progress_label)
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)
        self.progress_bar.hide()
        self.progress_label.hide()

        # Add vertical spacer item with adjustable alpha parameter
        # spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        # layout.addItem(spacer)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def select_folder(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog  # Use Qt dialog implementation
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", options=options)
        if folder_path:
            self.folder_path = folder_path
            self.folder_label.setText(f"Selected Folder: {self.folder_path}")
            num_files = len([name for name in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, name))])
            self.confirmation_label.setText(f"Number of files: {num_files}")

    # def align(self):
    #     if self.folder_path:
    #         print(f"Aligning files from {self.folder_path}...")

    def align(self):

        if self.folder_path:
            self.progress_label.show()
            self.progress_label.setText("Progressing")
            self.progress_bar.show()
            print(f"Aligning files from {self.folder_path}...")
            self.progress_label.setText("Progressing")
            self.progress_bar.setMaximum(15)  # Set maximum value for the progress bar
            self.progress_bar.setValue(0)  # Reset progress bar value
            for i in range(1, 16):
                time.sleep(0.1)  # Simulate processing time
                self.progress_bar.setValue(i)  # Update progress bar value
            self.progress_label.setText("Done!")

            # Start another progress bar for the second loop
            self.progress_label.setText("Second loop")
            self.progress_bar.setMaximum(10)  # Set maximum value for the progress bar
            self.progress_bar.setValue(0)  # Reset progress bar value
            for i in range(1, 11):
                time.sleep(0.1)  # Simulate processing time
                self.progress_bar.setValue(i)  # Update progress bar value
            self.progress_label.setText("Done 2!")

    def auto(self):
        if self.folder_path:
            print(f"Automating files from {self.folder_path}...")

    def go_back(self):
        self.folder_path = None
        self.folder_label.setText("Selected Folder: None")
        self.confirmation_label.setText("")
        # Hide progress bar and label
        self.progress_label.hide()
        self.progress_bar.hide()
        QApplication.processEvents()
        self.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = PyalignerGUI()
    gui.show()
    sys.exit(app.exec_())
