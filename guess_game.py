# guess the number! Input a level, and then guess the randomly generated number between 1 and your level

import random

# prompt user for a level, n
while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            continue
# if user does not input a positive integer, prompt again
    except ValueError:
        continue

# randomly generate an integer between 1 and n using random module
    range = random.randint(1, level)
    break

# prompt user to guess integer
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 0:
           continue
# if guess is not positive integerk prompt user again
    except ValueError:
        continue
# if guess smaller than integer, output "Too small" and prompt again
    if guess < range:
        print("Too small!")

# if guess larger than integer, output "Too large" and prompt user again
    elif guess > range:
        print("Too large!")

# if guess same as integer, output "Just right" and exit
    else:
        print("Just right!")
        break
