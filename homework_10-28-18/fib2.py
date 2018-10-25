import sys

def fib2(num):
    list = []
    first_fib = 1                           # first two fibonacci numbers
    second_fib = 1
    for i in range(num):
        list.append(first_fib)             # **1**
        temp = first_fib                   # storing old first to a temporary variable so we can change the value without loosing it
        first_fib = second_fib             # the new first = the old second so we can move forward in the list (getting ready for next loop)
        second_fib = temp + second_fib     # making the new second = the old first (temp) + the old second (fibonacci equation)
                                           # then start over by number **1** and append it the first which became the value of old second
    return (list[num - 1])


def __main__():
    if len(sys.argv) < 2:
        print("Pass a number to this program to get the fibonacci value.")
        return
    try:
        userInput = str(sys.argv[1])
        if userInput.isnumeric():
            exec_fib(userInput)
        elif userInput[0] == "-":
            print(f"fibonacci can't be minus please try again...")
        else:
            print(f"{userInput} is not a number.", file=sys.stderr)

    except ValueError:
        print(f"{userInput} is not a valid entry", file=sys.stderr)
        return


def exec_fib(userInput):
    number = int(userInput)
    fib_value = fib2(number)
    print(f"The fibonacci value for {number} is {fib_value}", file=sys.stdout)

# ________________________________________________________________________
# test cases result
# The fibonacci value for 8 is 21
# The fibonacci value for 98 is 135301852344706746049
# -8   fibonacci can't be minus please try again...
# kljh is not a number.

__main__()








































































