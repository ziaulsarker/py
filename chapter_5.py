# 5.1

# should print true for the following

car = 'audi'

if (car == 'audi') : 
  print(True)
  
if (car.capitalize() == 'Audi') : 
  print(True)

if (car.title() == 'Audi') :
  print(True)

if (car.lower() == 'audi') : 
  print(True)

if (car.lower() == 'AUDI') : 
  print(True)

if (car[-1] == 'audi'[-1]) : 
  print(True)


# should print false for the following
animal = 'amena'

if (animal != 'tiger') :
  print(False)

print( animal != 'amena' )

if (animal == 'amena') : 
  print(False)

print(animal == car)

print(len(car) < 0)


# 5.2
print('#5.2')

print(len(animal))
print((len(car) + len(animal[len(car):]) ))
print(len(animal) == (len(car) + len(animal[len(car):]) ))
print(len(animal) > len(car))
print(list(animal))
print(list(car).pop(0).lower() == list(animal).pop().lower())

a = 1988
z = 1900

me = 1990


print(a > z)

print(a < z)

print(a > z and me > a)

print( (z > me) or me == 1990  )

print(z >= a and z <= a)

arr = [1,2,3,4]

print(1 in arr)

print(10  in arr)