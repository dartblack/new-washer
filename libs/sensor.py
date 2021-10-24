from libs.config import ConfigLoader
import json
import time
import serial
from gpiozero import DigitalOutputDevice
from gpiozero import DigitalInputDevice


class Sensor(ConfigLoader):
    port = None
    data = None
    lasers = []
    trig = None
    left_echo = None
    right_echo = None

    def __init__(self):
        ConfigLoader.__init__(self)

    def init_sensors(self):
        self.data = self.get("sensors")
        if self.data is None:
            raise ValueError("config is empty")
        self.trig = DigitalOutputDevice(self.data["TRIG_PIN"])
        self.left_echo = DigitalInputDevice(self.data["LEFT_ECHO"])
        self.right_echo = DigitalInputDevice(self.data["RIGHT_ECHO"])

    def get_distance(self, echo):
        startTime = 0
        endTime = 0
        self.trig.on()
        time.sleep(0.00001)
        self.trig.off()
        while echo.value == 0:
            startTime = time.time()

        while echo.value == 1:
            endTime = time.time()

        TimeElapsed = endTime - startTime
        return round(TimeElapsed * 17150, 2)

    def get_left_distance(self):
        value = 0
        for i in range(0, 10):
            temp = self.get_distance(self.left_echo)
            if temp > value:
                value = temp
        return value

    def get_right_distance(self):
        value = 0
        for i in range(0, 10):
            temp = self.get_distance(self.right_echo)
            if temp > value:
                value = temp
        return value

    def lasers_info(self):
        self.port = serial.Serial("/dev/rfcomm0", baudrate=9600)
        if not self.port.is_open:
            self.port.open()
        while True:
            data = self.port.readline()
            if data:
                self.port.close()
                return json.loads(data.decode())

    def get_TFmini_data(self):
        self.port = serial.Serial("/dev/ttyAMA0", 115200)
        if not self.port.is_open:
            self.port.open()
        distance = 0
        count = self.port.in_waiting
        if count > 8:
            recv = self.port.read(9)
            self.port.reset_input_buffer()
            if recv[0] == 'Y' and recv[1] == 'Y':  # 0x59 is 'Y'
                low = int(recv[2].encode('hex'), 16)
                high = int(recv[3].encode('hex'), 16)
                distance = low + high * 256
        return distance
