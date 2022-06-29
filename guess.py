import random


def guess(num):
    random_num = random.randint(1, num)
    guess = 0

    while guess != random_num:
        guess = int(input(f"Guess the number between 1 and {num}: "))

        if guess < random_num or guess > random_num:
            print("That's incorrect. Try again.")

    print(f"Congratulations. You guessed the number '{random_num}' correctly.")


guess(5)
