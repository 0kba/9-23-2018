import sys

def break_down_money (userInput):
    result = {"$": 0, "25¢": 0, "10¢": 0, "5¢": 0, "¢": 0}

    result["$"] = int(userInput)                                 # that is the dollars
    result["¢"] = round((userInput - int(userInput)) * 100)      # that is all the cents

    while result["¢"] > 5:                                       # here we break the cents going
        if (result["¢"] - 25) >= 0:                              # count how many of the biggest (25¢)
            result["25¢"] = result["25¢"] + 1
            result["¢"] = (result["¢"] - 25)
        elif (result["¢"] - 10) >= 0:
            result["10¢"] = result["10¢"] + 1
            result["¢"] = (result["¢"] - 10)
        elif (result["¢"] - 5) >= 0:                             # to the smallest (5¢)
            result["5¢"] = result["5¢"] + 1
            result["¢"] = (result["¢"] - 5)                      # the leftover will be single cents

    for key, value in result.items():                            # if the value is zero no need to print it
        if value != 0:
            print(f"{key} x {value}")






def main():
    if len(sys.argv) < 2:
        print("Pass a number to this program")
        return
    try:
        userInput = sys.argv[1]
        if userInput.isalpha():
            print(f"{userInput} is not a number.", file=sys.stderr)

        else:
            print(break_down_money(float(userInput)))


    except ValueError:
        print(f"{userInput} is not a valid entry", file=sys.stderr)
        return


if __name__ == '__main__':
    main()

# ______________________________________TEST CASES RESULTS________________________________________

# python>draft.py 897.3
# $ x 897
# 25¢ x 1
# ¢ x 5
#
# python>draft.py -8789.494
# $ x -8789
# ¢ x -49
#
# python>draft.py fdfd
# fdfd is not a number.