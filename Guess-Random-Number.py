# Guessing Random Number

# Importing Random Module

import random
import time

num = random.randint(1,10)
guess = 0

while guess != num:
    guess = int(input("Try to guess the number between 1 and 10 :"))
    if guess > num:
        print("It's too high!")
    elif guess < num:
        print("It's too low!")

time.sleep(2)

print("\n Wow !, You got it Right...")