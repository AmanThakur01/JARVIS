def top():
    a = 1
    while a <= 10:
        n = a*a
        yield n
        a += 1


x = top()   # yield store value in the form of array

for i in x:
    print(i)
