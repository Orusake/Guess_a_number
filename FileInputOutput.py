# FileInputOutput


def fileInputOutput():
    filename = "names.txt"
    data = ""
    
    f = open(filename, "w")  # w = write

    f.write(data + "\n")  # \n is a newline  \t is a tab
    f.close()

    f_read = open(filename, "r")  # r = read

    data = f_read.read()
    print("List of the names which have been saved")
    print(data)

    return data






