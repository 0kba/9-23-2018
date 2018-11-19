numbers = [1,2,2,2,3,3,4,4,4,4,5,6,6,-1,0,1,2,5]
count=0
count1=0
count2=0
for num in numbers:
    if num == 2:
        count= count +1
print (f"number 2 appeared {count} times.")

for num in numbers:
    if num == 3:
        count1= count1 +1
print (f"number 3 appeared {count1} times.")

for num in numbers:
    if num == 4:
        count2= count2 +1
print (f"number 4 appeared {count2} times.")


# result______________________________________________________________
# number 2 appeared 4 times.
# number 3 appeared 2 times.
# number 4 appeared 4 times.
