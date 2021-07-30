from libs.motor import Motor

motor = Motor()
motor.init_motor("main_motor")
motor.set_debug(True)
motor.control(2, 100000, 0.001)
