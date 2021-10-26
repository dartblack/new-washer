import smbus2
from time import sleep


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = smbus2.SMBus(1)

    def read_version(self):
        paket = [0x00, 0x43, 0x00, 0x00, 0x00, 0x00, 0x55, 0x10, 0xCD, 0x9A]
        for byte in paket:
            self.buss.write_byte(self.address, byte)
        sleep(0.2)
        print(self.buss.read_byte(self.address))
