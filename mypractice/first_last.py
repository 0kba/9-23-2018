a = [5, 10, 15, 20, 25]


def first_last(list):

    length = len(list)
    result_list = []
    for num in list:
        if num == list[0]:
            result_list.append(num)
        elif num == list[length-1]:
            result_list.append(num)
    return result_list

print(first_last(a))