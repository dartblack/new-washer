from libs.config import ConfigLoader
import json
import time
import serial
import math
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

    def get_tof_distances(self):
        mini = 0
        lidar07 = 0
        self.port = serial.Serial("/dev/rfcomm0", baudrate=9600)
        if not self.port.is_open:
            self.port.open()

        for i in range(0, 10):
            while True:
                data = self.port.readline()
                if data:
                    self.port.close()
                try:
                    data = json.loads(data.decode())
                    if data['tfmini_distance'] > mini:
                        mini = data['tfmini_distance']
                    if data['lidar07_distance'] > lidar07:
                        lidar07 = data['lidar07_distance']
                except ValueError as e:
                    break
        return {
            "hypotenuse_distance": mini,
            "distance": math.sqrt(math.pow(mini, 2) / 2),
            "motor_distance": lidar07
        }
