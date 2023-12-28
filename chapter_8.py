# 8.1
def msg() : 
  print("hello motherfucker")

msg()

def favorite_book(title) :
  print(f'my favorite book is {title.title()}')

favorite_book(title='Legend of Drizzt')

def make_shirt(size='large', msg='i love python') :
  print(f"the size is {size} with msg {msg.title()}")

make_shirt('small', 'this is a shirt')
make_shirt(size='medium', msg='this is a shirt keyword')

make_shirt()


def describe_city(city, country='USA') :
  if city and country :
    print(f"the city {city} is {country}")
  if city and country is None : 
    print(f"the city {city}")
  if country and not city : 
    print(f"the country {country}")

describe_city('New York', "USA")
describe_city(city='New York')
describe_city(None)

# 8.7
def make_album(name:str, album:str, num_somgs:int=None) :
  my_album = {}

  if not name or not album : return my_album

  my_album['name'] = name.title()
  my_album['album'] = album

  if num_somgs : 
    my_album['num_somgs'] = num_somgs

  return my_album


album_1 = make_album('mike jones', 'all on me', 10)
album_2 = make_album('50 cent', 'get rich or die trying')

print(album_1)

print(album_2)







