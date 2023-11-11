#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'Hello World' in the console 
# print("Hello World")

# create a rock, paper and scissors game that is displayed on the console, you must give the player two options, one to restart the game and continue 
# playing and another to end the game, if you enter an invalid option you must mention it and ask the player to enter a valid option
# add a marker where the score is seen, it must be updated every time the player wins or loses, when the player loses the game must 
# end and display the score
import random
import sys

print("Welcome to Rock, Paper, Scissors!")

computerScore = 0
userScore = 0
rounds = 0

while True:
    print("Pick your weapon!")
    userChoice = input("Rock, Paper or Scissors? \n")

    choices = ["Rock", "Paper", "Scissors"]

    computerChoice = random.choice(choices)

    if userChoice == computerChoice:
        print("It's a Tie!")
        rounds += 1
    elif userChoice == "Rock":
        rounds += 1
        if computerChoice == "Paper":
            print("You lose!", computerChoice, "covers", userChoice)
            computerScore += 1
        else:
            print("You win!", userChoice, "smashes", computerChoice)
            userScore += 1
    elif userChoice == "Paper":
        rounds += 1
        if computerChoice == "Scissors":
            print("You lose!", computerChoice, "cut", userChoice)
            computerScore += 1
        else:
            print("You win!", userChoice, "covers", computerChoice)
            userScore += 1
    elif userChoice == "Scissors":
        rounds += 1
        if computerChoice == "Rock":
            print("You lose!", computerChoice, "smashes", userChoice)
            computerScore += 1
        else:
            print("You win!", userChoice, "cut", computerChoice)
            userScore += 1
    else:
        print("That's not a valid play. Check your spelling!")

    userChoice = input("Do you want to play again? (Y/N) \n")

    if userChoice == "N":
        print("User score: " + str(userScore))
        print("Computer score: " + str(computerScore))
        print("Rounds played: " + str(rounds))
        sys.exit()
    elif userChoice == "Y":
        continue
    else:
        print("I don't understand, try again.")