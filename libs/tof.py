import smbus2
from time import sleep


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = smbus2.SMBus(1)

    def read_version(self):
        self.buss.write_block_data(self.address, 0, [0xF5, 0x43, 0x00, 0x00, 0x00, 0x00, 0xAC, 0x45, 0x62, 0x3B])
        sleep(5)
        print(self.buss.read_block_data(self.address, 0))
