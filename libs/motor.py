from libs.config import ConfigLoader
from time import sleep
from gpiozero import DigitalOutputDevice


class Motor(ConfigLoader):
    motor_config = None
    DR = None
    PL = None
    debug = False

    def __init__(self):
        ConfigLoader.__init__(self)

    def init_motor(self, name: str):
        self.motor_config = self.get(name)
        if self.motor_config is None:
            raise ValueError(name + " config is empty")
        self.DR = DigitalOutputDevice(self.motor_config["DIR_PIN"])
        self.PL = DigitalOutputDevice(self.motor_config["PL_PIN"])

    def set_debug(self, debug: bool):
        self.debug = debug

    def direction(self, dir):
        if dir == 1:
            self.DR.on()
        elif dir == 2:
            self.DR.off()

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
        if self.debug:
            print("PULSE COUNT:" + str(count))
