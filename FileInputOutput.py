# FileInputOutput


def fileInputOutput():
    my_name = input()
    filename = "names.txt"
    data = "whatever - acts as placeholder"

    f_read = open(filename, "r")  # r = read

    data = f_read.read()
    print("List of the names which have been saved:")
    print(data)

    if my_name in data:
        print("Welcome back, " + my_name + "! Nice to hear from you again!")
    else:
        print("Hello, newbie!")
        with open(filename, "w") as f:
            f.write(data)
            f.write(my_name + "\n")
            f_read = open(filename, "r")
            data = f_read.read()

    return my_name






