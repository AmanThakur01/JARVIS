from numpy import *
def sort(l1):
    for i in range(len(l1)-1,0,-1):
        pass
        for j in range(i):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1] = l1[j+1],l1[j]

#l1 = array([input("Enter list integers : ")])
l1 = [9,7,4,2]
sort(l1)
print(l1)



