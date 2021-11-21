from libs.config import ConfigLoader
from time import sleep
from gpiozero import DigitalOutputDevice, DigitalInputDevice


class Motor(ConfigLoader):
    motor_config = None
    DR = None
    PL = None
    DR2 = None
    debug = False
    safe_sensors = None

    def __init__(self):
        ConfigLoader.__init__(self)

    def init_motor(self, name):
        self.motor_config = self.get(name)
        if self.motor_config is None:
            raise ValueError(name + " config is empty")
        self.DR = DigitalOutputDevice(self.motor_config["DIR_PIN"])
        self.PL = DigitalOutputDevice(self.motor_config["PL_PIN"])
        if "DIR_PIN2" in self.motor_config:
            self.DR2 = DigitalOutputDevice(self.motor_config["DIR_PIN2"])
        if "SAFE_SENSOR_PINS" in self.motor_config:
            self.safe_sensors = {
                "1": DigitalInputDevice(self.motor_config["SAFE_SENSOR_PINS"]["1"]),
                "2": DigitalInputDevice(self.motor_config["SAFE_SENSOR_PINS"]["2"])
            }

    def set_debug(self, debug):
        self.debug = debug

    def direction(self, direction):
        if direction == 1:
            self.DR.on()
            if self.DR2 is not None:
                self.DR2.off()
        elif direction == 2:
            self.DR.off()
            if self.DR2 is not None:
                self.DR2.on()

    def move(self, delay=None):
        if delay is None:
            delay = self.motor_config["PULSE_DELAY"]

        self.PL.on()
        self.PL.off()
        sleep(delay)

    def control(self, direction, duration=10, delay=None):
        if delay is None:
            delay = self.motor_config["PULSE_DELAY"]
        count = 0
        self.direction(direction)
        for i in range(round(duration)):
            self.move(delay)
            count = count + 1
        if self.debug:
            print("PULSE COUNT:" + str(count))

    def control_ace(self, direction, duration=10, delay=None):
        if delay is None:
            delay = self.motor_config["PULSE_DELAY"]
        count = 0
        self.direction(direction)
        start_delay = 0.001
        for i in range(2000):
            self.move(start_delay)
            start_delay = start_delay + delay
            count = count + 1

        for i in range(round(duration) - 2000):
            self.move(delay)
            count = count + 1
        if self.debug:
            print("PULSE COUNT:" + str(count))

    def sm_control(self, direction, sm=1, ace=False, delay=None):
        duration = sm * self.motor_config["SM_PULSE"]
        if self.debug:
            print(direction, sm, duration)
        if ace:
            self.control_ace(direction, duration, delay)
        else:
            self.control(direction, duration, delay)
