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

def askDifficulty(my_name):
    print("Well, " + my_name + ", which difficulty do you want? easy, normal or difficult?")

    guesses_available = 0     # specificy this! start with a default value!
    difficulty_taken = "easy"   # then I need a difficulty_taken default! So I declare that I use these two values locally in this function.
    
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

    return guesses_available    #if with brackets []: used for Array (Liste), beginning from 0, 1, 2 etc.

    #   print(askDifficulty()) to check if this function works or not..
    #   return None


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

