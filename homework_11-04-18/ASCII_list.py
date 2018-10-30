
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


def sum_of_list(remainder_list):             # (2) function to take care of this list by adding all numbers inside the list together
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








