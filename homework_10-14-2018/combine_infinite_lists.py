
def combine_infinite_lists (list_of_infinite_lists):

    combined_list = []

    for item in list_of_infinite_lists:

        if type(combined_list) == type(item):                 # if it is a list go to the next line

            for list in item:                                 # iterate over that particular list

                if type(combined_list) == type(list):
                    list_of_infinite_lists.append(list)              # if it is a list take it and add it to our main list

                else: combined_list.append(list)

        else: combined_list.append(item)

    return combined_list



list_of_infinite_lists = [[[[[[[1,7]]],[[[[[[2,3]]]]]]]]]]
printable_list =combine_infinite_lists(list_of_infinite_lists)



strings_and_lists =[[[1,2],[None],None,[3,4]],[[3,4],["hello","there"]]]
printable_string_list = combine_infinite_lists(strings_and_lists)



print(printable_list)
print(printable_string_list)

# ________________________________________________________________________________
# result
# [1, 7, 2, 3]
# [None, 1, 2, None, 3, 4, 3, 4, 'hello', 'there']
