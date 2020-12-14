# import datetime
# import re
# # ct_date = datetime.datetime.now()
# print(ct_date)
# lst = []
# #lst.append("aman")
# print(lst)
# lst = {}
# ---------------------------------------
# a = input("enter key and scope separated by ':'")
# lst[0] = a
# print(lst.get())
# ct_date = datetime.datetime.now()
# val_ct_date = ct_date.strftime("%Y")
# print(val_ct_date)
#--------------------------------------
# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)
#
# txt = "The rain in Spain"
# x = re.search("\s", txt)
# print("The first white-space character is located in position:", x.start())
# txt = "The rain in Spain rain"
# x = re.search("rain", txt)
# print(x)
#
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)
# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)
#
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)
#
# string = "aman +919893063139, thakur, 91 +919893063130 +919893063139 aman"
# patt = re.compile(r"(91)\d{10}")
# a = patt.finditer(string)
# for i in a:
#     print(i)
#
# txt = "The rain in Spain "
# x = re.sub("\s", "9", txt, 2)
# print(x)
# ------------------------------------
# lst = [1, 2, 3, 4, 5, 6]
# if len(lst)%2 == 0:
#     d = len(lst)/2
#     for i in range(int(d)):
#         lst[i],lst[len(lst)-1-i]=lst[len(lst)-1-i], lst[i]
#     print(lst)
# --------------------------------------
# a = int(input("Enter number of inputs : "))
# n = int(input("Enter number for palindrome: "))
# def pd1(n):
#     return n[::-1] == n
# def pd(n):
#     while not pd1(str(n)):
#         n+=1
#     return n
# a = pd(n)
# print(a)
# a = str(input("Enter words for palindrome: "))
# def pd2(n):
#     return n[::-1] == n
# def pd3(a):
#     while not pd2(a):
import platform
platform.architecture()