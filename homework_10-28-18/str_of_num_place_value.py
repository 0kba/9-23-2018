import sys

def positive_place_value(num):
    place_value = 1
    zero = ''
    for digit in reversed(num):
        print(f"place value ({place_value}) is : '{digit+zero}'")
        zero += '0'                              # zero variable is adding one more 0 to each digit
        place_value *= 10


def minus_place_value(num):
    place_value = 1
    zero = ''
    for digit in reversed(num):
        if digit != "-":                                                   # if the first digit is - that means number is minus
            print(f"place value ({place_value}) is : '-{digit+zero}'")     # add a minus before every digit
            zero += '0'
            place_value *= 10

def __main__():
    if len(sys.argv) < 2:
        print("Pass a string a number to this program to get the place value of each number")
        return
    try:
        userInput = str(sys.argv[1])
        if userInput.isnumeric():
            positive_place_value(userInput)
        elif userInput[0] == "-":
            minus_place_value(userInput)
        else:
            print(f"{userInput} is not a number.", file=sys.stderr)

    except ValueError:
        print(f"{userInput} is not a valid entry", file=sys.stderr)
        return

    except RecursionError:
        print(f"{userInput} is a lot of numbers please try less numbers", file=sys.stderr)
        return



__main__()





