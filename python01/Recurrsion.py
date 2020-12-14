#Recursion means the function calling itself.
import sys
sys.setrecursionlimit(2000)# Here i can set recursion limit.(2000)
print(sys.getrecursionlimit())
i = 0


def rec():
    global i
    i+=1
    print("hello",i)
    rec()


rec()
