from behave import *
from libs.sensor import Sensor
from libs.motor import Motor

use_step_matcher("parse")
sensors = Sensor()
sensors.init_sensors()
left_distance = sensors.get_left_distance()
right_distance = sensors.get_right_distance()
back_distance = sensors.get_back_distances()

print(left_distance, right_distance, back_distance)

main_motor = Motor()
main_motor.init_motor("main_motor")

side_motor = Motor()
side_motor.init_motor('side_motor')

round_motor = Motor()
round_motor.init_motor('round_motor')

construct_config = main_motor.get('construct')

side_move = construct_config['X_WIDTH'] - construct_config['SIDE_START_LINE'] - 50
main_move = construct_config['Y_WIDTH'] - construct_config['START_LINE']

print(side_move, main_move)


@given("Start wash car")
def step_start(context):
    assert 15 < left_distance < 50
    assert 15 < right_distance < 50
    assert 30 < back_distance < 400


@when("I Start first position")
def step_start_positions(context):
    assert 1 == 1


@then('I move side motor dir "{direction}"')
def step_move_side_motor(context, direction):
    if direction == 1:
        move = side_move - left_distance
    else:
        move = side_move - right_distance
    side_motor.sm_control(direction, move)
    assert 1 == 1


@then('I move round motor dir "{direction}"')
def step_move_round_motor(context, direction):
    move = round_motor.motor_config['SM_PULSE']
    round_motor.control(direction, move)
    assert 1 == 1


@then('I move main motor dir "{direction}"')
def step_move_main_motor(context, direction):
    move = main_move - back_distance
    main_motor.sm_control(direction, move)
    assert 1 == 1


@then('I correct main motor dir "{direction}"')
def step_correct_main_motor(context, direction):
    diff = 0
    move = main_move - back_distance
    top = sensors.get_top_distances()
    if move > top and direction == 1:
        diff = move - top
    if direction == 2:
        diff = top - construct_config['START_LINE']
    main_motor.sm_control(direction, diff)
    assert 1 == 1
