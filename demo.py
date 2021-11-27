from libs.relay import Relay
from time import sleep

relay = Relay()

relay.turn_on_hair_dryer()
sleep(5)
relay.turn_off_hair_dryer()
