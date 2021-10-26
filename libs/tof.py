from smbus2 import SMBus, i2c_msg
from time import sleep


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = SMBus(1, True)

    def read_version(self):
        paket = [0x43, 0x00, 0x00, 0x00, 0x00, 0xAC, 0x45, 0x62, 0x3B]
        self.buss.write_i2c_block_data(self.address, 0xF5, paket, True)
        for i in paket:
            self.buss.write_byte_data(self.address, 0xF5, i)
        sleep(0.2)
        for i in range(0, 20):
            print(self.buss.read_block_data(self.address, 0xFA))
