# 10.1
def state_location(city: str, country: str, population: int = 0) -> str :

  if population and population > 0 :
    return f'{city}, {country} - population {population}'
  else :
    return f'{city}, {country}'


my_city = state_location("New York", "USA")


class Employees : 
  def __init__(self, first_name: str, last_name: str, salary: int) : 
    self.first_name = first_name
    self.last_name = last_name
    self.salary = salary
  
  def give_raise(self, amount: int = 5_000): 
    self.salary += amount
  
  