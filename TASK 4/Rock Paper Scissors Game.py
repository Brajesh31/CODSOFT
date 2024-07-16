import tkinter as tk
import random

def determine_winner(player_choice, computer_choice):
    """Determines the winner between player and computer."""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game(player_choice):
    """Handles the game logic when player makes a choice."""
    computer_choice = random.choice(options)
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Initialize tkinter
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Color theme
root.configure(bg="#f0f0f0")  # Light gray background

# Available options
options = ["rock", "paper", "scissors"]

# Create labels and buttons with increased sizes
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 24), bg="#3498db", fg="#ffffff")
title_label.pack(pady=30)

button_frame = tk.Frame(root, bg="#f0f0f0")  # Match background color
button_frame.pack(pady=30)

button_specs = {"width": 15, "height": 3, "padx": 15, "bg": "#2980b9", "fg": "#ffffff", "font": ("Helvetica", 14)}

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game("rock"), **button_specs)
rock_button.grid(row=0, column=0)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("paper"), **button_specs)
paper_button.grid(row=0, column=1)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game("scissors"), **button_specs)
scissors_button.grid(row=0, column=2)

result_label = tk.Label(root, text="", font=("Helvetica", 18), bg="#f0f0f0", fg="#333333")
result_label.pack()

# Start the tkinter main loop
root.mainloop()
