import smbus2


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = smbus2.SMBus(1)

    def init_sensors(self):
        byte = self.buss.read_byte_data(self.address, 1)
        print(byte)
