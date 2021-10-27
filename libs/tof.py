from smbus2 import SMBus, i2c_msg
import time
import random

I2CBUS = 1

ADDRESS = 0x70

SIM_MIN = 90.17  # centimeters
SIM_MAX = 92.71  # centimeters


class TFMiniPlus:

    def __init__(self, i2c_address=ADDRESS, bus=None, simulate=False, sim_min=SIM_MIN, sim_max=SIM_MAX):
        self.addr = i2c_address
        self.sim_min = sim_min
        self.sim_max = sim_max
        self.simulate = simulate
        if not simulate:
            if bus is None:
                self.bus = SMBus(I2CBUS)  # Initialize I2C
            else:
                self.bus = bus

    def write_cmd(self, cmd):
        self.bus.write_byte(self.addr, cmd)
        time.sleep(0.0001)

    def write_cmd_arg(self, cmd, data):
        self.bus.write_byte_data(self.addr, cmd, data)
        time.sleep(0.0001)

    def write_block_data(self, cmd, data):
        self.bus.write_i2c_block_data(self.addr, cmd, data)
        time.sleep(0.0001)

    def read(self):
        return self.bus.read_byte(self.addr)

    def read_data(self, cmd):
        return self.bus.read_byte_data(self.addr, cmd)

    def read_block_data(self, cmd):
        return self.bus.read_i2c_block_data(self.addr, cmd, 0)

    def get_reading_version(self):
        ts1 = time.time()
        if not self.simulate:
            block = list()
            COMMAND = [0x43, 0x00, 0x00, 0x00, 0x00]
            self.write_block_data(0x00, COMMAND)
            time.sleep(0.01)
            for a_byte in range(0, 9):
                byte = self.read()
                block.insert(a_byte, byte)
            print(block)

            if block[0] == 0x59 and block[1] == 0x59:
                distance = block[2] + block[3] * 256
                strength = block[4] + block[5] * 256
                temperature = block[6] + block[7] * 256
                temperature = (temperature / 8) - 256

            if block[0] == "Y" and block[1] == "Y":
                distL = int(block[2].encode("hex"), 16)
                distH = int(block[3].encode("hex"), 16)
                stL = int(block[4].encode("hex"), 16)
                stH = int(block[5].encode("hex"), 16)
                distance = distL + distH * 256
                strength = stL + stH * 256
                tempL = int(block[6].encode("hex"), 16)
                tempH = int(block[7].encode("hex"), 16)
                temperature = tempL + tempH * 256
                temperature = (temperature / 8) - 256
        else:
            distance = random.uniform(self.sim_min, self.sim_max)
            strength = 300.0
            temperature = 80.0
        # end if

        # gets the second timestamp and the difference
        ts2 = time.time()
        ttr = ts2 - ts1
        data_block = {
            "distance": distance,
            "strength": strength,
            "temperature": temperature,
            "ttr": ttr
        }
        return data_block
