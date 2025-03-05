import tkinter as tk
import random

# Initialize scores and round count
player_score = 0
ai_score = 0
draws = 0
rounds = 0

# List of choices
choices = ["rock", "paper", "scissors"]


# Function to handle player choice
def play(player_choice):
    global player_score, ai_score, draws, rounds

    ai_choice = random.choice(choices)

    # Determine the result
    if player_choice == ai_choice:
        result = "It's a Draw!"
        draws += 1
    elif (player_choice == "rock" and ai_choice == "scissors") or \
            (player_choice == "paper" and ai_choice == "rock") or \
            (player_choice == "scissors" and ai_choice == "paper"):
        result = "You Win!"
        player_score += 1
    else:
        result = "AI Wins!"
        ai_score += 1

    rounds += 1

    # Update labels
    ai_choice_label.config(text=f"AI Chose: {ai_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Player: {player_score} | AI: {ai_score} | Draws: {draws} | Rounds: {rounds}")


# Function to end the game
def end_game():
    root.quit()  # Closes the Tkinter window


# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create labels
title_label = tk.Label(root, text="Rock, Paper, Scissors Game", font=("Arial", 14))
title_label.pack()

ai_choice_label = tk.Label(root, text="AI Chose: ", font=("Arial", 12))
ai_choice_label.pack()

result_label = tk.Label(root, text="Make Your Move!", font=("Arial", 12))
result_label.pack()

score_label = tk.Label(root, text="Player: 0 | AI: 0 | Draws: 0 | Rounds: 0", font=("Arial", 12))
score_label.pack()

# Create buttons for game choices
btn_rock = tk.Button(root, text="Rock", font=("Arial", 12), command=lambda: play("rock"))
btn_rock.pack()

btn_paper = tk.Button(root, text="Paper", font=("Arial", 12), command=lambda: play("paper"))
btn_paper.pack()

btn_scissors = tk.Button(root, text="Scissors", font=("Arial", 12), command=lambda: play("scissors"))
btn_scissors.pack()

# Create Quit Game button
btn_quit = tk.Button(root, text="Quit Game", font=("Arial", 12), fg="white", bg="red", command=end_game)
btn_quit.pack()

# Run the application
root.mainloop()
