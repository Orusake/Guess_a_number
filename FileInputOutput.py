# FileInputOutput


def fileInputOutput():
    my_name = input()
    filename = "names.txt"

    f_read = open(filename, "r")  # r = read
    playernames = f_read.read()

    print("List of the names which have been saved:")
    print(playernames)

    if my_name in playernames:
        print("Welcome back, " + my_name + "! Nice to hear from you again!")
    else:
        print("Hello, newbie!")
        with open(filename, "a") as f:  # a = append
            # f.write(playernames) don't need to write that anymore.
            f.write(my_name + "\n")
            f_read = open(filename, "r")

    return my_name






