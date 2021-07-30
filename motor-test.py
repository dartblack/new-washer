from libs.motor import Motor

motor = Motor()
motor.init_motor("main_motor")
motor.control(1, 1000)
