def fib(n):
    if n > 0 or n == 1:
        a = 0
        print(a)
        if n > 1 or n == 2:
            b = 1
            print(b)
            if n > 2:
                for i in range(3, n+1):
                    c = a+b
                    a = b
                    b = c
                    print(c)
    else:
        print("Invalid input!!!")


fib(-4)


