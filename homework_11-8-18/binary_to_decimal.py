def binary_to_decimal (binary):
    binary = str(binary)
    list_len = len(binary)
    list_two_to_the_power = []
    two_to_the_power_list(list_two_to_the_power, list_len)
    rev_binary = binary[::-1]
    decimal_result = 0
    decimal_result = result_out_of_list(list_two_to_the_power, rev_binary, decimal_result)
    print(F"decimal of {binary} is {decimal_result}")


def result_out_of_list(list_two_to_the_power, rev_binary, decimal_result):
    for n in list_two_to_the_power:
        if rev_binary[(list_two_to_the_power.index(n))] == '1':
            decimal_result = n + decimal_result
    return decimal_result


def two_to_the_power_list(list, list_len):
    for i in range(list_len):
        i = int(i)
        i = 2 ** i
        list.append(i)


binary = 0
print(binary_to_decimal(binary))

# ________________________________RESULT_____________________________________
# decimal of 10000 is 16
# decimal of 101101110 is 366
# decimal of 0 is 0