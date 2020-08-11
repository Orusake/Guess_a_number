# Drawing Functions
# the Drawing Functions are only used to draw function, not used to change values! They only display them.


# Add colors
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'  # red
    ENDC = '\033[0m'   # stop the color
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def drawWelcomeMessage():
    print("Hello! Welcome to my little game Guess my number! :) What's your name?")




def drawRemaining(guesses_available, guesses_taken):
    print("Now you have", guesses_available - guesses_taken , "guesses remaining.")

def drawResultNotCorrect(guess, number):
    if guess < number:
        print(bcolors.FAIL + "Your guess is too low." + bcolors.ENDC)
    if guess > number:
        print(bcolors.FAIL + "Your guess is too high." + bcolors.ENDC)

def drawWinningMessage(my_name, guesses_taken, win_score, loose_score):
    print(bcolors.OKGREEN + "Bravo, " + my_name + "! You guessed my number in " + str(guesses_taken) + " guesses!" + bcolors.ENDC)
    print("You win " + str(win_score) + " times." "You loose " + str(loose_score) + " times.")

def drawLoosingMessage(my_name, number, win_score, loose_score):
    print(bcolors.OKBLUE + "How bad, "+ my_name + ". The number I was thinking of was " + str(number) +"." + bcolors.ENDC)
    print("You win " + str(win_score) + " times." "You loose " + str(loose_score) + " times.")  


def drawLine(length):
    print("-" * length)

def drawSadEmoji():
    print(bcolors.OKGREEN + "(T.T) No? OK..." + bcolors.ENDC)

def drawHappyEmoji():
    print(bcolors.OKGREEN + "\(^0^)/ Great!" + bcolors.ENDC)

