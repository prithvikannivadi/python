# Prompts the user for a level between 1, 2, 3
# Randomly generates 10 math problems formatted as X + Y =
# Prompts the user to solve each of those problems. If an answer is not correct the program will output EEE and prompt the user again.
# After 3 tries, the program will output the correct value and move on
# The program will ultimately output the user’s score: the number of correct answers out of 10.

import random

def main():
    level = get_level()
    score = get_score(level)

    print("Score: ", score)

# prompt/re-prompt user for level and return 1,2,3
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                 break
        except:
            pass
    return level

# returns randomly generated non-negative integer with level digifts or raises ValueError if level is not 1,2,3
def generate_integer(level):

        if level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
        elif level == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
        elif level == 3:
            x = random.randint(100,999)
            y = random.randint(100,999)
        return x,y

# use x, y levels from above to randomly generate math problems
# user must solve these problems in under 3 tries, or program moves on and outputs correct answer
def get_round(x,y):
    tries = 1
    while tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                 return True
            elif answer != (x + y):
                 tries += 1
                 print("EEE")
        except:
             tries += 1
             print("EEE")

    print(f"{x} + {y} = {x + y}")
    return False

# calculate user score based on how many they got correct
def get_score(level):
    round = 1
    score = 0
    while round <= 10:
        x,y = generate_integer(level)
        user_input = get_round(x,y)
        if user_input == True:
            score += 1
        round += 1

    return score

if __name__ == "__main__":
    main()
