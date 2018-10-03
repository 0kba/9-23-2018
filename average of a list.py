list = [1,2,3,4,5,6]

def average (list):
    leng = len(list)
    sum = 0
    for a in list:
        sum =sum +a
    result = sum / leng
    return result

print(average(list))

# _______________________________
# result is
# 3.5