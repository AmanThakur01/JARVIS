num1 = float(input("Enter First Number : "))
opperator = input("Enter Opperator : ")
num2 = float(input("Enter Second Number : "))
if opperator == "+":
    print(num1 + num2)
elif opperator == "-":
    print(num1 - num2)
elif opperator == "/":
    print(num1/num2)
elif opperator== "*":
    print(num1*num2)
elif opperator == "^":
    print(pow(num1,num2))
    #print("Second num must be always in integer ")
    #result =1
   # for index in range(int(num2)):
   #     result = result*num1
  #  print(result)
elif opperator == "%":
    print((num1/100)*num2)

else:
    print("Opps! Invalid Opperator.")
print("-----------------------------------------------------------------------------------------------------------------")
