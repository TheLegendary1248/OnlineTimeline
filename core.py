from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QFileDialog
from PyQt6.QtCore import Qt
import sys
import time
app=QApplication([])
app.setStyle('Fusion')
app.setApplicationName('Online Timeline')
win=QWidget()
win.setBaseSize(200,200)
def SetNewTextView()
def StartUp():

    layout=QVBoxLayout()
    label=QLabel('Please wait a moment while the program loads', alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(label)

    win.setLayout(layout)
    win.show()

StartUp()
sys.exit(app.exec())

