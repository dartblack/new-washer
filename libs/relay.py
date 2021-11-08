from libs.config import ConfigLoader
from gpiozero import DigitalOutputDevice
from gpiozero import LEDBoard


class Sensor(ConfigLoader):
    def __init__(self):
        ConfigLoader.__init__(self)
        self.data = self.get("relay")
        if self.data is None:
            raise ValueError("config is empty")
        self.water = DigitalOutputDevice(self.data["WATER_PIN"])
        self.hair_dryer = LEDBoard(self.data["HAIR_DRYER"])

    def turn_on_water(self):
        self.water.on()

    def turn_off_water(self):
        self.water.off()

    def turn_on_hair_dryer(self):
        self.hair_dryer.on()

    def turn_off_hair_dryer(self):
        self.hair_dryer.off()
