import random
import sys

# Functions


def playGame():
    guessesTaken = 0

    global win_score
    global loose_score

    print("Well," + myName + ", which difficulty do you want? easy, normal or difficult?")
    
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

    def remaining(guess):
        print("Now you have", guesses_available - guessesTaken , "guesses remaining.")

    number = random.randint(1, 20)
    print("OK," + myName + ", I am thinking of a number between 1 and 20.")


    while guessesTaken < guesses_available: 

        for guessesTaken in range(guesses_available):  #do this 6 times
            print("Take a guess.")

            try: 
                guess = int(input())
                guessesTaken = guessesTaken + 1
                
                if guess < number:
                    print("Your guess is too low.")
    
                if guess > number:
                    print("Your guess it too high.")
    
                remaining(guess)
                
                if guess == number:
                    break

            except ValueError:
                if guessesTaken < guesses_available - 1:
                   print("Don't try to fool me, you fool! Try again.")
                   continue
                else:
                    print("You are so mean to me! :( I don't want to play with you anymore! Bye!") 
                    sys.exit()



        if guess == number:
            guessesTaken = str(guessesTaken)
            print("Bravo, " + myName + "! You guessed my number in " + guessesTaken + " guesses!")
            win_score = win_score + 1
            print("You win " + str(win_score) + " times." "You loose " + str(loose_score) + " times.")
            break 

        else:
        # if guess != number:
            number = str(number)
            print("How bad, "+ myName + ". The number I was thinking of was " + number +".")
            loose_score += 1            #instead of loose_score = loose_score + 1
            # loose_score = str(loose_score)
            print("You win " + str(win_score) + " times." "You loose " + str(loose_score) + " times.")   

def Ask_continue():
    while True:
        a = input("Continue?" "(y/n)")
        if a =="y":
            playGame()
            
        elif a=="n":
            print("No? Well, ok then. Bye, " + myName + "!")    
            break
        
        else:
            print("Ummm.... Enter either y/n, you fool!")

# Program:

win_score = 0
loose_score = 0 

print("Hello! Welcome to my little game Guess my number! :) What's your name?")
myName = input()
            
playGame()

Ask_continue()


    


# score = {
#        'H': {
#                'wins' : 0,
#                'losses': 0,
#                'score': 0
#                },
