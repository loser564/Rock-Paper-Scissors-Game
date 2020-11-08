
from random import randint
t = ["Rock", "Paper", "Scissors"]
computer =t[randint(0,2)]
player = False
input()
while player == False:
    player = input("Rock, Paper, Scissors")
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!")
        else :
            print("You win!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!")
        else:
            print("You win!")