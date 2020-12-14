l1 = ["aman","vyabha","shubha"]
l2 = [18,19,22]
l3 = set(zip(l1,l2))   #alphabatically
print(l3)
l4 = list(zip(l1,l2))
print(l4)
for (a,b) in l4:
    print(a,b)