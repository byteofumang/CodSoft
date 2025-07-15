import random
import tkinter as tk
from tkinter import messagebox

choices = ['rock', 'paper', 'scissors']
symbols = {
    'rock': '✊',
    'paper': '✋',
    'scissors': '✌️'
}
button_colors = {
    'rock': '#A3CEF1',      # Light blue
    'paper': '#B6E2A1',     # Light green
    'scissors': '#F7B7A3'   # Light coral
}

class RockPaperScissorsGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock, Paper, Scissors")
        self.user_score = 0
        self.computer_score = 0

        self.label_title = tk.Label(master, text="Welcome to Rock, Paper, Scissors!", font=("Arial", 16))
        self.label_title.pack(pady=10)

        self.label_instruction = tk.Label(master, text="Choose rock, paper, or scissors to play.", font=("Arial", 12))
        self.label_instruction.pack(pady=5)

        self.frame_buttons = tk.Frame(master)
        self.frame_buttons.pack(pady=10)

        # Add buttons with colors and symbols
        self.btn_rock = tk.Button(
            self.frame_buttons, 
            text=f"{symbols['rock']} Rock", 
            width=12, 
            font=("Arial", 14, "bold"),
            bg=button_colors['rock'],
            activebackground="#7FB3D5",
            command=lambda: self.play('rock')
        )
        self.btn_rock.grid(row=0, column=0, padx=5)

        self.btn_paper = tk.Button(
            self.frame_buttons, 
            text=f"{symbols['paper']} Paper", 
            width=12, 
            font=("Arial", 14, "bold"),
            bg=button_colors['paper'],
            activebackground="#82C785",
            command=lambda: self.play('paper')
        )
        self.btn_paper.grid(row=0, column=1, padx=5)

        self.btn_scissors = tk.Button(
            self.frame_buttons, 
            text=f"{symbols['scissors']} Scissors", 
            width=12, 
            font=("Arial", 14, "bold"),
            bg=button_colors['scissors'],
            activebackground="#F1948A",
            command=lambda: self.play('scissors')
        )
        self.btn_scissors.grid(row=0, column=2, padx=5)

        self.label_user_choice = tk.Label(master, text="You chose: ", font=("Arial", 12))
        self.label_user_choice.pack(pady=2)

        self.label_computer = tk.Label(master, text="Computer chose: ", font=("Arial", 12))
        self.label_computer.pack(pady=2)

        self.label_result = tk.Label(master, text="", font=("Arial", 14, "bold"))
        self.label_result.pack(pady=5)

        self.label_score = tk.Label(master, text="Score => You: 0 | Computer: 0", font=("Arial", 12))
        self.label_score.pack(pady=10)

        self.btn_exit = tk.Button(master, text="Exit", width=10, command=self.exit_game, bg="#CCCCCC", font=("Arial", 12, "bold"))
        self.btn_exit.pack(pady=5)

        # Make buttons interactive: highlight on hover
        for btn in [self.btn_rock, self.btn_paper, self.btn_scissors]:
            btn.bind("<Enter>", self.on_enter)
            btn.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        event.widget.config(relief=tk.SUNKEN, bd=4)

    def on_leave(self, event):
        event.widget.config(relief=tk.RAISED, bd=2)

    def determine_winner(self, user, computer):
        if user == computer:
            return "tie"
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'scissors' and computer == 'paper') or \
             (user == 'paper' and computer == 'rock'):
            return "user"
        else:
            return "computer"

    def play(self, user_choice):
        computer_choice = random.choice(choices)
        # Show user and computer choices with symbols
        self.label_user_choice.config(
            text=f"You chose: {symbols[user_choice]} {user_choice.capitalize()}"
        )
        self.label_computer.config(
            text=f"Computer chose: {symbols[computer_choice]} {computer_choice.capitalize()}"
        )

        result = self.determine_winner(user_choice, computer_choice)

        if result == "tie":
            self.label_result.config(text="It's a tie!", fg="blue")
        elif result == "user":
            self.label_result.config(text="You win this round!", fg="green")
            self.user_score += 1
        else:
            self.label_result.config(text="Computer wins this round!", fg="red")
            self.computer_score += 1

        self.label_score.config(text=f"Score => You: {self.user_score} | Computer: {self.computer_score}")

    def exit_game(self):
        final_msg = f"Final Score:\nYou: {self.user_score} | Computer: {self.computer_score}\nThanks for playing!"
        messagebox.showinfo("Game Over", final_msg)
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()