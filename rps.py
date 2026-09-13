import random
score = 0
while True:

    pc = input("Enter your choice: ")
    print("You chose:", pc)
    if pc not in ["rock", "paper", "scissors"]:
        print("Invalid choice")
        continue
    c = random.choice(["rock", "paper", "scissors"])
    print("Computer chose:", c)
    
    if pc == c:
        print("It's a tie! Your new score is:", score)
    if pc == "rock" and c == "scissors":
            score += 1
            print("You win! Your new score is:", score)
    elif pc == "paper" and c == "rock":
            score += 1
            print("You win! Your new score is:", score)
    elif pc == "scissors" and c == "paper":
            score += 1
            print("You win! Your new score is:", score)
    elif pc == "rock" and c == "paper":
            score -= 1
            print("You lose! Your new score is:", score)
    elif pc == "paper" and c == "scissors":
            score -= 1
            print("You lose! Your new score is:", score)
    elif pc == "scissors" and c == "rock":
            score -= 1
            print("You lose! Your new score is:", score)
    if score == 2:
        print("You win!")
        exit()
    elif score == -2:
        print("You lose!")
        exit()