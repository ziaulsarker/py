# 6.1
me = {
  'first_name': 'Ziaul',
  'last_name': 'Sarker',
  'age': 33,
  'city': 'Long Island'
}

for key, value in me.items(): 
  print(f'{key} = {value}')


niggas_fav_number = {
  "bill": 'black',
  'rob': 'blue',
  'mike': 'green',
}

for (nigga, color) in niggas_fav_number.items() :
  print(f'this nigga {nigga} fav color is {color}')


glossary = {
  'clousures': 'a way to create a private varbles',
  'functions': 'a way to reuse code from'
}


print(glossary['clousures'])