def is_leap(year):
    leap = False


# The conditions of a year to be leap year
# 1. The year must be evenly divided by 4
# 2. if it evenly divided by 100,
#    it is not a leap year unless,
# 3. it also divided by 400


    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap

year = int(input())
print(is_leap(year))
    