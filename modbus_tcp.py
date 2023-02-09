from threading import Thread
import modbus_tk
import modbus_tk.modbus_tcp as modbus_tcp
import modbus_tk.defines as mdef
import time
import operator
import copy
from PySide6.QtCore import (QThread,Signal) 

class ModTcp03_100(QThread):
    updateFrame = Signal(str)
    def __init__(self,paren=None):
        QThread.__init__(self)
        logger = modbus_tk.utils.create_logger(name='console', record_format='%(message)s')
        logger.info("running...")

    def initData(self,port=10152,backsize=10):
        server = modbus_tcp.TcpServer(port=port)
        server.start()
        self.backsize = backsize
        self.slave1 = server.add_slave(1)
            # add 2 blocks of holding registers
        self.slave1.add_block('a', mdef.HOLDING_REGISTERS, 0, self.backsize)  # address 0, length 100
            # set the values of registers at address 0
        # slave1.set_values('a', 0, 0)
        self.value2  = copy.copy(self.slave1.get_values('a',0,self.backsize))

    def run(self):
        while True:
            time.sleep(1)
            value = self.slave1.get_values('a',0,self.backsize)
            if(not operator.eq(self.value2,value)):
                # self.back(value)
                s = []
                for everyOne in value:
                   s.append(str(everyOne)) 
                self.updateFrame.emit(",".join(s))
                self.value2 = copy.copy(value)    

    def set_value(self,adress,value):
        self.slave1.set_values('a',adress,value)
def backdata(value):
    print(value)

if __name__ == "__main__":
    ModTcp03_100(port=11520,back=backdata,backsize=20).start()