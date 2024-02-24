from time import time, localtime, time_ns

def say_loud(fn) :

  def wrapper() :
    return_result = fn()
    return return_result.upper()

  return wrapper

def say_somthing(fn) : 
  def wrapper(*args, **kwargs) :
    # print('kwargs', **kwargs)
    if (kwargs['vol']== 'loud') :
      print('its loud')
    elif (kwargs['vol'] == 'low') :
      print('its soft')
    x = fn(*args, **kwargs)
    return x 
  return wrapper




def looger(fn) :
  def wrapper(*args, **kwargs) :
    starting = time_ns()
    print(f'starting {starting}')
    x = fn(*args, **kwargs)
    end = time_ns();
    print(f'finished took {end - starting}')
    return x
  return wrapper

@say_somthing
@looger
def say(name, vol='loud') :
  return f"Hello {name}"

print(say(name='world', vol='loud'))

