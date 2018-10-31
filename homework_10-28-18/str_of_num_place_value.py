import sys


def convert_str_to_int(num):
    str_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # every index in this list number of string is equal to the position in the list
    place_value = 1
    final_int = 0
    sign = 1
    if num[0] == "-":
        sign = -1
        num = num[1:]
    for digit in reversed(num):
        if digit in str_list:
            final_int += str_list.index(digit)*place_value
            place_value *= 10
        else:
            raise ValueError("{} is not a valid digit.".format(digit))

    return  final_int * sign



def __main__():
    if len(sys.argv) < 2:
        print("Pass a string a number to this program to get the place value of each number")
        return
    try:
        userInput = str(sys.argv[1])
        if userInput is not None:
            final = convert_str_to_int(userInput)
            print(final, file=sys.stdout)
            # print(type(final))
        else:
            print(f"{userInput} is not a number.", file=sys.stderr)

    except ValueError:
        print("an exception occurred", file=sys.stderr)
        return

#___________________________________________________________________
# test cases results
# str_of_num_place_value.py 987
# place value (1) is : 7
# place value (10) is : 80
# place value (100) is : 900

# -987
# place value (1) is : -7
# place value (10) is : -80
# place value (100) is : -900

# str_of_num_place_value.py lkj
# lkj is not a number.



__main__()








