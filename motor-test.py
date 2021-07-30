from libs.motor import Motor

main_motor = Motor()
main_motor.init_motor("main_motor")
main_motor.set_debug(True)
main_motor.control(2, 1000, 0.0005)
