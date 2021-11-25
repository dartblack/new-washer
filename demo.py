from libs.relay import Relay
from time import sleep

relay = Relay()

relay.turn_on_hair_dryer()
relay.turn_on_water()
sleep(5)
relay.turn_off_hair_dryer()
relay.turn_off_water()
