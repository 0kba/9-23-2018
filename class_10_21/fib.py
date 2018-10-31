import sys

# fib(1) = 1
# fib(2) = 1
# 2-3-5-8
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
            exec_fib(userInput)
        else:
            print(f"{userInput} is not a number.", file=sys.stderr)

    except ValueError:
        print(f"{userInput} is not a valid entry", file=sys.stderr)
        return
    
    except RecursionError:
        print(f"{userInput} is a lot of numbers please try less numbers", file=sys.stderr)
        return



def exec_fib(userInput):
    number = int(userInput)
    fib_value = fib(number)
    print(f"The fibonacci value for {number} is {fib_value}", file=sys.stdout)


__main__()
