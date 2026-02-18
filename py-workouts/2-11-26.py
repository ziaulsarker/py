# write a function run_time that asks the user to enter a distance in miles and a time in minutes, then the function continues to ask how long in minutes it looks for addinoal runs until the user enters enter.
def run_time():

  runs = []

  while True:
    if len(runs) == 3:
      break
    run = float(input('Enter 10k run time : '))
    if not run:
      run = float(input('Enter 10k run time : '))
    runs.append(run)

  average_time = sum(runs) / len(runs)

  print(f"Average run time: {average_time}")  

  return average_time


run_time()