from smbus2 import SMBus, i2c_msg
from time import sleep


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = SMBus(1, True)

    def read_version(self):
        paket = [0x00, 0x43, 0x00, 0x00, 0x00, 0x00, 0x55, 0x10, 0xCD, 0x9A]
        write = i2c_msg.write(self.address, paket)
        read = i2c_msg.read(self.address, 12)
        self.buss.i2c_rdwr(write, read)
        data = list(read)
        print(data)
