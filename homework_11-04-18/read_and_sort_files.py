from operator import itemgetter as it
import sys

def read_and_sort_files (file, LastName):
    file = open(file, "r")
    line = file.readline()  # skipping the first line by reading it
    list = []
    item = ""

    for lines in file:  # iterate over all the lines
        item = read_each_line(item, lines, list)

    list.append(item)  # now we have all items in the file in a list

    final = fil_list_to_dic(list)

    final.sort(key=it(LastName))  # print the whole list of dic(of students) sorted by the key gaven
    return final




def read_each_line(item, lines, list):
    for char in lines:  # iterate over each character in the line

        if char == "," or char == "\n":  # if you found "," or "\n"(end of the line)
            list.append(item)  # append the variable item to the list
            item = ""  # then reset it to empty
        else:
            item = item + char  # add every character in the variable "item"
    return item

def fil_list_to_dic(list):
    final = []
    while len(list) >= 3:
        final.append({"FirstName": list[0], "LastName": list[1], "DateOfBirth": f"{list[2]}"})
        # we created a dictionary to capture every item in where it should be
        # then append it to a list

        del list[0:3]  # delete the first 4 items so we can move to the next line
    return final





def main():
    if len(sys.argv) < 3:
        print("Pass a file name and a sorting key for example (student_data.txt FirstName)")
        return
    try:
        userInput1 = sys.argv[1]    # the file name
        userInput2 = sys.argv[2]    # sorting key
        print( read_and_sort_files(userInput1,userInput2))

    except KeyError:
        print(f"{userInput2} is not a valid Entry the key has to be written in one of those ways(FirstName,LastName or DateOfBirth)", file=sys.stderr)
        return
    except FileNotFoundError:
        print(f"{userInput1} doesn't exist please try a different file", file=sys.stderr)
        return

#_______________________________RESULTS______________________________________
# C:\Users\naweh\python\homework_11-04-18>read_and_sort_files.py student_data.txt LastName
# [{'FirstName': 'Juha', 'LastName': 'Abdo', 'DateOfBirth': '8/1/200'},
#  {'FirstName': 'Magas', 'LastName': 'Kisra', 'DateOfBirth': '7/2/1999'},
#  {'FirstName': 'Ali', 'LastName': 'Saleh', 'DateOfBirth': '5/5/2005'},
#  {'FirstName': 'Manal', 'LastName': 'Saleh', 'DateOfBirth': '5/9/2004'}]

#___________________

# C:\Users\naweh\python\homework_11-04-18>read_and_sort_files.py
# Pass a file name and a sorting key for example (student_data.txt FirstName)

#_____________________

#C:\Users\naweh\python\homework_11-04-18>read_and_sort_files.py student_data.txt kfj43
# kfj43 is not a valid Entry the key has to be written in one of those ways(FirstName,LastName or DateOfBirth)

#____________________

# C:\Users\naweh\python\homework_11-04-18>read_and_sort_files.py dkjhd87 LastName
# dkjhd87 doesn't exist please try a different file




if __name__ == '__main__':
    main()


