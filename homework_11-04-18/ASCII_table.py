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
    print(f"Decimal ({char}) is hex {decimal_to_hex_decimal(char)} and Keyboard Entry is ({chr(char)}) ")


# __________________TEST CASES RESULTS______________________________________
# Decimal (0) is hex 00 and Keyboard Entry is ( )
# Decimal (1) is hex 01 and Keyboard Entry is ()
# Decimal (2) is hex 02 and Keyboard Entry is ()
# Decimal (3) is hex 03 and Keyboard Entry is ()
# Decimal (4) is hex 04 and Keyboard Entry is ()
# .etc
# Decimal (120) is hex 78 and Keyboard Entry is (x)
# Decimal (121) is hex 79 and Keyboard Entry is (y)
# Decimal (122) is hex 7A and Keyboard Entry is (z)
# Decimal (123) is hex 7B and Keyboard Entry is ({)
# Decimal (124) is hex 7C and Keyboard Entry is (|)
# Decimal (125) is hex 7D and Keyboard Entry is (})
# Decimal (126) is hex 7E and Keyboard Entry is (~)
# Decimal (127) is hex 7F and Keyboard Entry is ()