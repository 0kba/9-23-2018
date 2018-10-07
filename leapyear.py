
# **********that was my source*********
# How to determine whether a year is a leap year
# To determine whether a year is a leap year, follow these steps:
# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# The year is a leap year (it has 366 days).
# The year is not a leap year (it has 365 days).

def leapyear (num):

    leap = f"{num} is a leap year."
    notleap = f"{num} isn't a leap year."
    if num %4 == 0 :
        if num % 100 == 0 :

            if num % 400 == 0 :
                return leap
            else: return notleap
        else: return leap
    else: return notleap


print(leapyear(2019))

# ___________________________________________
# result 2019 isn't a leap year.