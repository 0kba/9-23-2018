import sys


# 1- learn how to use a function inside a function (study recursive)
# 2- git checkout to discard a changes u did to a code u have on the desktop
# 3- home work is recursive don't worry about multi dimenstional and compare the first item is enough


# fib(1) = 1
# fib(2) = 1
# 2358
#
# fib(n) = fib(n-1) + fib(n - 2)

def fib(n):
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


def __main__():
    if len(sys.argv) < 2:
        print("Pass a number to this program to get the fibonacci value.")
        return
    try:
        userInput = str(sys.argv[1])
        if userInput.isnumeric():
            number = int(sys.argv[1])
            fib_value = fib(number)
            print(f"The fibonacci value for {number} is {fib_value}")
        else:
            print(f"{userInput} is not a number.", file=sys.stderr)

    except ValueError:
        print(f"{userInput} is not a valid entry", file=sys.stderr)
        return


__main__()
