import sys
import typing
from PyQt6 import QtCore
import globals
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QTabWidget,QVBoxLayout, QHBoxLayout, QLabel, QFileDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot
from GUI.presets import FilePathSelector

class ConfigArea(QWidget):
    def __init__(self, parent):
        #TODO Update settings.json here
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setStyleSheet("border-color:#000; border-width:3px;")
        self.layout.addWidget(QLabel("Config Area"))
        self.layout.addWidget(FilePathSelector(globals.CONFIG['SaveLocation']))
        self.layout.addWidget(FilePathSelector(globals.CONFIG['DataLocation']))
        self.setLayout(self.layout)