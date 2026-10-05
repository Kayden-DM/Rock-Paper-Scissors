✂️ Python Rock Paper Scissors Game
A simple command-line Rock Paper Scissors game built with Python. Players compete against the computer, with the score changing based on wins and losses. It's a great beginner project for learning about loops, conditionals, random selection, and score tracking in Python.

📖 Python Rock Paper Scissors Game
The Python Rock Paper Scissors Game is a console-based game where the player faces off against the computer. Each round, the player enters their choice — rock, paper, or scissors — and the computer randomly picks one of the three.

The score starts at 0 and changes based on the outcome:

Win → +1 point

Lose → −1 point

Tie → no change

The game continues indefinitely until either the player reaches +2 (win) or −2 (lose). Invalid inputs are ignored, and the player is prompted to try again. All input is case-insensitive and whitespace is trimmed.

This project is ideal for anyone learning the fundamentals of Python — especially loops, conditionals, and randomization.

✨ Features
Three choices – Rock, paper, or scissors.

Random computer choice – Generated using random.choice().

Case-insensitive input – Accepts uppercase, lowercase, and mixed case.

Whitespace trimming – Ignores extra spaces around the input.

Input validation – Rejects any choice outside rock, paper, or scissors.

Score tracking – Wins add 1 point; losses subtract 1 point; ties don't affect the score.

Win condition – Reach +2 points to win the game.

Lose condition – Reach −2 points to lose the game.

Automatic game over – Ends immediately when either condition is met.

Displayed score – Shows the updated score after every round.

🛠️ What It Uses
Language & Library
Python 3

random – Python's built-in module for random choice selection.

Key Variables
Variable	Purpose
score	Tracks the player's current score (starts at 0).
pc	The player's chosen move.
c	The computer's randomly chosen move.
Python Concepts Demonstrated
The random module – Using random.choice() to pick the computer's move.

while True loops – The main game loop.

Conditional logic – Comparing the player's and computer's choices.

if/elif chains – Handling each possible outcome.

continue statement – Skips the rest of the loop on invalid input.

List membership – Checking pc not in ["rock", "paper", "scissors"].

String methods – .lower() and .strip() for clean input.

Score arithmetic – Using += and -= to update the score.

Multiple if statements – Separate checks for tie, win, and lose conditions.

Built-in Functions Used
input() – Reads the player's choice from the console.

print() – Displays choices, results, and the current score.

random.choice() – Selects a random move for the computer.

exit() – Ends the game when a win or lose condition is reached.

📥 Download
You can download the source file from this repository and save it as a .py file:

text
rock_paper_scissors.py
No installation or dependencies are needed — just Python.

▶️ How to Run
Make sure you have Python 3 installed (python.org).

Save the code as rock_paper_scissors.py.

Open a terminal or command prompt in the folder containing the file.

Run:

bash
python rock_paper_scissors.py
Type rock, paper, or scissors to play. Reach +2 to win, or avoid hitting −2 to keep playing!

🐍 Made with Python
This project is written entirely in Python 3 using only the standard library. It's a fun and classic example of how loops, conditionals, and randomization can be combined to build a small game.

Whether you're a beginner practicing control flow or someone who just enjoys quick games, this project is a great starting point.

💡 Possible Future Improvements
Add a "quit" option so the player doesn't have to force-exit.

Use elif instead of multiple ifs to avoid the tie condition overlapping with win/lose checks.

Adjustable win/lose score – Let the player pick how many points are needed.

Best-of-N mode – Play a fixed number of rounds and declare a winner at the end.

Track history – Show a running list of past rounds.

Add difficulty levels – Give the computer weighted choices for harder play.

Add a visual countdown before the computer reveals its choice.

Build a Tkinter GUI version for a graphical interface.

📄 License
This project is free to use, modify, and distribute for personal or educational purposes.

