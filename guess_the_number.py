import random


def choice(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_num:
            print("Higher")
        elif guess > random_num:
            print("Lower")
    print(f"NICE YOU GOT THE NUMBER WHICH WAS {random_num}")


choice(10)
