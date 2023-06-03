import sys
import typing

from PyQt6 import QtCore
import globals
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QTabWidget,QVBoxLayout, QHBoxLayout, QLabel, QFileDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot

''' Code for later
import sys
from io import StringIO
class Tee:
    def __init__(self, stdout=None):
        if stdout is None:
            stdout = sys.stdout
        self.stdout = stdout
        self.buffer = StringIO()

    def write(self, data):
        self.stdout.write(data)
        self.buffer.write(data)

    def flush(self):
        self.stdout.flush()
        self.buffer.flush()
        '''


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Online Timeline'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()

class ConfigArea(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel(globals.CONFIG["DataLocation"]))
        self.layout.addWidget(FilePathSelector())
        self.setLayout(self.layout)
        
class FilePathSelector(QWidget):
    """Generic widget for displaying a file path """
    def __init__(self) -> None:
        super(QWidget,self).__init__()
        self.layout = QHBoxLayout(self)
        self.path = globals.CONFIG["DataLocation"]
        self.label = QLabel(self.path)
        self.browseButton = QPushButton()
        self.browseButton.clicked.connect(self.setPath)
        self.setStyleSheet("background-color:#33a")

        #Add child widgets
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.browseButton)
        self.setLayout(self.layout)
    def setPath(self):
        self.path = QFileDialog.getExistingDirectory(self, 'Locate data folder', self.path)
        if self.path != ('', ''):
            self.label.setText(self.path)


class DataFolderViewer():
    """Class for viewing one's unprocessed data"""
    pass
class RequestLinks(QWidget):
    """This class handles the """
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        
        self.setLayout(self.layout)

class RequestLinkButton(QPushButton):
    """This class handles the button for a single request data link"""




class MyTableWidget(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        
        self.tab3 = QWidget()
        self.tabs.resize(300,200)

        
        # Add tabs
        self.tabs.addTab(self.tab1,"Setup")
        self.tabs.addTab(self.tab2,"Process")
        self.tabs.addTab(self.tab3, "View")
        
        # Create first tab
        self.tab1.layout = QVBoxLayout()
        self.pushButton1 = QPushButton("PyQt6 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)
        
        #Second tab
        self.tab2.layout = QVBoxLayout()
        self.tab2.setLayout(self.tab2.layout)
        self.tab2.layout.addWidget(ConfigArea(self))
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = App()
    sys.exit(app.exec())

