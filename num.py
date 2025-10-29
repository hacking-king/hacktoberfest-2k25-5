import random

def guessing_game():
    number = random.randint(1, 50)
    print("I'm thinking of a number between 1 and 50...")
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} tries.")
            break

guessing_game()
