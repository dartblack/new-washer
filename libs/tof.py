from smbus2 import SMBus, i2c_msg
from time import sleep


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = SMBus(1, True)

    def read_version(self):
        paket = [0xE0, 0x01, 0x00, 0x00, 0x00, 0x66, 0x25, 0x46, 0x93]
        head = i2c_msg.write(self.address, [0xF5])
        command = i2c_msg.write(self.address, [0xE0])
        data = i2c_msg.write(self.address, [0x01, 0x00, 0x00, 0x00])
        checkData = i2c_msg.write(self.address, [0x9F, 0x70, 0xE9, 0x32])
        read = i2c_msg.read(self.address, 12)
        self.buss.i2c_rdwr(head, command, data, checkData, read)
        read_data = list(read)
        print(read_data)
