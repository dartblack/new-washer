from smbus2 import SMBus, i2c_msg
from time import sleep


def calculate_crc32_byte(crc, dataPtr):
    crc_uint32 = crc
    data_uint32 = dataPtr
    crc_uint32 = crc_uint32 ^ (data_uint32 << 24)
    for byte in range(0, 8):
        if (crc_uint32 & 0x80000000) == 0x80000000:
            crc_uint32 = (crc_uint32 << 1) ^ 0x04C11DB7
        else:
            crc_uint32 = (crc_uint32 << 1)
    return crc_uint32


def calculate_crc32(dataPtr):
    crc = 0xFFFFFFFF
    for i in dataPtr:
        crc = calculate_crc32_byte(crc, dataPtr[i])
    print(crc ^ 0)
    return crc ^ 0


class Tof:
    def __init__(self):
        self.address = 0x70
        self.buss = SMBus(1, True)

    def read_version(self):
        head = i2c_msg.write(self.address, [0x00])
        command = i2c_msg.write(self.address, [0x43])
        data = i2c_msg.write(self.address, [0x00, 0x00, 0x00, 0x00])
        crc = i2c_msg.write(self.address, calculate_crc32([0x00, 0x00, 0x00, 0x00]))
        response = i2c_msg.read(self.address, 0x01)
        self.buss.i2c_rdwr(head, command, data, crc, response)
        print(list(response))

    def read_distance(self):
        head = 0x00
        command = 0xE0
        paket = [0x00, 0xE0, 0x01, 0x00, 0x00, 0x00, 0x66, 0x25, 0x46, 0x93]
        data = i2c_msg.write(self.address, paket)
        read = i2c_msg.read(self.address, 12)
        self.buss.i2c_rdwr(data, read)
        read_data = list(read)
        print(read_data)
