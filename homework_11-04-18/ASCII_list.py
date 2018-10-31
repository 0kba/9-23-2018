# that code doesn't give u a correct value it was a try would like to keep




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










