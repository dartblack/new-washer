from libs.relay import Relay
from time import sleep

relay = Relay()

relay.turn_on_water()
sleep(3)
relay.turn_off_water()
relay.turn_on_hair_dryer()
sleep(50)
relay.turn_off_hair_dryer()
