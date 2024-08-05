# HERE WE WRITE A FUNCTION THAT WHENEVER THE COMPUTER GUESSES A NUMBER THAT WE HAVE IN MIND:

import random

# Computer vs Me:
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again, Too low...')
        elif guess > random_number:
            print('Sorry, guess again. Too high...')
    print(f'Yay, Congrate, You have guessed the number {random_number} Correctly!!! ')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c': # you telling the computer is correct!
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high(H), to low(L), or correct(c)???').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l': # this is a small letter for L
            low = guess + 1
    print(f'Yay! The Computer guessed your number, {guess}, correctly!')


computer_guess(1000)


# Me vs computer
def guess2(x):
    random_number2 = random.randint(1, x)
    guess2 = 0
    while guess2 != random_number2:
        guess2 = int(input(f'Guess a number between 1 and {x}: '))
        if guess2 < random_number2:
            print('Sorry, guess again, Too low...')
        elif guess2 > random_number2:
            print('Sorry, guess again. Too high...')
    print(f'Yay, Congrate, You have guessed the number {random_number2} Correctly!!! ')


guess2(1000)