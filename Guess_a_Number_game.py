import random

print("Hello! What's your name?")
myName = input()

def playGame():
    guessesTaken = 0

    def nb_of_guesses(guess):
        print("Now you have", 6 - guessesTaken , "guesses remaining.")

        
    number = random.randint(1, 20)
    print("Well," + myName + ", I am thinking of a number between 1 and 20.")

    while guessesTaken < 6:   
        for guessesTaken in range(6):  #do this 6 times
            print("Take a guess.")

            try: 
                guess = int(input())
                guessesTaken = guessesTaken + 1

            except ValueError:
                print("Don't try to fool me, you fool! Try again.")
                continue

            if guess < number:
                print("Your guess is too low.")

            if guess > number:
                print("Your guess it too high.")

            nb_of_guesses(guess)

            if guess == number:
                break


        if guess == number:
            guessesTaken = str(guessesTaken)
            print("Bravo, " + myName + "! You guessed my number in " + guessesTaken + " guesses!")
            break

        else:
        # if guess != number:
            number = str(number)
            print("How bad, "+ myName + ". The number I was thinking of was " + number +".")

playGame()

while True:
    a = input("Continue?" "(y/n)")
    if a =="y":
        playGame()
        
    elif a=="n":
        print("No? Well, ok then. Bye, " + myName + "!")
        break
    
    else:
        print("Ummm.... Enter either y/n, you fool!")
    