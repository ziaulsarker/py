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

# 5.3 

aliens_color = "red"

if(aliens_color == "green"): 
  print('got 5 points')
elif (aliens_color == "yellow"): 
  print('got 10 points')
elif (aliens_color == "red"): 
    print('got 15 points')


age = 32

if (age < 2):
  print('you a baby')
elif (age < 4):
  print('u a todler')
elif (age < 13):
  print('you a kid')
elif (age < 20): 
  print('you a teen')
elif age < 65 :
  print ('you are an adult')
elif ( age >= 65):
  print("u old as fuckk ")


favorite_fruits = ['mango', 'watermelon', 'apple']

other_fruits = ['blueberries', 'bananas', 'orange', 'peach', 'mango', "limes"]

for fruit in other_fruits :
  if fruit in favorite_fruits: 
    print(f'your bitch ass realluy like {fruit}')
  else : print(f'your bitch DONT LIKE {fruit.upper()}')

  
print("fuck fruits")


# 5.8
users = ["ziaul", "admin", "mike", "bill", "larry"]

if not users: 
    print('no user found')

for user in users :
  if(user.lower() == 'admin'): 
    print(f'hello {user}')
  else :
    print(f'hello {user} u ugly motherfucker')


#5.10
active_users = users[:]

new_useres = active_users[2:4] + ['ross', 'lebron']

for user in new_useres :
  if(user.lower() in active_users): 
    print(f'sorry {user} is already in use')
  else :
    print(f"ohh you good {user} mother fucker")
  


   