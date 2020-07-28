# Drawing Functions
# the Drawing Functions are only used to draw function, not used to change values! They only display them.

def DrawWelcomeMessage():
    print("Hello! Welcome to my little game Guess my number! :) What's your name?")

def drawResultNotCorrect(guess, number):
    if guess < number:
        print("Your guess is too low.")
    if guess > number:
        print("Your guess it too high.")

def drawWinningMessage(my_name, guesses_taken, win_score, loose_score):
    print("Bravo, " + my_name + "! You guessed my number in " + str(guesses_taken) + " guesses!")
    print("You win " + str(win_score) + " times." "You loose " + str(loose_score) + " times.")

def drawLoosingMessage(my_name, number, win_score, loose_score):
    print("How bad, "+ my_name + ". The number I was thinking of was " + str(number) +".")
    print("You win " + str(win_score) + " times." "You loose " + str(loose_score) + " times.")  

def drawRemaining(guesses_available, guesses_taken):
    print("Now you have", guesses_available - guesses_taken , "guesses remaining.")


