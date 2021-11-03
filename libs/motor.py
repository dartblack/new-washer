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

    def direction(self, dir):
        if dir == 1:
            self.DR.on()
            if self.DR2 is not None:
                self.DR2.off()
        elif dir == 2:
            self.DR.off()
            if self.DR2 is not None:
                self.DR2.on()

    def move(self, delay=None):
        if delay is None:
            delay = self.motor_config["PULSE_DELAY"]

        self.PL.on()
        self.PL.off()
        sleep(delay)

    def control(self, dir, duration=10, delay=None):
        if delay is None:
            delay = self.motor_config["PULSE_DELAY"]
        count = 0
        self.direction(dir)
        for i in range(duration):
            self.move(delay)
            count = count + 1
        if self.debug:
            print("PULSE COUNT:" + str(count))

    def sm_control(self, dir, sm=1, delay=None):
        duration = sm * self.motor_config["SM_PULSE"]
        self.control(dir, duration, delay)
