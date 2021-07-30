from libs.motor import Motor

main_motor = Motor()
main_motor.init_motor("side_motor")
main_motor.set_debug(True)
main_motor.control(1, 3050, 0.0005)
