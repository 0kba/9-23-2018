def decimal_to_hex (decimal):

    division_by_16 = decimal / 16
    num_before_letter = int(division_by_16)
    letter_definer = division_by_16 - num_before_letter
    letters = {"A": 0.625, "B": 0.6875, "C": 0.75, "D": 0.8125, "E": 0.875, "F": 0.9375}

    for key, value in letters.items():
        if letter_definer == value:
            return f"{num_before_letter}{key}"




    remainder_list = []
    while decimal != 0:
        remainder = decimal % 16
        decimal = int(decimal / 16)
        remainder_list.append(remainder)

    hex = 0
    place_value = 1
    for num in remainder_list:
        num = num * place_value
        place_value *= 10
        hex = num + hex

    return hex


for char in range(128):
    print(f"Decimal ({char}) is hex {decimal_to_hex(char)} and Keyboard Entry is ({chr(char)}) ")



