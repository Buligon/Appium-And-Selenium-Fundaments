class Vehicle:
  is_engine_on = False
  is_headlight_on = False
  is_driving = False
  make = None
  model = None

  def __init__(self, make, model):
    self.make = make
    self.model = model

  def __repr__(self):
    return (f'{self.make} {self.model} with engine '
            f'{"on" if self.is_engine_on else "off"} '
            f'and headlight {"on" if self.is_headlight_on else "off"}')

  def turn_engine_on(self):
    print('Turning engine on')
    self.is_engine_on = True

  def turn_engine_off(self):
    print('Turning engine off')

    if self.is_driving:
      print('You tried to turn the engine off while driving, and crashed')
      return
    
    self.is_engine_on = False

  def turn_headlight_on(self):
    print('Turning headlight on')
    self.is_headlight_on = True

  def turn_headlight_off(self):
    print('Turning headlight off')
    self.is_headlight_off = False
  
  def start_driving(self):
    if not self.is_engine_on:
      print("You can't drive without turning the engine on!")
      return
    
    print('Starting to drive')
    self.is_driving = True
  
  def stop_driving(self):
    print('Stopping')
    self.is_driving = False

class Motorcycle(Vehicle):
  def lean(self, direction):
    if not self.is_driving:
      print('You leaned while not driving, and crashed!')
      return
    
    print(f'Leanin {direction}')

  def turn_handlebars(self, direction):
    print(f'Turning handlebars {direction}')
  
  def turn(self, direction):
    if direction == 'left': 
      self.turn_handlebars('right')
      self.lean('left')
    elif direction == 'right':
      self.turn_handlebars('left')
      self.lean('right')
    else:
      print("Didn't understand that direction")

class Car(Vehicle):
  def turn(self, direction):
    if direction == 'left': 
      print('Turning left')
    elif direction == 'right':
      print('Turning right')
    else:
      print("Didn't understand that direction")

""" moto = Motorcycle('Suzuki', 'Hayabusa')
print(moto)
moto.turn_engine_on()
moto.turn_headlight_on()
moto.start_driving()
moto.turn('left')
moto.turn('right')
print(moto)
moto.stop_driving()
moto.turn_engine_off()
moto.turn_headlight_off() """