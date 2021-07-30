from libs.motor import Motor

main_motor = Motor()
main_motor.init_motor("side_motor")
main_motor.set_debug(True)
main_motor.control(2, 7100, 0.0005)

main_motor = Motor()
main_motor.init_motor("main_motor")
main_motor.set_debug(True)
main_motor.control(2, 10000, 0.0005)
