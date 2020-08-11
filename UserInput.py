
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