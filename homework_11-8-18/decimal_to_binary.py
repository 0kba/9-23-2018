number = 893
def decimal_to_binary(number):
    list_of_two_xx_decimal = []
    number_index = make_list_get_index(list_of_two_xx_decimal, number)
    list_of_two_xx_decimal = list_of_two_xx_decimal[:(number_index + 1)]
    produce_binary_from_list(list_of_two_xx_decimal, number)



def make_list_get_index(list_of_two_xx_decimal, number):
    breaking_compare = 0
    number_index = 0
    for decimal in range(number):
        two_xx_decimal = (2 ** decimal)
        breaking_compare = two_xx_decimal + breaking_compare
        list_of_two_xx_decimal.append(two_xx_decimal)
        if number in list_of_two_xx_decimal:
            number_index = list_of_two_xx_decimal.index(number)
            break
        elif breaking_compare > number * number:
            number_index = get_closest_index(list_of_two_xx_decimal, number, number_index)
    return number_index

def get_closest_index(list_of_two_xx_decimal, number, number_index):
    for two_xx_ in list_of_two_xx_decimal:
        index_of_this_item = list_of_two_xx_decimal.index(two_xx_)
        next_item = list_of_two_xx_decimal[index_of_this_item + 1]
        if two_xx_ < number < next_item:
            number_index = list_of_two_xx_decimal.index(two_xx_)
            break
    return number_index

def two_xx_to_binary(index_of_instance_number, list_of_two_xx_decimal, matching_number, number, result, two_xx_):
    if two_xx_ == number:
        matching_number = number
        result = '1' + result
    elif number != matching_number and (
            matching_number + list_of_two_xx_decimal[index_of_instance_number]) <= number and two_xx_ < number:
        matching_number = matching_number + two_xx_
        result = '1' + result
    else:
        result = '0' + result

def produce_binary_from_list(list_of_two_xx_decimal, number):
    for two_xx_ in reversed(list_of_two_xx_decimal):
        matching_number = 0
        result = ''
        index_of_instance_number = list_of_two_xx_decimal.index(two_xx_)
        two_xx_to_binary(index_of_instance_number, list_of_two_xx_decimal, matching_number, number, result, two_xx_)
    print(f"the binary of {number} is 0b{result[::-1]} = {bin(number)}")


print(decimal_to_binary(number))