import random

# Display game instructions
print("This is a rock, paper, scissors game. To play, type 1 for ROCK, 2 for PAPER, or 3 for SCISSORS.")
print("If you want to see who is winning between the AI and you, type 2.")
print("To end the game and quit, type 'end_game'. (NOTE: Your progress will not be saved!)")

# List of possible choices for the game
choices = ["rock", "paper", "scissors"]

# Initialize scores and round count
Score1 = 0  # Player's score
Score2 = 0  # AI's score
Score3 = 0 # Number of draws
Round_count = 0  # Count of rounds played

# Game loop: keep playing until 'end_game' is chosen
while True:
    # Prompt user for input
    player_choice = input(
        "What do you want to pick? Type 1 for ROCK, 2 for PAPER, 3 for SCISSORS, or 'end_game' to quit: ")

    # End game condition if player chooses 'end_game'
    if player_choice == "end_game":
        print("Game Over!")
        break  # Exit the loop and end the game

    # Input validation: Ensure player choice is valid
    if player_choice not in ["1", "2", "3"]:
        print("Invalid input, please try again.")
        continue  # Ask for input again if invalid

    # Randomly choose the AI's move
    AI_choice = random.choice(choices)

    # Display both player and AI choices
    print(f"AI chose: {AI_choice}")
    print(f"You chose: {player_choice}")

    # Check for draw conditions
    if player_choice == "1" and AI_choice == "rock":
        print("This round was a Draw!")
        Score3 += 1
    elif player_choice == "2" and AI_choice == "paper":
        print("This round was a Draw!")
        Score3 += 1
    elif player_choice == "3" and AI_choice == "scissors":
        print("This round was a Draw!")
        Score3 += 1

    # Check for player wins
    elif player_choice == "1" and AI_choice == "scissors":
        print("Player 1 is the Winner!")
        Score1 += 1  # Update player score
    elif player_choice == "2" and AI_choice == "rock":
        print("Player 1 is the Winner!")
        Score1 += 1  # Update player score
    elif player_choice == "3" and AI_choice == "paper":
        print("Player 1 is the Winner!")
        Score1 += 1  # Update player score

    # If the player loses
    else:
        print("Player 1 is the Loser")
        Score2 += 1  # Update AI score

    # Increment round count after each round
    Round_count += 1

    # Display current game status
    print(f"Score: Player = {Score1}, AI = {Score2}, Draw = {Score3} Rounds played = {Round_count}")
