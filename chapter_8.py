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



# 8.8

artists = {}

while True : 
  artist_name = input('Artist Name or q to quit ')
  if artist_name == 'q' : 
    print('good bye')
    break

  album_name = input('artist album or q to quit ')
  if album_name == 'q' : 
    print('good bye')
    break

  album = make_album(artist_name, album_name)

  artists[artist_name] = album

  print("album =>", album)

  should_continue = input('want to add more albums (y/n) ')

  if should_continue == 'y' : continue 
  break

print(artists.get('asap rocky', 'opps not found'))


8.9
def show_msg(my_list: [str]) :
  for x in my_list :
    print(x)
    

show_msg(['artist', 'album'])


msg_que = ["yoo", 'whats cracking']
sent_msg = []

print(msg_que, sent_msg)

def send_msg(msg_que: [str], msg_sent: [str]) :
  print("inside, fn before loop", msg_que, msg_sent)
  while msg_que :
    first_msg = msg_que.pop(0)
    msg_sent.append(first_msg)
  
  print("inside, fn after loop", msg_que, msg_sent)
  return (msg_que, msg_sent)




print(msg_que, sent_msg, send_msg(msg_que[:], sent_msg[:]))


# 8.12

def sandwich(*topings) :
  for toping in topings :
    print(f'putting {toping} in the sandwich')

  print(f'now you got a sandwich with the following toppoings {topings}')



sandwich('beek', 'cheese', 'pickels', 'sauce')


# 8.13

def build_profile(fname, lname, **kwargs) :
  kwargs['first_name'] = fname
  kwargs['last_name'] = lname

  return kwargs


print(build_profile('ziaul', 'sarker', **{'age': 33, "hobby": 'coding', 'lover': 'amena'} ))

# 8.14

def build_car(model, make, **kwargs) :
  kwargs['model'] = model
  kwargs['make'] = make

  return kwargs

print(build_car('accord', 2023, color='blue', miles=35_000))
