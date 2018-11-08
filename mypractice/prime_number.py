number = input("please enter a number to check if it is a prime or not")

def prime_number(number):
    number = int(number)
    if number == 2 or number ==3:
        return "prime number"
    elif number ==1 or number%2 == 0 or number%3 == 0:
        return "not a prime number"
    else:
        return "prime number"


print(prime_number(number))