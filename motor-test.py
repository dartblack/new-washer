from libs.motor import Motor

# main_motor = Motor()
# main_motor.init_motor("main_motor")
# main_motor.set_debug(True)
# main_motor.control(1, 12000, 0.001)

side_motor = Motor()
side_motor.init_motor('side_motor')
side_motor.set_debug(True)
side_motor.control(2, 3050, 0.001)
