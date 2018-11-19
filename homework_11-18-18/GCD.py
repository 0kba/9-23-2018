import sys

def GCD(first_number, second_number):
    if first_number >= second_number  :
        return GCD_algorithm(first_number, second_number)
    elif second_number > first_number :                                      # if number2 greater than number1
        return GCD_algorithm(second_number, first_number)                     # switch positions in the algorithm

def GCD_algorithm(first_number, second_number):
    while second_number!=0:
        division = first_number / second_number
        remainder = first_number % second_number
        first_number = second_number
        second_number = remainder
    if first_number== 0:
        return print("you can't have both of numbers 0")
    return first_number

def main():
    if 3 < len(sys.argv) < 3:
        print("Pass just two numbers separated by space to get their GCD")
        return
    try:
        first_number = int(sys.argv[1])
        second_number = int(sys.argv[2])
        return print(GCD(first_number,second_number))

    except ValueError:
        print(f"one or both of ur numbers are not valid numbers", file=sys.stderr)
        return

# __________________________________________TEST CASES_____________________________________________
# C:\python\homework_11-18-18>GCD.py 270 192
# 6
#
# C:\python\homework_11-18-18>GCD.py -23 323
# -1
#
# C:\python\homework_11-18-18>GCD.py 270 uye
# one or both of ur numbers are not valid numbers
#
# C:\python\homework_11-18-18>GCD.py 270,873
# one or both of ur numbers are not valid numbers
# C:python\homework_11-18-18>GCD.py 0 0
# 0
#
# C:python\homework_11-18-18>GCD.py 0 987
# 987
#
# C:python\homework_11-18-18>GCD.py 654 0
# 654

if __name__ == '__main__':
    main()
