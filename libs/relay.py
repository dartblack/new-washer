from libs.config import ConfigLoader
from gpiozero import DigitalOutputDevice


class Relay(ConfigLoader):
    def __init__(self):
        ConfigLoader.__init__(self)
        self.data = self.get("relay")
        if self.data is None:
            raise ValueError("config is empty")
        self.water = DigitalOutputDevice(self.data["WATER_PIN"])
        self.hair_dryer = []
        for k, i in self.data["HAIR_DRYER"]:
            self.hair_dryer.insert(int(k), DigitalOutputDevice(i))

    def turn_on_water(self):
        self.water.on()

    def turn_off_water(self):
        self.water.off()

    def turn_on_hair_dryer(self):
        for i in self.hair_dryer:
            i.on()

    def turn_off_hair_dryer(self):
        for i in self.hair_dryer:
            i.off()
