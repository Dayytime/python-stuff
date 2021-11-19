import random


def play():
    player_choice = input("Select rock, paper, or scissors: ").lower()
    pc_choice = random.choice(["rock", "paper", "scissors"])

    if player_choice == pc_choice:
        print("cool")
    elif player_choice == "paper" and pc_choice == "rock" or player_choice == "rock" and pc_choice == "scissors" or player_choice == "scissor" and pc_choice == "paper":
        print("YOU WON")
    else:
        print("YOU LOST")


play()
