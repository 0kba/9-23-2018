
string = input("please write a statment")
string2 = string.lower()


vowels = {"a" : 0 , "e" : 0 , "i" : 0 ,  "o" : 0 , "u" : 0}
vowelslist = []

for char in string2:
    if char in vowels:
        vowelslist.append(char)  # putting all the vowels in a list

if len(vowelslist) == 0:
    print(f"The text: '{string}' has no vowels found.")
elif len(vowelslist) % 2 == 0:
    print(f"The text: '{string}' has an even number of vowels")    # the three ifs lines are for measuring the length of the vowels only list
elif len(vowelslist) % 2 != 0:
    print(f"The text: '{string}' has an odd number of vowels")

for vowel in vowelslist:
    if vowel in vowels:
        vowels [vowel] += 1               #counting how many we have of each vowel

for vo in vowels:
    if vowels [vo] != 0:                   # making sure we have the vowel before print it
     print(vo , vowels[vo])




# results
#  ______________________________________________________
# please write a statment this is a test
# The text: 'thIs Is A test' has an even number of vowels
# a 1
# e 1
# i 2
# __________________
# The text: 'we love programming' has an even number of vowels
# a 1
# i 1
# e 2
# o 2
# ___________________
# please write a statmentaeiou is vowels characters
# The text: 'aeiou is vowels characters' has an odd number of vowels
# a 3
# i 2
# e 3
# o 2
# u 1
# __________________
# please write a statmentwalking is healthy for you
# The text: 'walking is healthy for you' has an even number of vowels
# a 2
# i 2
# e 1
# o 2
# u 1



