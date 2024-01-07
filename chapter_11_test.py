from chapter_11 import state_location, Employees


def test_state_location_with_out_population() :
  expected_result = 'New York, USA'
  city_country = state_location('New York', 'USA')
  assert expected_result == city_country


# 11.2
def test_state_location_with_population () :
  city = 'New York'
  country = 'USA'
  population = 1_000_000

  expected_result = f'New York, USA - population 1000000'
  city_country = state_location(city, country, population)
  assert expected_result == city_country





def test_employee () :
  elmployee = Employees('ziaul', 'sarker', 1_000_000)

  assert elmployee.salary == 1_000_000
  assert elmployee.first_name == 'ziaul'
  assert elmployee.last_name == 'sarker'


def test_emplyee_raise_meathod() :
  elmployee = Employees('ziaul', 'sarker', 1_000_000)
  elmployee.give_raise()

  assert elmployee.salary == 1_005_000


def test_emplyee_custom_raise_meathod() :
  elmployee = Employees('ziaul', 'sarker', 1_000_000)
  elmployee.give_raise(1_000_000)

  assert elmployee.salary == 2_000_000