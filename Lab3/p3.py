# Write a Python program to guess a number between 1 to 9.
# Note: User is prompted to enter a guess. If the user guesses wrong then the prompt
# appears again until the guess is correct, on successful guess, user will get a "Well
# guessed!" message, and the program will exit.

import random 

rand_num =  random.randint(1,9)

while True:
    guess = int(input('Enter a number:'))   
    if guess==rand_num:
        print('Well guessed!')
        break
    else:
        print("try again")