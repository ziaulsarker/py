import math
# 3.1 - 3.3

names = ["ziaul", "amena"]

print(names[0], names[1])

print(f"Hi {names[0]}, and {names[-1]} so gald to have your bitch ass here")

cars = ["lambo", "benz"]

for index, car in enumerate(cars): 
  print(f"{car} is in {index}")

try: 
  lambo = cars.index("benz", 0, 1)
  print(lambo)
except ValueError: 
  print('oops value error pussy')


# 3.4
guests = ["micheal jordan", "micheal jackson", "mike tyson"]
msgs_for_guest = [f"yoo bitch ass {guest}, glad you made it" for guest in guests]
print(msgs_for_guest)

# 3.5 and 3.6
print(f"sorry {guests[-1]} had to cancle")

guests[-1] = 'mike myars'

new_msgs_for_guest = [f"yoo bitch ass {guest}, glad you made it" for guest in guests]

print(new_msgs_for_guest)


guests.insert(0, "Bill cosby")

middle = math.floor(len(guests) / 2)
guests.insert(middle, "Lebron JAMES")

guests.append("Money Mayweather")

print(guests)


# 3.7
tmt = guests.pop();
movie_myars = guests.pop();
pop_king = guests.pop();
bb_god = guests.pop();

x_guests = [tmt, movie_myars, pop_king, bb_god]

x_guests_msg = [f"{x_guest} sorry you are uninvited" for x_guest in x_guests]


print(x_guests_msg)


print('current guests', guests)

del guests[:]
print("new guests", guests)


# 3.8
locations = ['london', "sweden", 'praguae', 'europe']
sorted_list = sorted(locations)
sorted_list_reversed = sorted(locations, reverse=True)
print(locations)
print(sorted_list)
print(sorted_list_reversed)

locations.sort();

print(locations)

locations.reverse()


print(locations)
locations.reverse()
print(locations)

locations.sort(reverse=True)



# 3.9
print(f"{len(x_guests)} is Not coming to the party")

# 3.10
list_of_songs = ["aint no sunshine", "loose yourself", "goldie"]

print(sorted(list_of_songs))

reverse_list_of_songs = reversed(list_of_songs)

for song in reverse_list_of_songs :
  print(song)


