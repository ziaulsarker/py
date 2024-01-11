def say_loud(fn) :

  def wrapper() :
    return_result = fn()
    return return_result.upper()

  return wrapper

  
def looger(fn) :
  def wrapper(*args, **kwargs) :
    return fn(*args, **kwargs)
  return wrapper


@looger
def say(name) :
  return f"Hello {name}"



print(say(name='world'))

