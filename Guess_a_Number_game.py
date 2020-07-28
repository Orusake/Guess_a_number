import random
import sys

from Game_engine import drawResultNotCorrect
from Game_engine import drawWinningMessage
from Game_engine import drawLoosingMessage
from Game_engine import drawRemaining
from Game_engine import DrawWelcomeMessage


def playGame():
    guesses_taken = 0

    global win_score
    global loose_score

    print("Well," + my_name + ", which difficulty do you want? easy, normal or difficult?")
    
    while True:
        difficulty_taken = input()

        if difficulty_taken == "easy":
            guesses_available = 10
            break
        if difficulty_taken == "normal":
            guesses_available = 6
            break
        if difficulty_taken == "difficult":
            guesses_available = 3
            break
        else:
            print("Please write easy, normal or difficult correctly.")

    print("You have chosen " + difficulty_taken + ". You will have", guesses_available ,"guesses.")

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
    while True:
        a = input("Continue?" "(y/n)")
        if a =="y":
            playGame()
            
        elif a=="n":
            print("No? Well, ok then. Bye, " + my_name + "!")    
            break
        
        else:
            print("Ummm.... Enter either y/n, you fool!")



# Program:

win_score = 0
loose_score = 0 

DrawWelcomeMessage()
my_name = input()
            
playGame()

drawAskContinue(my_name)


    
