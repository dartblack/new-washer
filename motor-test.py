from libs.motor import Motor

main_motor = Motor()
main_motor.init_motor("main_motor")
main_motor.set_debug(True)

side_motor = Motor()
side_motor.init_motor('side_motor')
side_motor.set_debug(True)

round_motor = Motor()
round_motor.init_motor('round_motor')
round_motor.set_debug(True)

main_motor.control(1, 12000, 0.001)
round_motor.control(2, 400, 0.005)
side_motor.control(1, 7100, 0.001)
round_motor.control(2, 400, 0.005)
main_motor.control(2, 12000, 0.001)
round_motor.control(2, 400, 0.005)
side_motor.control(2, 7100, 0.001)
round_motor.control(2, 400, 0.005)
