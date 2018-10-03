list = ["sample", "test", "test"]

def numofaword (list,word):
    list2 =[]
    for a in list:
       if word == a :
          list2.append(word)
    num = len(list2)
    return num
print(numofaword(list,"test"))

# ______________________________________
# result
# 2