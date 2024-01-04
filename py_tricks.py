# implement a context manager that measures the execution of a code block using the time.time function 
# use both a decorator and a class-based variant

from contextlib import contextmanager
from time import time, sleep, gmtime

# @contextmanager
# def ex_timer_decorator(cb, *args) :
#   start_time = time()
#   end_time = start_time
#   try :
#     yield 
#   finally:
#     pass


# # def console():
# #   print('hello python')
   

# # with ex_timer_decorator(print, 'hello') as t :
# #   print(t)
# #   with ex_timer_decorator(print, 'world') as z :
# #     print(f'{t} {z}')
# # print('done!!')


class Ex_timer(): 

  def __init__(self, start) :
    self.time = start

  def __enter__(self) : 
    print(f'{self.time} seconds to start')
    sleep(2)
    self.time = time()
    return self
  
  def __exit__(self, exc_type, exc_value, exc_trackback) :
    self.time = time()
  
  def timer(self):
    print(f'{self.time} seconds to end \n')
  

with Ex_timer(time()) as t :
  t.timer()
  with t : 
    t.timer()
    with t :
      t.timer()

    

  

  





