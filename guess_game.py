import random


def main():
    secret_number = int((random.randint(1, 11)))
    guess = 0
    tries = 0
    tries_limit = 3
    out_of_tries = False

    def lower_or_higher():
        if guess < secret_number:
            print("higher")
        elif guess > secret_number:
            print("lower")

    print("guess the secret number! (1-10)")
    print("you have three tries")

    while int(guess) != secret_number and out_of_tries == False:
        guess = int(input("enter guess: "))
        tries += 1
        lower_or_higher()
        if tries > tries_limit:
            out_of_tries = True

    if out_of_tries == True:
        print("you failed no one loves you")
        main()
    elif out_of_tries == False:
        print("NICE YOU DID IT!")
        main()


main()
