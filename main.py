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
from modbus_tcp import ModTcp_master
class AGV:
   
    def __init__(self):
        self.ui = QUiLoader().load('ui\control.ui')
        self.ui.Cont_PB.clicked.connect(lambda:self.btnsHandler(self.ui.Cont_PB))

    def btnsHandler(self,b):
        print("butenName"+b.text())
        self.socke = ModTcp_master(self)
        self.socke.initData(ip="192.168.3.70",port=10180)
        self.socke.updateFrame.connect(self.backData)
        self.socke.start()
    
    @Slot(object)   
    def backData(self,value):
        print(value)
        self.robotInfoUpdata(value[0])
        self.axleUpdata(value[1])
        self.wordUpdata(value[2])
        self.torsionUpdata(value[3])
        
        # value = s.split(',')
        # for i in range(len(value)):
        #     print(value[i])
    
    def robotInfoUpdata(self,vlaue):
        self.ui.LineEdit_44.setText(str(vlaue[0]))
        self.ui.LineEdit_45.setText(str(vlaue[1]))
        self.ui.LineEdit_46.setText(str(vlaue[2]))
        self.ui.LineEdit_47.setText(str(vlaue[3]))
        self.ui.LineEdit_48.setText(str(vlaue[4]))
        self.ui.LineEdit_49.setText(str(vlaue[5]))
    


    def axleUpdata(self,vlaue):
        self.ui.LineEdit_20.setText(str(vlaue[0]))
        self.ui.LineEdit_21.setText(str(vlaue[1]))
        self.ui.LineEdit_22.setText(str(vlaue[2]))
        self.ui.LineEdit_23.setText(str(vlaue[3]))
        self.ui.LineEdit_24.setText(str(vlaue[4]))
        self.ui.LineEdit_25.setText(str(vlaue[5]))
            
    def wordUpdata(self,vlaue):
        self.ui.LineEdit_26.setText(str(vlaue[0]))
        self.ui.LineEdit_27.setText(str(vlaue[1]))
        self.ui.LineEdit_28.setText(str(vlaue[2]))
        self.ui.LineEdit_29.setText(str(vlaue[3]))
        self.ui.LineEdit_30.setText(str(vlaue[4]))
        self.ui.LineEdit_31.setText(str(vlaue[5]))

    def torsionUpdata(self,vlaue):
        self.ui.LineEdit_32.setText(str(vlaue[0]))
        self.ui.LineEdit_33.setText(str(vlaue[1]))
        self.ui.LineEdit_34.setText(str(vlaue[2]))
        self.ui.LineEdit_35.setText(str(vlaue[3]))
        self.ui.LineEdit_36.setText(str(vlaue[4]))
        self.ui.LineEdit_37.setText(str(vlaue[5]))
            

    def closeEvent(self,event):
        self.socke.stop()
        event.accept()       


if __name__ == '__main__':
    app = QApplication([])
    agv = AGV()
    agv.ui.show()
    app.exec()
