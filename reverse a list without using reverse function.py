
def reverse(list):
    revlist = list [::-1]
    return revlist
print(reverse([21,23,43,545,65]))

# another soulution

def reverse(list):
    a = 0
    b = len(list)-1
    while a<b:
        list[a],list[b] = list[b],list[a]
        a = a + 1
        b = b - 1
    return list

list = [21,23,43,545,65]

print(reverse(list))


