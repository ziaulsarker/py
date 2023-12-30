# """DOCS MOTHER FUCKERS"""

# # 9.1 
# class Resturant :
#   """ Resturant ClassYou Bitchas """
#   def __init__(self, resturant_name: str, cusine: str) -> None:
#     self.resturant_name = resturant_name
#     self.cusine = cusine
#     self.open_resturant = False
#     self._number_server = 0

#   def get_number_server(self): 
#     print(f"Number Servered {self._number_server}")

#   def set_num_served(self, num_served):
#     if num_served > self._number_server :
#       self._number_server = num_served
  
#   def increment_num_served(self, increment_num_served = 1):
#     if increment_num_served >= 1 : 
#       self._number_server += increment_num_served

#   def make_food(self, food) :
#     print(food)

#   def describe_resturant(self) :
#     print(f'{self.resturant_name.upper()} serves up {self.cusine}')

#   def open_resturant(self) :
#     self.open_resturant = True
#     print(f"Resturant is now open")

#   def close_resturant(self) :
#     self.open_resturant = False




# my_store = Resturant("AZ's", "American Fusion")
# my_store.describe_resturant()


# my_store.get_number_server()

# my_store.increment_num_served()

# my_store.get_number_server()


# my_store.increment_num_served(10)

# my_store.get_number_server()

# my_store.set_num_served(12)

# my_store.get_number_server()



# amena_resturant = Resturant("amenas", "American Fusion")
# amena_resturant.describe_resturant()

# moms = Resturant("moms", "Benaglie Fusion")
# moms.describe_resturant()



class User : 
  def __init__(self, fname='', lname='', password=None) :
    self.fname = fname
    self.lname = lname
    self.login_appemt = 0

  def describe_user(self) :
    return [ key for key in self.__dict__ ]
  
  def greet_user(self) :
    print(f'yoo whats cracking {self.fname.title()} {self.lname.title()}')

  def increment_login_appemt(self) :
    self.login_appemt += 1

  def reset_login_appemt(self) :
    self.login_appemt = 0

me = User("ziaul" ,  "sarker")

print(me.describe_user())

me.increment_login_appemt()
me.increment_login_appemt()

print(me.login_appemt)

me.increment_login_appemt()

print(me.login_appemt)

me.reset_login_appemt()

print(me.login_appemt)






