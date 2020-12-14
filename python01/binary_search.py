from sorting import *


n = int(input("number you want to search : "))
try:
    def search(n,l1):
        l = 0
        u = len(l1)
        while l<=u:
            mid = (l+u)//2
            if l1[mid]==n:
                print("found at ",mid)
                break
            else:
                if l1[mid]<n:
                    l=mid
                else:
                    u=mid
except :
    print("not in list ")
l1=[1,2,4,53,7]
search(n,l1)

