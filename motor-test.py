from libs.motor import Motor
from time import sleep
dir = 1
speed = 0.005
main_motor = Motor()
main_motor.init_motor("main_motor")
main_motor.set_debug(False)

side_motor = Motor()
side_motor.init_motor('side_motor')
side_motor.set_debug(False)

round_motor = Motor()
round_motor.init_motor('round_motor')
round_motor.set_debug(False)
#round_motor.control(1, 400, 0.002)
side_motor.control(1, 100, 0.001)
exit(0)

#for i in range(10):
#    main_motor.control(1 + (i%2), 200000, 0.001)
main_motor.control(1, 10000, 0.001)
exit()
v = 0.002
for x in range(50):
    v -= 0.0001
    if v <= speed:
       v = speed
    main_motor.control(dir, 100+2*x, v)
exit(0)
#side_motor.control(1, 5000, 0.0002) 
main_motor.control(1, 40000, 0.001)
exit(0)
round_motor.control(2, 400, 0.002)
side_motor.control(1, 7100, 0.0005)
round_motor.control(2, 400, 0.002)
main_motor.control(2, 12000, 0.0003)
round_motor.control(2, 400, 0.002)
side_motor.control(2, 7100, 0.0005)
round_motor.control(2, 400, 0.002)
