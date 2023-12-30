"""DOCS MOTHER FUCKERS"""

# 9.1 
class Resturant :
  """ Resturant ClassYou Bitchas """
  def __init__(self, resturant_name: str, cusine: str) -> None:
    self.resturant_name = resturant_name
    self.cusine = cusine
    self.open_resturant = False

  def make_food(self, food) :
    print(food)

  def describe_resturant(self) :
    print(f'{self.resturant_name.upper()} serves up {self.cusine}')

  def open_resturant(self) :
    self.open_resturant = True
    print(f"Resturant is now open")

  def close_resturant(self) :
    self.open_resturant = False


my_store = Resturant("AZ's", "American Fusion")
my_store.describe_resturant()

amena_resturant = Resturant("amenas", "American Fusion")
amena_resturant.describe_resturant()

moms = Resturant("moms", "Benaglie Fusion")
moms.describe_resturant()



class User : 
  def __init__(self, fname='', lname='', password=None) :
    self.fname = fname
    self.lname = lname

  def describe_user(self) :
    return [ key for key in self.__dict__ ]
  
  def greet_user(self) :
    print(f'yoo whats cracking {self.fname.title()} {self.lname.title()}')

me = User("ziaul" ,  "sarker")

print(me.describe_user())

