Rock, Paper, Scissors
A command-line Python game where the player faces the computer in rock-paper-scissors, scoring +1 for a win and -1 for a loss, ending at ±2.

Concepts Used
Random Module — random.choice() picks the computer's move.

Conditionals — if/elif chains compare the player and computer choices to decide outcomes.

While Loop — the game loops until the score reaches +2 or -2.

Features
Input Validation — rejects anything that isn't rock, paper, or scissors and re-prompts.

Score Tracking — wins add 1, losses subtract 1, ties change nothing.

Win/Loss Threshold — the game ends when the score hits +2 or -2.

Improvements
Fix the Tie Logic — the tie if is separate from the win/loss elif chain, so a tie can fall through and be checked again incorrectly; make it the first elif with a continue.

Simplify Win/Loss Checks — use a lookup dict like {"rock": "scissors", ...} instead of six near-identical branches.

Prevent Negative Play — a score can drop below -2 between checks if logic changes; use a while -2 < score < 2 loop instead of while True with exit().
