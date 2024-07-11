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


print(10 * float(8.9))




def lowercase_decorator(fn) :

  def decorated_callable() :
    result_of_callable = fn()
    return result_of_callable.lower()
  
  return decorated_callable

# the original callable
def callable_to_deforate() :
  return 'Hello WORLD!'

# the callable that will "DECORATED"
@lowercase_decorator
def decorated_callable() :
  return 'Hello WORLD!'


originale_callable = decorated_callable
decorated_original_callable = lowercase_decorator(callable_to_deforate)

# invoke the callables 
# the actully function result with out it being mutated
print(originale_callable()) # 'Hello WORLD!'

# the decorated result 
print(decorated_original_callable()) # 'hello world!'

print('Calling')