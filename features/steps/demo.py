from behave import *
from libs.sensor import Sensor
from libs.motor import Motor

use_step_matcher("parse")
sensors = Sensor()
sensors.init_sensors()
left_distance = sensors.get_left_distance()
right_distance = sensors.get_right_distance()

main_motor = Motor()
main_motor.init_motor("main_motor")

side_motor = Motor()
side_motor.init_motor('side_motor')

round_motor = Motor()
round_motor.init_motor('round_motor')


@given("Start wash car")
def step_start(context):
    assert 15 < left_distance < 50
    assert 15 < right_distance < 50


@when("I Start first position")
def step_start_positions(context):
    assert 1 == 1


@then('I move side motor dir "{dir}"')
def step_move_side_motor(context, dir):
    if dir == 1:
        move = 300 - 70 - left_distance
    else:
        move = 300 - 70 - right_distance
    side_motor.sm_control(dir, move)
