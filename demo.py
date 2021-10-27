from libs.tof import Tof

# sensor = Sensor()
# print("get distance info")
# print(sensor.get_TFmini_data())

sensor = Tof()
sensor.read_version()
