def readFile(filename):
    try:
        file = open(filename, "r")
    except OSError:
        print("error")


readFile("non_existing")