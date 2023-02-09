import time
import PySide6
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtWidgets import QApplication
from PySide6.QtGui import *
from PySide6.QtCore import *

from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication


import os
import sys
print("sys path :",os.getcwd())
# sys.path.append(os.getcwd()+'\\src\\qt_010test\\my_modbus_tcp')

class AGV:
   
    def __init__(self):
        self.ui = QUiLoader().load('ui\control.ui')
       
        
        
                
if __name__ == '__main__':
    app = QApplication([])
    agv = AGV()
    agv.ui.show()
    app.exec()
