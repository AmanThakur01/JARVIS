import random
import fstrings
lst = []
tab_input = int(input("Enter number for table : "))
table = 0
for i in range(10):
    varable = random.randrange(0,10)
    table = table + tab_input
    if varable==i:
        print(table + 1)
        lst.append(table + 1)
    else:
        print(table)
input("press key to check...")
for i in lst:
    print("This is wrong {}".format(i))