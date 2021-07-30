from libs.motor import Motor

motor = Motor()
motor.init_motor("side_motor")
motor.set_debug(True)
motor.control(2, 10000, 0.001)
