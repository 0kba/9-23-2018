
def reading_file_to_a_list(filename):

    try:
        file = open(filename, "r")
        line = file.readline()                    # skipping the first line by reading it
        list = []
        item = ""

        for lines in file:                        # iterate over all the lines
            item = divide_lines_to_words(item, lines, list)

        list.append(item)                         # now we have all items in the file in a list
        return list

    except OSError:
        return "Oops! the source file doesn't exist.  please try again..."           # handling error if the file doesn't exist


def divide_lines_to_words(item, lines, list):
    for char in lines:  # iterate over each character in the line

        if char == "," or char == "\n":  # if you found "," or "\n"(end of the line)
            list.append(item)  # append the variable item to the list
            item = ""  # then reset it to empty
        else:
            item = item + char  # add every character in the variable "item"
    return item

def fill_list_to_dic(list):
    while len(list) >= 4:
        result = {"Employee Id": list[0], "Full Name": f"{list[2]}, {list[1]}", "Salary": f"${list[3]}"}
        # we created a dictionary to capture every item in where it should be

        print(result)

        del list[0:4]  # delete the first 4 items so we can move to the next line


def handling_source_error (list):

    if list == "Oops! the source file doesn't exist.  please try again...":
        print("Oops! the source file doesn't exist.  please try again...")

    elif list != ['']:
        fill_list_to_dic(list)


    elif list == ['']:
        print("the source file is empty")





# __________________________________________________________________________________

list = reading_file_to_a_list("employee-info.txt")

result = handling_source_error(list)

print(result)

# ______________________________________________________
#   test results
#
#
# if writefromafile("employee-info.txt")
#     result
# {'Employee Id': '1', 'Full Name': 'Ali, Abdo', 'Salary': '$59533.54'}
# {'Employee Id': '2', 'Full Name': 'Ali, Leeema', 'Salary': '$509533.54'}
# {'Employee Id': '3', 'Full Name': 'hasan, mohamed', 'Salary': '$8376483'}
# {'Employee Id': '4', 'Full Name': 'ibrahim, ahmed', 'Salary': '$9839.4'}
# None
#
# if writefromafile("jkfdjfhdk.txt")
# result
# Oops! the source file doesn't exist.  please try again...


# if writefromafile("empty.txt")
#     result
# the source file is empty
