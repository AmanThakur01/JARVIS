def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)# here function is again cclled

result = fact(5)
print(result)