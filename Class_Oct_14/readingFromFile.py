def readFile(filename):
    file = open(filename, "r")
    line = file.readline()
    someVar = None
    while True:
        print(line, end="")
        line = file.readline()
        if line == "":
            break

readFile("test.txt")
