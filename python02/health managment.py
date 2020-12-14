# healthcare
import time
print("Here you can update your diet ,exercise like activities")
# def getdate():
#     import datetime
#     return datetime.datetime.now()
# a = getdate()
# print(a,end="")
a= time.asctime(time.localtime(time.time()))
get1 = int(input("Press 1. For upload data\nPress 2. For view data.\n"))
if get1 == 1:
    ip1 = int(input("Press 1. For Aman.\nPress 2. For Piyush.\n"))
    if ip1 == 1:
        with open("aman_load","a") as amanl:
            a2 = input("Enter your diet for today : ")
            a1 = amanl.write(str(a)+" = "+a2)
            amanl.write("\n")

    elif ip1 == 2:
        with open("piyush_load", "a") as piyushl:
            a3 = input("Enter your diet for today : ")
            a4 = piyushl.write(str(a) + " = " + a3)
            piyushl.write("\n")
    else:
        print("Enter valid Number..!")
elif get1 == 2:
    ip2 = int(input("Press 1. For Aman.\nPress 2. For Piyush.\n"))
    if ip2 == 1:
        with open("aman_load") as a5:
            r1 = a5.read()
            print(r1)
    elif ip2 == 2:
        with open("piyush_load") as a6:
            r = a6.read()
            print(r)
    else:
        print("Enter valid Number..!")
else:
    print("Enter valid Number..!")

