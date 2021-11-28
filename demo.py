from libs.relay import Relay
from time import sleep

relay = Relay()

relay.turn_on_water()
sleep(50)
relay.turn_off_water()
