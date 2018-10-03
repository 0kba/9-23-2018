string = "this is a sample test."
def numofwords (string):
    a = " "
    list =[]
    for b in string :
        if a ==b:
            list.append(a)
    numwords = 1 + len(list)
    return numwords

print(numofwords(string))

# ______________________________________________________________
# result
# 5