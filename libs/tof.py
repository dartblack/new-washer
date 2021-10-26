from smbus2 import SMBus
from time import sleep


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = SMBus(1, True)

    def read_version(self):
        paket = [0x00, 0x43, 0x00, 0x00, 0x00, 0x00, 0x55, 0x10, 0xCD, 0x9A]
        self.buss.write_i2c_block_data(self.address, 0, paket, True)
        sleep(0.1)
        print(self.buss.read_i2c_block_data(self.address, 0, 12, True))
