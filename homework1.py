numbers = [3,5,10,9,45,23,90,7,98,89,32,54,65,76,87,12,21,11,22,33,44,55,66,77,88,99]

for num in numbers:

    if num%3 == 0:
        print(f" {num } is divisble by 3.")
    else:
        print(f" {num } isn't divisble by 3.")
    if num%5 == 0:
        print(f" {num } is divisble by 5.")
    else:
        print(f" {num } isn't divisble by 5.")
    if num%3 and num%5 > 0:
        print(f" {num } isn't divisble by 3 nor 5.")
