import random

guessesTaken = 0

print("Hello! What's your name?")
myName = input()

number = random.randint(1, 20)
print("Well," + myName + ", I am thinking of a number between 1 and 20.")

for guessesTaken in range(6):  #do this 6 times
    print("Take a guess.")
    guess = input()
    guess = int(guess)
    
    if guess < number:
        print("Your guess is too low.")
        
    if guess > number:
        print("Your guess it too high.")
        
    if guess == number:
        break
        
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("Bravo, " + myName + "! You guessed my number in " + guessesTaken + " guesses!")
    
if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was" + number +".")