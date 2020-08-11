import random
import sys

# from FileInputOutput import file_input_output

from GameEngine import drawWelcomeMessage
from GameEngine import askDifficulty
from GameEngine import drawRemaining
from GameEngine import drawResultNotCorrect
from GameEngine import drawWinningMessage
from GameEngine import drawLoosingMessage
from GameEngine import drawLine
from GameEngine import drawSadEmoji
from GameEngine import drawHappyEmoji



def playGame():
    guesses_taken = 0

    global win_score
    global loose_score
   
    guesses_available = askDifficulty(my_name)

    number = random.randint(1, 20)
    print("OK," + my_name + ", I am thinking of a number between 1 and 20.")


    while guesses_taken < guesses_available: 

        for guesses_taken in range(guesses_available):  #do this 6 times
            print("Take a guess.")

            try: 
                guess = int(input())
                guesses_taken = guesses_taken + 1
                
                drawResultNotCorrect(guess, number)
    
                drawRemaining(guesses_available, guesses_taken)
                
                if guess == number:
                    break

            except ValueError:
                if guesses_taken < guesses_available - 1:
                   print("Don't try to fool me, you fool! Try again.")
                   continue
                else:
                    print("You are so mean to me! :( I don't want to play with you anymore! Bye!") 
                    sys.exit()

        if guess == number:
            win_score = win_score + 1
            drawWinningMessage(my_name, guesses_taken, win_score, loose_score)
            break

        else:
            loose_score += 1            #instead of loose_score = loose_score + 1
            drawLoosingMessage(my_name, number, win_score, loose_score)
            


def drawAskContinue(my_name):
    drawLine(20)
    while True:
        a = input("Continue?" "(y/n)")
        if a =="y":
            drawHappyEmoji()
            playGame()
            
        elif a=="n":
            drawSadEmoji()
            print("Well, ok then. Bye, " + my_name + "!")    
            break
        
        else:
            print("Ummm.... Enter either y/n, you fool!")



# Program to play:


win_score = 0
loose_score = 0 

filename = "UserInput.py"
data = "Hang, Thomy, Ellie"

f = open(filename, "w")  # w = write

f.write(data + "\n")  # \n is a newline  \t is a tab
f.close()

f_read = open(filename, "r")  # r = read

data = f_read.read()
print("List of the names")
print(data)

drawWelcomeMessage()

my_name = input()

if my_name in data:
    print("Welcome back, " + my_name + "! Nice to hear from you again!")
else:
    print("Hello, newbie!")

playGame()

drawAskContinue(my_name)


    
