import sys

def GCD(first_number, second_number):
    if first_number >= second_number :
        return GCD_algorithm(first_number, second_number)
    elif second_number > first_number :                                      # if number2 greater than number1
        return GCD_algorithm(second_number, first_number)                     # switch positions in the algorithm

def GCD_algorithm(first_number, second_number):
    while second_number!=0:
        division = first_number / second_number
        remainder = first_number % second_number
        first_number = second_number
        second_number = remainder
    return first_number

def main():
    if len(sys.argv) < 3:
        print("Pass two numbers separated by space to get their GCD")
        return
    elif len(sys.argv) > 3:
        print("please enter just two numbers not more")
        return
    try:
        first_number = int(sys.argv[1])
        second_number = int(sys.argv[2])
        return print(GCD(first_number,second_number))

    except ValueError:
        print(f"one or both of ur numbers are not valid numbers", file=sys.stderr)
        return

if __name__ == '__main__':
    main()
