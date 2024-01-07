# 10.1
def state_location(city: str, country: str, population: int = 0) -> str :

  if population and population > 0 :
    return f'{city}, {country} - population {population}'
  else :
    return f'{city}, {country}'


my_city = state_location("New York", "USA")

print(my_city)