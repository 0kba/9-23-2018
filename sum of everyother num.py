list = [11,12,2,3,4,5,6,7,8]

def sumofeveryother1 (list):
    listofeveryother = []
    sum = 0

    for i in range (len(list)):
        if i %2 ==0:
            listofeveryother.append(list[i])

    for a in listofeveryother:
        sum = sum +a
    return sum


print(sumofeveryother1(list))

# another soultion
# _______________________________________________________

def sumofeveryother2 (list):

    listofeveryother = list [::2]
    sum =0
    for num in listofeveryother:
        sum =sum +num
    return sum


print(sumofeveryother2(list))

# _________________________________
# result is
# 31
# 31