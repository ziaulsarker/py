# # 10.1 - 10.3
# from pathlib import Path

# file = Path('chapter_10.txt')
# file_text_content = file.read_text()



# print(file_text_content)

# for line in file_text_content.splitlines(): 
#   print(line + '\n')


# line_read = 0
# while line_read < len(file_text_content.splitlines()) :
#   print(file_text_content.splitlines()[line_read], "\n")
#   line_read += 1

# file_text_content = file_text_content.replace('python', 'rust')

# print(file_text_content)


# # 10.4 

# # one way
# guest_name = input('Enter guest name : ')
# guests_registry = open('chapter_10_guests.txt', '+a')
# guests_registry.writelines(guest_name + '\n')
# guests_registry.close()

# # another way
# guest_name = input('Enter guest name : ')
# guests_registry = Path('chapter_10_guests.txt')
# guests_registry = guests_registry.open(mode='+a')
# guests_registry.writelines(guest_name + '\n')
# guests_registry.close()

# # another way -> much cleaner
# with Path('chapter_10_guests.txt').open(mode='+a') as f : 
#   f.writelines(guest_name + '\n')


# 10.6

def add_two_nums() :
  while True : 
    try :
      first_number = int(input('enter first number to add '))
    except ValueError :
      print('opps that is not a number, please enter a numerical value')
      continue 
    else : 
      break
  
  while True :
    try :
      second_number = int(input('enter second number to add '))
    except ValueError :
      print('opps that is not a number, please enter a numerical value')
      continue 
    else : 
      break

  sum_of_nums = first_number + second_number
  
  print(f'the sum on {first_number} + {second_number} is : {sum_of_nums}')


add_two_nums()







