from libs.motor import Motor
from libs.sensor import Sensor

sensor = Sensor()
sensor.init_sensors()

main_motor = Motor()
main_motor.init_motor("main_motor")

main_motor.control_ace(1, 40000, 0.0001)
distance = sensor.get_top_distances()
print("Distance: " + str(distance))
print("PULSE/SM: " + str(40000 / distance))

main_motor.control_ace(2, 50000, 0.0001)
distance = sensor.get_top_distances()
print("Distance: " + str(distance))
