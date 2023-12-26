# 7.1

prompt = 'yoo bitch ass what car you want '
car_desired = input(prompt)

print(f'let me check if we have that shit, hold on pussy. \n aii we got {car_desired}')


# 7.2

prompt = 'how many people do you have. '

group_size = input(prompt)

int_group_size = int(group_size)

max_group_size = 8

if(int_group_size > max_group_size) : 
  print('sorry you have to wait bitch ass the table aint ready')
else :
  print('your table is ready')



# 7.3
prompt = 'pick a number. '

user_number = input(prompt)

int_user_number = int(user_number)

if(int_user_number % 10 == 0) :
  print('its a multiple of 10 smart ass')
else : 
  print('its NOT a multiple')


# 7.4

flag = True
prompt = 'what tooping you want. '
pizza_toppings = []

while flag :
  msg = input(prompt)

  if msg == 'quit' :
    flag = False
  else :
    pizza_toppings.append(msg)

print(pizza_toppings)
  



prompt = 'how old are you: '

while True :
  user_input = input(prompt)
  age = int(user_input)

  if age < 3 :
    price = 0
  elif age > 3 and age < 12 :
    price = 10
  elif age > 12 : 
    price = 15
  break

print(f'the price is ${price}')


# 7.6





