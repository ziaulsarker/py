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
