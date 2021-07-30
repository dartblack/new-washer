from libs.motor import Motor

motor = Motor()
motor.init_motor("main_motor")
motor.control(1, 100000, 0.001)
