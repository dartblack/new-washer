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
        self.port = serial.Serial("/dev/rfcomm0", baudrate=9600)

    def init_sensors(self):
        self.data = self.get("sensors")
        if self.data is None:
            raise ValueError("config is empty")
        self.trig = DigitalOutputDevice(self.data["TRIG_PIN"])
        self.left_echo = DigitalInputDevice(self.data["LEFT_ECHO"])
        self.right_echo = DigitalInputDevice(self.data["RIGHT_ECHO"])

    def get_distance(self, echo: DigitalInputDevice):
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
        data = self.get_laser_info()
        return json.loads(data)

    def get_laser_info(self):
        while True:
            rcv = self.port.readall()
            if rcv:
                return rcv
