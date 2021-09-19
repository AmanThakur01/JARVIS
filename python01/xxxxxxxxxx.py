# a#for i in range(1,20,5):
#    # print(i)
#
# #txt = "helo"[::-1]
# #print(txt)
# import time
# # try:
# #     class person:
# #         def __init__(self):
# #             self.name = "aman"
# #             self.age = 18
# #     a1 = person()
# #     a2 = person()
# #     print(a1.name)
# # except ZeroDivisionError as e:
# #     print("Opps!@....sorry....!")
# # except ValueError as e:
# #     print("value error")
# # finally:
# #     print("come again")
# # for i in range(5):
# #     print(i)
# t1 = time.localtime(time.time())
# print(t1)
# categories = ["Action_and_adventure", "History", "Thriller", "Fantasy", "Fiction", "Mystery", "Horror", "Other"]
#
# for i in categories:
#      print(i)

# a=1,b=2
# res=a+b-(a=b-a)
# importing Numpy package
# importing numpy library
# import numpy as np
#
# # create numpy 2d-array
# m = np.array([[2, 2,1],
#               [1, 3,1],
#               [1,2,2]])
#
# print("Printing the Original square array:\n",
#       m)
#
# # finding eigenvalues and eigenvectors
# w, v = np.linalg.eig(m)
#
# # printing eigen values
# print("Printing the Eigen values of the given square array:\n",
#       w)
#
# # printing eigen vectors
# print("Printing Right eigenvectors of the given square array:\n",v)


# result=eval(input("enter your expression: "))
# print(result)
#
# i = 3
# while i > 0:
#     for j in range(5):
#         # print(j," ",end="")
#         if ((i - 1) > 0) and j < (i - 1):
#             print(" ", end="")
#         elif (i == 3 and j > 2) or (i == 2 and j > 3):
#             print(" ", end="")
#         else:
#             print("*", end="")
#     # print()
#
#     i = i - 1
#     print()

#
# a="'"
# for b in a:
#     if b=="h"or b=="H":
#         print("_",end="")
#     else:
#         print(b,end="")


# count = 3
# Str = input("Input String: ")
# for a in Str:
#     if count % 2 == 0:
#         print(a.lower(), end="")
#     else:
#         print(a.upper(), end="")
#     count = count + 1

# def listtostring(x):
#     str1 = ""
#     for ele in x:
#         str1 = str1 + ele + " "
#     return str1
#
#
# Str = list(map(str, input().split()))
# # print(Str)
# Rev = Str[-1::-1]
# print(listtostring(Rev))


# str1=(input("--> "))
# rev1=str1[::-1]
# print(rev1)


# import datetime
# import time
#
# Date = datetime.date.today()
# Time = time.localtime()
# ctime = time.strftime("%H:%M:%S", Time)
#
# Studata=open("student.txt","a")
# count=1
# while True:
#
#     name=input("Enter Name of a Student: ")
#     if name=="q" or name=="Q":
#         break
#
#     Studata.writelines(str(count))
#     Studata.write('\t')
#     Studata.writelines(name)
#     Studata.write('\t')
#     Studata.writelines(str(Date))
#     Studata.write('\t')
#     Studata.writelines(ctime)
#     Studata.write("\n")
#     count+=1
# Studata.close()


# ans = 1
# num = int(input())
# for a in range(num, 0, -1):
#     ans = ans * a
# print(ans)
#
#
# a=0
# b=1
# count=1
# stopcount=int(input("--> "))
# while count<=stopcount:
#     c = a + b
#     a=b
#     b=c
#     print(c,end=",")
#     count=count+1







