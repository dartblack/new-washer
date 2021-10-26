import smbus2
from time import sleep


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = smbus2.SMBus(1)

    def read_version(self):
        paket = [0x43, 0x00, 0x00, 0x00, 0x00, 0xAC, 0x45, 0x62, 0x3B]
        self.buss.write_i2c_block_data(self.address, 0xF5, paket)
        sleep(0.2)
        print(self.buss.read_i2c_block_data(self.address, 0xFA, 11))
