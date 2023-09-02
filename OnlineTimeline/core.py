'''
import sys
import typing

from PyQt6 import QtCore
import globals
from GUI import App
from PyQt6.QtWidgets import QApplication'''

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

import importlib

if __name__ == '__main__':
    import sys
    # Try core
    import plugin
    print(plugin.__doc__)
    # print(importlib.import_module('test').__doc__)

    # Then try a GUI
    """ 
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = App()
    sys.exit(app.exec())
 """
