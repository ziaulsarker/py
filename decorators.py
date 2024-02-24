from time import time, localtime, time_ns

def say_loud(fn) :

  def wrapper() :
    return_result = fn()
    return return_result.upper()

  return wrapper

def say_somthing(fn) : 
  def wrapper(*args, **kwargs) :
    if (kwargs.get('vol') == 'loud') :
      print('its loud')
    elif (kwargs.get('vol') == 'soft') :
      print('its soft')
    return fn(*args, **kwargs)
  
  return wrapper

@say_somthing
def say(name, vol='loud') :
  return f"Hello {name}"

say("hello")



  
# def looger(fn) :
#   def wrapper(*args, **kwargs) :
#     starting = time_ns()
#     print(f'starting {starting}')
#     x = fn(*args, **kwargs)
#     end = time_ns();
#     print(f'finished took {end - starting}')
#     return x
#   return wrapper


# @looger
# def say(name) :
#   return f"Hello {name}"



# print(say(name='world'))

