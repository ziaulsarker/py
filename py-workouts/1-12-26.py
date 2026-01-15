# gueesing game where the user has to guess a number between 1 and 100. The program should give feedback on whether the guess is too high, too low, or correct. The game should continue until the user guesses the correct number.


import random;

def guessing_game(): 
    random_number = random.randint(1, 100)
    user_input = input("guess a number from 1 to 100 : ")
    continue_game = True
    num_of_guess = 3


    while continue_game:
        if int(user_input) == random_number:
            continue_game = False
            print("JUST RIGHT BITCH!!!, Congratulations! You guessed the correct number.")
            num_of_guess = 3
     
        if int(user_input) < random_number:
            user_input = input("Too low! Try again: ")

        if int(user_input) > random_number:
            user_input = input("Too high! Try again: ")
        
        if num_of_guess == 0: 
            continue_game = False
            print('Opps bitch you dead')

        num_of_guess = num_of_guess - 1


guessing_game() 