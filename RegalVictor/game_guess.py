import random

# Computer Vs Me
# Me vs Computer

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))  #  f string formatters
        if guess < random_number:
            print("Sorry, Guess again, Your guess if Low!...")
        elif guess > random_number:
            print("Sorry, guess again, Your guess is High!...")
    print(f'Yay, Congrates!! You have guessed the {random_number} Correctly!!!')

# the computer section
def computer_guess(x):
    low = 1 # letter small L
    high = x
    feedback = ''
    while feedback != 'c' : # you telling the computer is correct!
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high(H), or too low(L), or correct(c)???').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guessed your choice, {guess}, correctly!!!')


computer_guess(100) # here computer should not guess pass the range 100 while we have 57 in mind

"""
where computer has a number in mind
then you pick a guess!
"""