import requests
import statistics
import math

from libs.config import ConfigLoader
import time
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

    def get_back_distances(self):
        response = requests.get('http://' + self.data['DISTANCE_SENSOR_IP'] + '/distance', {
            'count': 30,
            'delay': 50
        })
        if response.status_code != 200:
            return 0
        data = response.json()
        d = statistics.mode(data['distance']) / 10
        dis = round(math.sqrt(math.pow(d, 2) / 2))
        return dis

    def get_top_distances(self):
        response = requests.get('http://' + self.data['TOP_SENSOR_IP'] + '/distance', {
            'count': 30,
            'delay': 50
        })
        if response.status_code != 200:
            return 0
        data = response.json()
        d = statistics.mode(data['distance'])
        return d
