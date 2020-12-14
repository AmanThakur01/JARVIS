list1 = [1,2,3,4,5,6,7,8,9,0]
n = 9
pos = 1
i = 0
def search(list1,n):
    global i
    while i < len(list1):
        if i == n:
            return i
        i +=1
if search(list1,n):
    print("found at ",i)
else:
    print("not found")