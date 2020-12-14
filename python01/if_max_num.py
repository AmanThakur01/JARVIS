def num_max(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
num1 = input("Enter First Number : ")
num2 = input("Enter second Number : ")
num3 = input("Enter third Number : ")

#print(num_max(num1,num2,num3))
num = num_max(num1,num2,num3)
print(num)
