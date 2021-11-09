from behave import *
from libs.sensor import Sensor

use_step_matcher("re")
sensors = Sensor()
sensors.init_sensors()


@given("Start wash car")
def step_impl(context):
    assert 1 == 1


@when("I Get Car Positions")
def step_impl(context):
    assert 2 == 2
