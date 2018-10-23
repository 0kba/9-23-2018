
def combine_infinite_lists (main_list):

    result_list = []

    for item in main_list:

        if type(result_list) == type(item):                 # if it is a list go to the next line

            peel(result_list, item, main_list)

        else: result_list.append(item)

    return result_list


def peel(result_list, item, main_list):
    for list in item:  # iterate over that particular list

        if type(result_list) == type(list):
            main_list.append(list)  # if it is a list take it and add it to our main list

        else:
            result_list.append(list)


main_list = [[[[[[[1,7]]],[[[[[[2,3]]]]]]]]]]
printable_list =combine_infinite_lists(main_list)



strings_and_lists =[[[1,2],[None],None,[3,4]],[[3,4],["hello","there"]]]
printable_string_list = combine_infinite_lists(strings_and_lists)



print(printable_list)
print(printable_string_list)

# ________________________________________________________________________________
# result
# [1, 7, 2, 3]
# [None, 1, 2, None, 3, 4, 3, 4, 'hello', 'there']
