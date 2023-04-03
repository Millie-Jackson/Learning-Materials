player1 = "rock"
player2 = "lizzard"

if player1 != "rock" or player1 != "paper" or player1 != "scissors" or player2 != "rock" or player2 != "paper" or player2 != "scissors":
    print("Invalid Input")

if player1 == "rock" and player2 == "paper" or player1 == "paper" and player2 == "scissors" or player1 == "scissors" and player2 == "rock":
    winner = "Player 2"
    print("Player 2 wins")
elif player1 == "rock" and player2 == "rock" or player1 == "paper" and player2 == "paper" or player1 == "scisors" and player2 == "scissors":
    print("It's a tie")
else:
    winner = "Player 1"
    print("Player 1 wins")


