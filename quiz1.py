# Author: CRS 10/19/21
m = int(input("Please input the month."))
q = int(input("Please input the day of the month."))
year = int(input("Please input the year."))
k = year % 100
j = year // 100
h = (q + ((26 * (m + 1)) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7
if m == 13:
    year = year - 1
elif m == 14:
    year = year - 1
if h == 0:
    print("The day was Saturday")
elif h == 1:
    print("The day was Sunday")
elif h == 2:
    print("The day was Monday")
elif h == 3:
    print("The day was Tuesday")
elif h == 4:
    print("The day was Wednesday")
elif h == 5:
    print("The day was Thursday")
elif h == 6:
    print("The day was Friday")
