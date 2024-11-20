# Importing the random module to generate a random number
import random

# Generating a random integer between 1 and 50, and initializing the attempt counter
num = random.randint(1, 50)
count = 0

# Informing the player of the rules of the game
print(
    "Guess a number between 1 and 50. I will reply with either 'too high' or 'too low'. To end the game early, type -1.")

# Starting the game loop, allowing up to 5 attempts
while count < 5:
    # Prompting the player for their guess, showing the current attempt number
    guess = int(input(f"Attempt {count + 1}: "))

    # If the player chooses to end the game early
    if guess == -1:
        print("You ended the game early. Goodbye!")
        break

    # Incrementing the attempt count
    count += 1

    # Providing feedback on whether the guess is too low, too high, or correct
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    else:
        # If the guess is correct, congratulating the player and ending the game
        print(f"Correct! You guessed the number in {count} attempts.")
        break
else:
    # If the player uses all 5 attempts without guessing correctly
    print(f"Sorry! You've used all 5 attempts. The number was {num}.")

