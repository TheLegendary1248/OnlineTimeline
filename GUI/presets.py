from PyQt6.QtWidgets import *
"""This folder should be for reused GUI Widgets"""

class FilePathSelector(QWidget):
    """Generic widget for displaying a file path """
    def __init__(self, path) -> None:
        super(QWidget,self).__init__()
        self.layout = QHBoxLayout(self)
        self.setFixedHeight(50)
        self.path = path
        self.label = QLabel(self.path)
        self.browseButton = QPushButton(self)
        self.browseButton.setFixedWidth(50)
        self.browseButton.clicked.connect(self.setPath)

        #Add child widgets
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.browseButton)
        self.setLayout(self.layout)
        
    def setPath(self):
        path = QFileDialog.getExistingDirectory(self, 'Locate data folder', self.path)
        if path != '': 
            self.path = path
            self.label.setText(self.path)