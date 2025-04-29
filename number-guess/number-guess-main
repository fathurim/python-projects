import random

print("Welcome to the Number Guessing Project!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty level, type 'easy' or 'hard': ")
my_number = random.randint(1, 100)
if difficulty == "easy":
    attemp = 10
elif difficulty == "hard":
    attemp = 5

while attemp != 0:
    print(f"You have {attemp} attemps remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess < my_number:
        print("Your guess is too low.")
        attemp -= 1
    elif guess > my_number:
        print("Your guess is too high.")
        attemp -= 1
    else:
        print("You guessed it correctly!")
        break

    if guess != my_number and attemp == 0:
        print(f"You've run out of guesses, you lose. The number was {my_number}.")
        break
