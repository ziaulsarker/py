from car import Car
from battery import Battery

class Ev(Car): 
  def __init__(self, carObj) : 
    make, model, year = carObj.values()
    print(f'make -> {make}, model -> {model}, year -> {year}')
    super().__init__(make, model, year)
    self.battery = Battery()




