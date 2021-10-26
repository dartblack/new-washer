import smbus2


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = smbus2.SMBus(1)

    def init_sensors(self):
        self.buss.write_block_data(self.address, 1, list([0xF5, 0x43, 0x00, 0x00, 0x00, 0x00, 0xAC, 0x45, 0x62, 0x3B]))

    def read_data(self):
        print(self.buss.read_byte_data(self.address, 1))
        print(self.buss.read_byte_data(self.address, 2))
        print(self.buss.read_byte_data(self.address, 3))
        print(self.buss.read_byte_data(self.address, 4))
        print(self.buss.read_byte_data(self.address, 5))
        print(self.buss.read_byte_data(self.address, 6))
        print(self.buss.read_byte_data(self.address, 7))
