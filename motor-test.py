from libs.motor import Motor

motor = Motor()
motor.init_motor("side_motor")
motor.set_debug(True)
motor.control(1, 15000, 0.001)
