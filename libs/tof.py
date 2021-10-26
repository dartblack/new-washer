from smbus2 import SMBus


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = SMBus(1, True)

    def read_version(self):
        paket = [0x43, 0x00, 0x00, 0x00, 0x00, 0x55, 0x10, 0xCD, 0x9A]
        self.buss.write_i2c_block_data(self.address, 0x00, paket, True)
        print(self.buss.read_i2c_block_data(self.address, 0x00, 12, True))
