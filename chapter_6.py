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




# 6.5

rivers = {
  'missippie': 'luisiana',
  'goerge': "NY",
  'ganji': "india",
}


for river, location in rivers.items() :
  print(f'\n the {river} is in {location}')


# 6.6
  
favorite_languages = {
  "bill": 'C++',
  "rob": 'Python',
  "ziaul": "js"
}
  
people_taken_poll = ['ziaul', 'mike', 'rob' ]

for person in favorite_languages : 
  if person not in people_taken_poll :
    print(f'\n{person} please take out poll')
  
  if person in people_taken_poll :
    print(f'\nyo bitch ass {person}, thanks for taking the pill!!')


# 6.7
    
me = {
  'first_name': 'Ziaul',
  'last_name': 'Sarker',
  'age': 33,
  'city': 'Long Island'
}

amena =  {
  'first_name': 'Amena',
  'last_name': 'Pat',
  'age': 21,
  'city': 'Long Island'
}

mike =  {
  'first_name': 'Mike',
  'last_name': 'Rob',
  'age': 30,
  'city': 'Canada'
}


peoples = [me, amena, mike]

for person in peoples : 
  print(f'hi im {person['first_name'].upper()} here are some stuff about me ')
  for infor in person : 
    print(f'\n {infor} : {person[infor]} \n')



niggas_fav_number = {
  "bill": [0, 1],
  'rob': [100, 11],
  'mike': [5, 2],
}

for person in niggas_fav_number :
  print(f'hi im {person}, my favorite numbers are', *niggas_fav_number[person])

my_set = {'uoo', 1, 2,3 }

print(my_set)


