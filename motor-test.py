from libs.motor import Motor

main_motor = Motor()
main_motor.init_motor("round_motor")
main_motor.set_debug(True)
main_motor.control(1, 1000, 0.001)
