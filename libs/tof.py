import smbus2


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = smbus2.SMBus(1)

    def init_sensors(self):
        print(self.buss.read_byte_data(self.address, 1))
        print(self.buss.read_byte_data(self.address, 2))
        print(self.buss.read_byte_data(self.address, 3))
        print(self.buss.read_byte_data(self.address, 4))
        print(self.buss.read_byte_data(self.address, 5))
        print(self.buss.read_byte_data(self.address, 6))
        print(self.buss.read_byte_data(self.address, 7))
