from libs.motor import Motor
from libs.sensor import Sensor

sensor = Sensor()
sensor.init_sensors()
print("get distance info")
print(sensor.get_left_distance())
print(sensor.get_right_distance())
print(sensor.lasers_info())
