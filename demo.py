from libs.sensor import Sensor

sensor = Sensor()
sensor.init_sensors()
print(sensor.get_tof_distances())
