from libs.config import ConfigLoader
from time import sleep
from gpiozero import DigitalOutputDevice


class Motor(ConfigLoader):
    motor_config = None
    DR = None
    PL = None
    DR2 = None
    debug = False

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
        sleep(delay)
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
        self.PL.off()
        if self.debug:
            print("PULSE COUNT:" + str(count))
