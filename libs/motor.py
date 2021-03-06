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
    active_sensor = None

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
            if self.safe_sensors is not None:
                self.active_sensor = self.safe_sensors["1"]
            self.DR.on()
            if self.DR2 is not None:
                self.DR2.off()
        elif direction == 2:
            if self.safe_sensors is not None:
                self.active_sensor = self.safe_sensors["2"]
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
            if self.active_sensor is not None and self.active_sensor.value == 1:
                break
            self.move(delay)
            count = count + 1
        if self.debug:
            print("PULSE COUNT:" + str(count))

    def control_ace(self, direction, duration=10, delay=None):
        if delay is None:
            delay = self.motor_config["PULSE_DELAY"]
        count = 0
        self.direction(direction)

        if duration < self.motor_config["ACE_COUNT"]:
            self.motor_config["ACE_COUNT"] = duration

        start_delay = 0.001
        coef = start_delay / self.motor_config["ACE_COUNT"]
        for i in range(self.motor_config["ACE_COUNT"]):
            if self.active_sensor is not None and self.active_sensor.value == 1:
                break
            self.move(start_delay)
            start_delay = start_delay - coef
            count = count + 1

        for i in range(round(duration) - self.motor_config["ACE_COUNT"] - self.motor_config["ACE_COUNT"]):
            if self.active_sensor is not None and self.active_sensor.value == 1:
                break
            self.move(delay)
            count = count + 1

        start_delay = delay
        for i in range(duration - count):
            if self.active_sensor is not None and self.active_sensor.value == 1:
                break
            self.move(start_delay)
            start_delay = start_delay + coef
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
