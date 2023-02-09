
from threading import Thread
import modbus_tk
import modbus_tk.modbus_tcp as modbus_tcp
import modbus_tk.defines as mdef
import time
import operator
import copy
from PySide6.QtCore import (QThread,Signal) 

class TaskTest(QThread):
    updateFrame = Signal(str)
    def __init__(self,paren=None):
        QThread.__init__(self)
        logger = modbus_tk.utils.create_logger(name='console', record_format='%(message)s')
        logger.info("running...")

    def initData(self,p1 = "",p2 = "",t=5):
        self.p1 = p1
        self.p2 = p2
        self.t = t

    def run(self):
        time.sleep(self.t)
        s = "1.前往"+self.p1+"取料盘"
        self.updateFrame.emit(s)

        time.sleep(self.t)
        s = "2.到达"+self.p1
        self.updateFrame.emit(s)

        time.sleep(self.t)
        s = "3.顶升顶起"
        self.updateFrame.emit(s)

        time.sleep(self.t)
        s = "4.顶升到位"
        self.updateFrame.emit(s)

        time.sleep(self.t)
        s = "5.前往"+self.p2+"放料盘"
        self.updateFrame.emit(s)

        time.sleep(self.t)
        s = "6.到达"+self.p2
        self.updateFrame.emit(s)

        time.sleep(self.t)
        s = "7.顶升下降"
        self.updateFrame.emit(s)

        time.sleep(self.t)
        s = "8.顶升到位"
        self.updateFrame.emit(s)

        time.sleep(self.t)
        s = "9.完成！"
        self.updateFrame.emit(s)


