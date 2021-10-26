from smbus2 import SMBus, i2c_msg
from time import sleep


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = SMBus(1, True)

    def read_version(self):
        paket = [0xF5, 0x43, 0x00, 0x00, 0x00, 0x00, 0xAC, 0x45, 0x62, 0x3B]
        for i in paket:
            self.buss.write_byte(self.address, i)
        sleep(0.2)
        for i in range(0, 11):
            print(self.buss.read_byte(self.address))
