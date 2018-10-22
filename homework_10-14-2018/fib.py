#   1- learn how to use a function inside a function (study recursive)
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


number = 5
result = fib(number)
print(result)
