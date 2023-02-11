from threading import Thread
import modbus_tk
import modbus_tk.modbus_tcp as modbus_tcp
import modbus_tk.defines as mdef
import time
import operator
import copy
from PySide6.QtCore import (QThread,Signal) 


class ModTcp_master(QThread):
    updateFrame = Signal(object)
    isOpen = None
    def __init__(self,paren=None):
        QThread.__init__(self)
        logger = modbus_tk.utils.create_logger(name='console', record_format='%(message)s')
        logger.info("running...")
        self.isOpen = True
    def initData(self,ip='127.0.0.1',port=10152):
        print(ip)
        print(port)
        self.master =  modbus_tcp.TcpMaster(host=ip,port=port,timeout_in_sec=3)
    def threadClose(self):
        self.isOpen = False


    def run(self):
        while self.isOpen:
            time.sleep(2)
            print("...")
            print(self.master)
            s = []
            ls = []
            # (0,0,0)
            # 计算（0，1）、模式（2）
            value = self.master.execute(slave=1, function_code=mdef.READ_HOLDING_REGISTERS, starting_address=2183, quantity_of_x=3)
            ls.append(value[0]*65536+value[1])
            ls.append(value[2])
            
            # 轴数（0）
            value = self.master.execute(slave=1, function_code=mdef.READ_HOLDING_REGISTERS, starting_address=2267, quantity_of_x=1)
            ls.append(value[0])
            # 报警号
            value = self.master.execute(slave=1, function_code=mdef.READ_HOLDING_REGISTERS, starting_address=2396, quantity_of_x=1)
            ls.append(value[0]) 
            # 移动状态
            value = self.master.execute(slave=1, function_code=mdef.READ_HOLDING_REGISTERS, starting_address=2470, quantity_of_x=1)
            ls.append(value[0])
             # 全局速度:20200
            value = self.master.execute(slave=1, function_code=mdef.READ_HOLDING_REGISTERS, starting_address=20200, quantity_of_x=1)
            ls.append(value[0])
            s.append(ls)
            # 1轴（0，1），2轴（2，3），3轴（4，5），4轴（6，7），5轴（8，9），6轴（10，11）
            value = self.master.execute(slave=1, function_code=mdef.READ_HOLDING_REGISTERS, starting_address=2268, quantity_of_x=12)
            s.append(self.value_handle(value)) 
            # 世界坐标：X轴（0, 1），Y轴（2, 3），Z轴（4, 5），U轴（6, 7），V轴（8, 9），W轴（10，11）
            value = self.master.execute(slave=1, function_code=mdef.READ_HOLDING_REGISTERS, starting_address=2332, quantity_of_x=12)
            s.append(self.value_handle(value))
            # 扭矩：1轴（0），2轴（2），3轴（3），4轴（4），5轴（5），6轴（6）
            value = self.master.execute(slave=1, function_code=mdef.READ_HOLDING_REGISTERS, starting_address=2406, quantity_of_x=6)
            s.append(list(value))
            
            self.updateFrame.emit(s)
        
    def value_handle(self,value):
        print(value)
        newValue = []
        for i in range(int(len(value) / 2)):
            if value[2*i] > 32767:
                print(5536-value[2*i])
                newValue.append(value[2*i+1]-(65536 * (65536-value[2*i])))
            else:
                newValue.append(value[2*i]*65536+value[2*i+1])
        print(newValue)
        return newValue    

    def set_value(self,type,adress,value):
        if type == 0:
            self.master.execute(slave=1,function_code=mdef.WRITE_SINGLE_REGISTER,starting_address=5,output_value=1)
            self.master.execute(slave=1,function_code=mdef.WRITE_SINGLE_REGISTER,starting_address=6,output_value=1)
            self.master.execute(slave=1,function_code=mdef.WRITE_SINGLE_REGISTER,starting_address=9,output_value=1)
        elif type == 1:
            self.master.execute(slave=1,function_code=mdef.WRITE_SINGLE_REGISTER,starting_address=6,output_value=11)
            self.master.execute(slave=1,function_code=mdef.WRITE_SINGLE_REGISTER,starting_address=9,output_value=1)
def backdata(value):
    print(value)

if __name__ == "__main__":
    socke = ModTcp_master()
    socke.initData(ip='192.168.3.70',port=10180)
    socke.updateFrame.connect(backdata)
    socke.start()