import random
import sys

from Game_engine import drawWelcomeMessage
from Game_engine import askDifficulty
from Game_engine import drawRemaining
from Game_engine import drawResultNotCorrect
from Game_engine import drawWinningMessage
from Game_engine import drawLoosingMessage
from Game_engine import drawLine
from Game_engine import drawSadEmoji
from Game_engine import drawHappyEmoji



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

drawWelcomeMessage()
my_name = input()
            
playGame()

drawAskContinue(my_name)


    
