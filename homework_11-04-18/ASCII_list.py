
def decimal_to_hex_numbers_only (decimal) :      # (1) function does the hex equation for numbers only .. doesn't include hex letters and produce list
    remainder_list = []
    place_value = 1                           # link to the source of the equation    https://www.permadi.com/tutorial/numDecToHex/
    while decimal != 0:
        remainder = decimal % 16
        decimal = int(decimal / 16)        # reset decimal to be the int only of the divison result so next loop will divide the result not the original decimal
        remainder = remainder * place_value
        place_value *= 10
        remainder_list.append(remainder)

    return sum_of_list(remainder_list)


def sum_of_list(remainder_list):             # (2) function adding all numbers inside the list together
    hex = 0
    for num in remainder_list:
        hex = num + hex
    return hex


def decimal_to_hex_letters (decimal) :       # (3) function returning hex letters

    letters = {"A": 0.625, "B": 0.6875, "C": 0.75, "D": 0.8125, "E": 0.875, "F": 0.9375}       # dividing decimal by 16 gives us
                                                     # integer number ( the number before the letter) and decimal number ( the value in the dictionary we created )
    for key, value in letters.items():
        if (decimal / 16) - int(decimal / 16) == value:
            return f"{int(decimal / 16)}{key}"


#________________________________________________________________________________________________________


def decimal_to_hex (decimal):                # (4) main function (for hex problem) to call the past three function to convert any decimal to hex

    positioner = (decimal / 16) - int(decimal / 16)    # positioner is a variable to check if the decimal will be
                                                       # in the range of the hex letters or not(hex numbers)
    if positioner >= 0.625 and positioner <= 0.9375 :

        return decimal_to_hex_letters(decimal)


    return decimal_to_hex_numbers_only (decimal)


for char in range(128):                     # (5) print the ASCII table and using the decimal to hex function to produce hex in the table
    print(f"Decimal ({char}) is hex {decimal_to_hex(char)} and Keyboard Entry is ({chr(char)}) ")

# __________________TEST CASES RESULTS______________________________________
# Decimal (0) is hex 0 and Keyboard Entry is ( )
# Decimal (1) is hex 1 and Keyboard Entry is ()
# Decimal (2) is hex 2 and Keyboard Entry is ()
# Decimal (3) is hex 3 and Keyboard Entry is ()
# Decimal (4) is hex 4 and Keyboard Entry is ()
# .etc
# Decimal (120) is hex 78 and Keyboard Entry is (x)
# Decimal (121) is hex 79 and Keyboard Entry is (y)
# Decimal (122) is hex 7A and Keyboard Entry is (z)
# Decimal (123) is hex 7B and Keyboard Entry is ({)
# Decimal (124) is hex 7C and Keyboard Entry is (|)
# Decimal (125) is hex 7D and Keyboard Entry is (})
# Decimal (126) is hex 7E and Keyboard Entry is (~)
# Decimal (127) is hex 7F and Keyboard Entry is ()







