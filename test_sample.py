from chapter_11 import state_location

def test_state_location() :
  expected_result = 'New York, USA'
  city_country = state_location('New York', 'USA')
  assert expected_result == city_country



