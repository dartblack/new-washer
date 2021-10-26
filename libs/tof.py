import smbus2
from time import sleep


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = smbus2.SMBus(1)

    def read_version(self, ):
        readVersionPacket = list()
        readVersionPacket.insert(0, 0x00)
        readVersionPacket.insert(1, 0x43)
        readVersionPacket.insert(2, [0x00, 0x00, 0x00, 0x00])
        readVersionPacket.insert(3, [0xAC, 0x45, 0x62, 0x3B])
        self.buss.write_block_data(self.address, 0, readVersionPacket)
        sleep(0.2)
        print(self.buss.read_block_data(self.address, 0))
        list().insert(0, 0x00)
