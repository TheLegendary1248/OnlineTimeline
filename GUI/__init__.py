import sys
import typing
from PyQt6 import QtCore
import globals
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QTabWidget,QVBoxLayout, QHBoxLayout, QLabel, QFileDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot
from GUI.presets import FilePathSelector
from GUI.config import ConfigArea

if __name__ == '__main__':
    raise BaseException("Cannot start here")

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







class DataFolderViewer():
    """Class for the main window of viewing one's unprocessed data"""

    pass


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
