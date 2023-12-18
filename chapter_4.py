# 4.1
fav_pizzas = ['cheese', "meat", 'veggies']
 
for pizza in fav_pizzas: 
  print(f'i love {pizza} pizza')

print('pizza pizza pizza')

#4.3 - #4.9

million = 1_000_000

for num in range(0, million + 1):
  print(num)



sum_of_million = sum(list(range(0, million)))
min_of_million = min(list(range(0, million)))

print('sum of', sum_of_million)
print('min of', min_of_million)

odd_nums = range(1, 20, 2)
for odd_num in odd_nums:
  print(odd_num)


multiplese_of_thirty = range(3, 31, 3)
for multiple in multiplese_of_thirty:
  print(multiple)


for num in range(0, 11) :
  print(num**3)

first_ten_cibed = [num ** 3 for num in range(0,11)]
print(first_ten_cibed)



# 4.13

items_in_buffet = ("chicken", "fish", "shakes", "beef", "fries")

for item in items_in_buffet: 
  print(item)



new_items_in_buffet = ("pork", "fish", "shakes", "beef", "viel")

for item in new_items_in_buffet:
  print(item)


