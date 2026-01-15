# create your own sum function in python


def my_sum(*numArgs, **kwargs):
  sum = kwargs['start'] if 'start' in kwargs else 0
  for num in numArgs:
    if isinstance(num, list): 
      for n in num:
        sum += n
    else:
      sum += num
  
  return sum

print(my_sum(1,2,3,4,5,[6,7,8,9,10]))  # should return 55
