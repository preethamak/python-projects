import random

def guess(x):
    num = random.randint(1, x)
    guess = None
    while guess != num:
        guess = int(input(f'Guess the number between 1 and {x}: '))
        if guess < num:
            print("Sorry, that's too low.")
        elif guess > num:
            print("Sorry, that's too high.")
            
    print(f'Yes! You guessed it right. The number is {num}.')
     
guess(10)