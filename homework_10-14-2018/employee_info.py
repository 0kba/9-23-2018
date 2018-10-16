
def writefromafile(filename):
    try:
        file = open(filename, "r")  # open and read the file in variable called " file "
        line = file.readline()  # skipping the first line by reading it


        list = []
        item = ""

        for lines in file:  # iterate over all the lines

            for char in lines:  # iterate over each character in the line

                if char == "," or char == "\n":  # if you found "," or "\n"(end of the line)
                    list.append(item)  # append the variable item to the list
                    item = ""  # then reset it to empty

                else:
                    item = item + char  # add every character in the variable "item"

        list.append(item)  # now we have all items in the file in a list
        if list == ['']:
            print("your file is empty.")   # if list didn't capture anything that means the file is empty

        while len(list) >= 4:  # once we have less than 4 items that means we are done

            result = {"EmployeeId": list[0], "FullName": f"{list[2]}, {list[1]}", "Salary": f"${list[3]}"}
            # we created a dictionary to capture every item in where it should be

            print(result)  # print it right after u do that

            del list[0:4]  # delete the first 4 items so we can move to the next line

    except OSError:

        print("Oops!  either you entered a wrong file name or the file doesn't exist.  Try again...")



writefromafile("employee-info.txt")

# ______________________________________________________
#   test results
#
#
# if writefromafile("employee-info.txt")
#     result
# {'EmployeeId': '1', 'FullName': 'Ali, Abdo', 'Salary': '$59533.54'}
# {'EmployeeId': '2', 'FullName': 'Ali, Leeema', 'Salary': '$509533.54'}
# {'EmployeeId': '3', 'FullName': 'hasan, mohamed', 'Salary': '$8376483'}
# {'EmployeeId': '4', 'FullName': 'ibrahim, ahmed', 'Salary': '$9839.4'}
#
#
# if writefromafile("jkfdjfhdk.txt")
# result
# Oops!  either you entered a wrong file name or the file doesn't exist.  Try again...


# if we tray an empty file
#     result
# your file is empty.
