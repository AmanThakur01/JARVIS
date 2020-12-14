num = [9,5,67,3,7]
def sort(num):
    for i in range(4):
        min = i
        print(i)
        for j in range(i,5):
            if num[j] < num[min]:
                min = j
        num[i],num[min]=num[min],num[i]


sort(num)
print(num)

