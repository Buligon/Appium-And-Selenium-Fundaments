import pytest
from classes import Motorcycle
 
moto = Motorcycle('Suzuki', 'Hayabusa')
print(moto)
moto.turn_engine_on()
moto.turn_headlight_on()
moto.start_driving()
moto.turn('left')
moto.turn('right')
print(moto)
moto.stop_driving()
moto.turn_engine_off()
moto.turn_headlight_off()