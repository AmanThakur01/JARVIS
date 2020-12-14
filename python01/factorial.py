def facto(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f


result = facto(5)
print(result)
