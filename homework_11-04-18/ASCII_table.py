
def decimal_to_hex_decimal (decimal):
    letters = {"0": 0 , "1": 0.0625 , "2": 0.125 , "3": 0.1875 , "4": 0.25 , "5": 0.3125 ,
               "6": 0.375 , "7": 0.4375 , "8": 0.5 , "9": 0.5625 , "A": 0.625 , "B": 0.6875 ,
               "C": 0.75 , "D": 0.8125 , "E": 0.875 , "F": 0.9375}                     # dividing decimal by 16 gives us
                                                     # integer number ( the first number) and decimal number ( the value in the dictionary we created )
                                                     # which will tell us which number or letter should we use.
    for key, value in letters.items():
        if (decimal / 16) - int(decimal / 16) == value:
            return f"{int(decimal / 16)}{key}"


for char in range(128):                     # print the ASCII table and using the decimal to hexdecimal function to produce hex in the table
    print(f"Decimal: ({char})    hex: ({decimal_to_hex_decimal(char)})     Keyboard Entry: ({chr(char)}) ")


# __________________TEST CASES RESULTS______________________________________
# Decimal: (0)    hex: (00)     Keyboard Entry: ( )
# Decimal: (1)    hex: (01)     Keyboard Entry: ()
# Decimal: (2)    hex: (02)     Keyboard Entry: ()
# Decimal: (3)    hex: (03)     Keyboard Entry: ()
# Decimal: (4)    hex: (04)     Keyboard Entry: ()
# .etc
# Decimal: (120)    hex: (78)     Keyboard Entry: (x)
# Decimal: (121)    hex: (79)     Keyboard Entry: (y)
# Decimal: (122)    hex: (7A)     Keyboard Entry: (z)
# Decimal: (123)    hex: (7B)     Keyboard Entry: ({)
# Decimal: (124)    hex: (7C)     Keyboard Entry: (|)
# Decimal: (125)    hex: (7D)     Keyboard Entry: (})
# Decimal: (126)    hex: (7E)     Keyboard Entry: (~)
# Decimal: (127)    hex: (7F)     Keyboard Entry: ()