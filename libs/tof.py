from smbus2 import SMBus, i2c_msg
from time import sleep


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = SMBus(1)

    def read_version(self):
        paket = [0xF5, 0x43, 0x00, 0x00, 0x00, 0x00, 0xAC, 0x45, 0x62, 0x3B]
        writeMsg = i2c_msg.write(self.address, paket)
        readMsg = i2c_msg.read(self.address, 7)
        self.buss.i2c_rdwr(writeMsg, readMsg)
