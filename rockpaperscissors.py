# A fun and simple game of rock, paper, scissors

import random

RPS_Choices = ["R", "P", "S"]
player_score = 0
cpu_score = 0
tie = 0

# ask player to select between Rock, Paper, Scissors, or Quit
def main():
    global player_score, cpu_score, tie
    print("Thank you for playing Rock, Paper, Scissors, please select from an option below!")
    print("Type 'R' for Rock, 'P' for Paper, 'S' for Scissors, or 'Q' to Quit")
    while True:
        player_input = get_player_input()
        if player_input == "Q":
            break
        cpu_input = get_cpu_input()
        player_score, cpu_score, tie = get_winner(player_input, cpu_input, player_score, cpu_score, tie)
    # Display score after quitting the game
    print("Final Score")
    print(f"Player: {player_score}, Computer: {cpu_score}, Tie: {tie}")
    print("Thank you for playing!")

# check if player entry is valid. If not, re-prompt player for a valid entry
def get_player_input():
    while True:
        player_input = input("Rock, Paper, Scissors Shoot!: ").upper()
        if player_input in RPS_Choices or player_input == "Q":
            return player_input
        else:
            print("Invalid entry! Try again")

# returns randomly generated choice for the CPU
def get_cpu_input():
    cpu_input = random.choice(RPS_Choices)
    print(f"Computer chooses: {cpu_input}")
    return cpu_input

# compare player choice with randomly selected "cpu" choice and decide winner
def get_winner(player_input, cpu_input, player, cpu, tie):
    if player_input == cpu_input:
        print("Tie!")
        tie += 1
    elif (player_input == "R" and cpu_input == "S") or (player_input == "P" and cpu_input == "R") or (player_input == "S" and cpu_input == "P"):
        print("You Win!")
        player += 1
    else:
        print("Computer Wins!")
        cpu += 1
    return player, cpu, tie

if __name__ == "__main__":
    main()
