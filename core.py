from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QFileDialog,QPushButton
from PyQt6.QtCore import Qt
import sys
import time
app=QApplication([])
app.setStyle('Fusion')
app.setApplicationName('Online Timeline')
win=QWidget()
win.setBaseSize(200,200)
def SetNewTextView(label: QLabel, text: str) -> None:
    label.text
def StartUp():

    layout=QVBoxLayout()
    
    fileDialog = QFileDialog(caption="Hello?")
    fileDialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
    fileDialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    
    fileDialog.accepted.connect(lambda : print(f"$name?: {fileDialog.selectedFiles()}"))

    
    layout.addWidget(fileDialog)
    label=QLabel('Please wait a moment while the program loads', alignment=Qt.AlignmentFlag.AlignCenter)
    
    layout.addWidget(label)
    win.setLayout(layout)
    win.show()

StartUp()
sys.exit(app.exec())

