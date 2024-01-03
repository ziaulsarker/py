# # 10.1 - 10.3
import json
from pathlib import Path

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

# def add_two_nums() :
#   while True : 
#     try :
#       first_number = int(input('enter first number to add '))
#     except ValueError :
#       print('opps that is not a number, please enter a numerical value')
#       continue 
#     else : 
#       break
  
#   while True :
#     try :
#       second_number = int(input('enter second number to add '))
#     except ValueError :
#       print('opps that is not a number, please enter a numerical value')
#       continue 
#     else : 
#       break

#   sum_of_nums = first_number + second_number
  
#   print(f'the sum on {first_number} + {second_number} is : {sum_of_nums}')


file_paths = [*Path('./').glob("*.txt")]

def readFiles(files: str) -> None :
  for file in files :
    current_file = Path(file)
    try : 
      print(f'now reading {current_file}')
      file_text = current_file.read_text()
    except FileExistsError :
      print('opps that file dont exist')
    else :
      print(file_text + '\n')

# readFiles(file_paths)

json_file_path = 'fav_num.json'

def save_user_fav_number(json_file_path) : 
  while True : 
    try : 
      fav_num = int(input('enter your favorite number : '))
    except ValueError : 
      print('you must enter a numerical value : ')
    else : 
      json_file = Path(json_file_path)
      strigify_json = json.dumps({'fav_num': [fav_num]})
      
      if json_file.exists() :
        fav_nums = read_user_fav_number_from_file(json_file_path)
        fav_nums['fav_num'].append(fav_num)
        json_file.write_text(json.dumps(fav_nums))
        break
    
      Path.touch(json_file_path)
      Path(json_file_path).write_text(strigify_json)
      break


def read_user_fav_number_from_file(file) :
  fav_num_json = Path(file)
  try : 
    if fav_num_json.exists() :
      print('content',fav_num_json.read_text())
      fav_num = json.loads(fav_num_json.read_text())
  except (FileExistsError) : 
    print('opps file dont exist')
  except json.JSONDecodeError :
    print('opps could not decode json pussy')
  else : 
    print(fav_num)
    return fav_num
    
save_user_fav_number(json_file_path)     









