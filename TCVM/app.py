print("----------------------------Welcome into Tea vending machine-----------------------------------")
from sugar_cont import sugar_cont
from water_cont import water_cont
from milk_cont import milk_cont
from tea_cont import tea_cont
from coffee_cont import coffee_cont
from getpass import getpass
i = 1
t = 1
k = 2
s =0
def cont():
    sugar_cont.sugar_tot()
    milk_cont.milk_tot()
    water_cont.water_tot()
while k > 1:
    want = int(input("Press 1. for tea.\nPress 2. for coffee.\nPress 3. if you are from management.\nPress 0 for exit.\n"))
    if want == 1:
        i = 1
        name = "tea"
        no_cup = int(input("Enter number of cups of tea : "))
        while i<=no_cup  and s<=100:
            s = s + 1
            if s <= 100:
                sugar = sugar_cont(20)
                cont()
                tea_cont.tea_tot()
                water = water_cont(100)
                milk = milk_cont(100)
                tea = tea_cont(5)
                i += 1
                d = s
            else:
                print("====== Please Refill the containers=======")
                break
        price = (i-1) * 10
        print("Your " + str(i-1)+ " cup tea is Ready Please Collect it."
                                  "\nPay Amount = " + str(price) + "Rs only.")
        i=0
    elif want == 2:
        i=1
        d = s
        no_cup = int(input("Enter number of cups of coffee : "))
        while i <= no_cup and s<=100:
            s = s + 1
            if s<=100:
                sugar = sugar_cont(20)
                cont()
                coffee_cont.coffee_tot()
                water = water_cont(100)
                milk = milk_cont(100)
                coffee = coffee_cont(5)
                i += 1
            else:
                print("Please Refill the containers")
                break
        price = (i-1) * 20
        print("Your " + str(i-1) + " cup coffee is Ready Please Collect it."
                                      "\nPay Amount = " + str(price) + "Rs only.")
        i=0
    elif want == 0:
        k = 0
    elif want == 3:
        t=0
        while t <= 3:
            name = "aman"
            username = input("Enter Your User Name : ")
            password = int(getpass("Enter Your Password :"))
            if username == name and password == int(12):
                print("Login Successfully...")
                z = 1
                while z > 0:
                    view_cont = int(input("Press key to view container detail\nPress 1. For tea container.\nPress 2. For coffee container.\nPress 3."
                                          " For Milk container.\nPress 4. For sugar container.\nPress 5. For Water container.\nPress 0. For exit.\n"))
                    if view_cont == 1:
                        print(tea_cont.manage())
                    elif view_cont == 2:
                        print(coffee_cont.manage())
                    elif view_cont == 3:
                        print(milk_cont.manage())
                    elif view_cont == 4:
                        print(sugar_cont.manage())
                    elif view_cont == 5:
                        print(water_cont.manage())
                    elif view_cont == 0:
                        z = 0
                        t = 4
                    else:
                        print("Enter valid number ...")
                    print("--------------------------------------------------------------------------------------------")

            else:
                print("Login Failed!")
                t += 1
    else:
        print("Enter valid number... ")
    print("---------------Come Again--------------------")
