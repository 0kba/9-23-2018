
for char in range(401):
    print(f"Decimal: ({char})    hex: ({hex(char)})     Keyboard Entry: ({chr(char)}) ")


# results
# Decimal: (397)    hex: (0x18d)     Keyboard Entry: (ƍ)
# Decimal: (398)    hex: (0x18e)     Keyboard Entry: (Ǝ)
# Decimal: (399)    hex: (0x18f)     Keyboard Entry: (Ə)
# Decimal: (400)    hex: (0x190)     Keyboard Entry: (Ɛ)

# ________________________________IGNORE WHAT IS UNDER THIS LINE______________________________________
# ________________________________________________________________________________________________________
#
# def decimal_to_hex_decimal (decimal):
#     letters = {"0": 0 , "1": 0.0625 , "2": 0.125 , "3": 0.1875 , "4": 0.25 , "5": 0.3125 ,
#                "6": 0.375 , "7": 0.4375 , "8": 0.5 , "9": 0.5625 , "A": 0.625 , "B": 0.6875 ,
#                "C": 0.75 , "D": 0.8125 , "E": 0.875 , "F": 0.9375}                     # dividing decimal by 16 gives us
#                                                      # integer number ( the first number) and decimal number ( the value in the dictionary we created )
#                                                      # which will tell us which number or letter should we use.
#     for key, value in letters.items():
#         if (decimal / 16) - int(decimal / 16) == value:
#             return f"{hex(int(decimal / 16))}{key}"
#
#
# for char in range(401):                     # print the ASCII table and using the decimal to hexdecimal function to produce hex in the table
#     print(f"Decimal: ({char})    hex: ({decimal_to_hex_decimal(char)})     Keyboard Entry: ({chr(char)}) ")
#

________________________________________________________________________________


# def decimal_to_hex_numbers_only (decimal) :      # (1) function does the hex equation for numbers only .. doesn't include hex letters and produce list
#     remainder_list = []
#     place_value = 1                           # link to the source of the equation    https://www.permadi.com/tutorial/numDecToHex/
#     while decimal != 0:
#         remainder = decimal % 16
#         decimal = int(decimal / 16)        # reset decimal to be the int only of the divison result so next loop will divide the result not the original decimal
#         remainder = remainder * place_value
#         place_value *= 10
#         remainder_list.append(remainder)
#
#     return sum_of_list(remainder_list)
#
#
# def sum_of_list(remainder_list):             # (2) function adding all numbers inside the list together
#     hex = 0
#     for num in remainder_list:
#         hex = num + hex
#     return hex