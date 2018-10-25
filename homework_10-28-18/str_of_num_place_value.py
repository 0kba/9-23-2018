import sys


def positive_place_value(num):
    str_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']               # every index in this list number of string is equal to the position in the list
    place_value = 1
    for digit in reversed(num):
        if digit in str_list:
            print(f"place value ({place_value}) is : {str_list.index(digit)*place_value}")   #  instead of writting the digit or the number as a string
            place_value *= 10                                                                # we will write the position of it in the list which will be int type


def minus_place_value(num):
    str_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    place_value = 1

    for digit in reversed(num):
        if digit != "-" and digit in str_list:                                                   # if the first digit is - that means number is minus
            print(f"place value ({place_value}) is : -{str_list.index(digit)*place_value}")     # add a minus before every digit
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

#___________________________________________________________________
# test cases results
# str_of_num_place_value.py 987
# place value (1) is : '7'
# place value (10) is : '80'
# place value (100) is : '900'

# -987
# place value (1) is : '-7'
# place value (10) is : '-80'
# place value (100) is : '-900'

# str_of_num_place_value.py lkj
# lkj is not a number.






