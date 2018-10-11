
string = input("please write a statment")


vowels = "a" + "e" + "i" + "o" + "u"
vowelslist = []

for char in string:
    if char in vowels:
        vowelslist.append(char)  # putting all the vowels in a list

if len(vowelslist) == 0:
    print(f"The text: '{string}' has no vowels found.")
elif len(vowelslist) % 2 == 0:
    print(f"The text: '{string}' has an even number of vowels")    # the three ifs lines are for measuring the length of the vowels only list
elif len(vowelslist) % 2 != 0:
    print(f"The text: '{string}' has an odd number of vowels")

counti = 0
counte = 0
counta = 0
counto = 0
countu = 0

for vowel in vowelslist:
    if vowel == "i":
        counti +=1
    if vowel == "a":
        counta +=1
    if vowel == "e":
        counte +=1
    if vowel == "o":
        counto +=1
    if vowel == "u":
        countu +=1                #counting how many we have on each vowels
if counta !=0:
 print("a",counta)
if counti != 0:
 print("i",counti)
if counte != 0:
 print("e",counte)
if counto != 0:
 print("o",counto)               # making sure the vowel in there before we print a count for it
if countu != 0:
 print("u",countu)




# results
#  ______________________________________________________
# please write a statment this is a test
# The text: 'this is a test' has an even number of vowels
# a 1
# i 2
# e 1
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



