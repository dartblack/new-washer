from behave import *
from time import sleep
from libs.sensor import Sensor
from libs.motor import Motor
from libs.relay import Relay

use_step_matcher("parse")
relay = Relay()
sensors = Sensor()
sensors.init_sensors()
left_distance = 30
right_distance = 30
back_distance = 200

print(left_distance, right_distance, back_distance)

main_motor = Motor()
main_motor.init_motor("main_motor")
main_motor.set_debug(True)

side_motor = Motor()
side_motor.init_motor('side_motor')
side_motor.set_debug(True)

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
    direction = int(direction)
    move = 100000
    side_motor.control(direction, move)
    assert 1 == 1


@then('I move round motor dir "{direction}"')
def step_move_round_motor(context, direction):
    direction = int(direction)
    round_motor.direction(direction)
    for i in range(0, 300):
        round_motor.move(round_motor.motor_config["PULSE_DELAY"])
    move = round_motor.motor_config['SM_PULSE'] - 300
    round_motor.control(direction, move)
    assert 1 == 1


@then('I move main motor dir "{direction}"')
def step_move_main_motor(context, direction):
    direction = int(direction)
    move = main_move - back_distance
    main_motor.sm_control(direction, move, True)
    assert 1 == 1


@then('I correct main motor dir "{direction}"')
def step_correct_main_motor(context, direction):
    direction = int(direction)
    diff = 0
    move = main_move - back_distance
    top = sensors.get_top_distances() - 25
    if move > top + 20 and direction == 1:
        diff = move - top
    if direction == 2:
        diff = top
    main_motor.sm_control(direction, diff, True)
    assert 1 == 1


@then('I turn on hair dryer')
def turn_on_hair_dryer(context):
    relay.turn_on_hair_dryer()


@then('I turn off hair dryer')
def turn_off_hair_dryer(context):
    relay.turn_off_hair_dryer()


@then('I turn on water')
def turn_on_water(context):
    relay.turn_on_water()
    sleep(3)


@then('I turn off water')
def turn_off_water(context):
    relay.turn_off_water()
