# colors = ["red", "green", "blue", "yellow", "white", "black"]
# print(colors)
# for i in colors[:3]:
#     print(i)
# for i in colors[-3:]:
#     print(i)
# colors.append("cyan")
# index = 2
# while index < 5:
#     colors.pop(2)
#     index += 1
#
# print(len(colors))
# for i in colors:
#     if i=="orange":
#         print("Orange is present")
#     else:print("Not Present")


# def checkYear(year):
#     if (year % 400 == 0):
#         return True;
#
#     if (year % 100 == 0):
#         return False;
#
#     if (year % 4 == 0):
#         return True;
#     return False;
#
# year = int(input("Enter a year: "))
#
# print("Leap Year")if checkYear(year) else print("Not a Leap Year")

#
# family={"Name":"Vijay",
#         "income":45000,
#         "child":["hema","neha","ranbeer"]}
#
# for key, value in family.items() :
#     print(key)
#     if key=="child":
#         print(value)
#         print(len(value))
#
# family["income"]=(family["income"])*1.5
# family["child"].append("ravi")
#
# List=[12,15,32,42,55,75,122,132,150,180,200]
# for i in List:
#     if i>150:
#         break
#     elif i%5==0:
#         print(i)
#     else:pass


# file = open("/home/aman/PycharmProjects/python02/msg.txt","r")
#
#
# fileList=file.read()
# fileLine=fileList.split(' ')
# print(fileLine)
# for index,i in enumerate(fileLine):
#     print(index,i)
#
# file.close()

# file=open('story.txt','r')
#
# line=file.read()
# word=line.split(' ')
# for w in word:
#     if len(w)<5:
#         print(w)
#     else:pass
#
# file.close()

# try:
#     val=int(input("Enter value :"))
#     sum=val+val
#     print("value+value = ",sum)
#
# except Exception as e:
#     if e==TypeError or e== NameError:
#         pass
#     else:print(e)
# finally:
#     print("Calculation over.")

# import math
#
# print (math.degrees(-20))           #1
#
# p = [3, 3]
# q = [6, 12]
#
# print (math.dist(p, q))             #2
#
# radi=2
# print(math.pi*pow(radi,2))          #3 pi val=3.14
#
# print (math.sqrt (100))             #4
#
# print(math.factorial(12))           #5
#
# print(math.cos(math.pi))           #6 use pi
#
# print(math.ceil(5.3))               #7
#
# print(math.exp(65))                 #8
#
# print(math.floor(10.0))             #9
#
# print(math.radians(180))            #10


# from io import StringIO
# # The arbitrary string.
# string = 'Hello and welcome to GeeksForGeeks.'
#
# # Using the StringIO method to
# # set as file object.
# file = StringIO(string)
#
# # This will returns whether the file
# # is interactive or not.
# print("Is the file stream interactive?", file.isatty())
#
# # This will returns whether the file is
# # readable or not.
# print("Is the file stream readable?", file.readable())
#
# # This will returns whether the file supports
# # writing or not.
# print("Is the file stream writable?", file.writable())
#
# # This will returns whether the file is
# # seekable or not.
# print("Is the file stream seekable?", file.seekable())


# import numpy as np
#
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([6, 7, 8, 9, 0])
#
# # Addition of two Arrays
# Sum = np.add(arr1, arr2)
# print("Addition of Two Arrays: ")
# print(Sum)
#
# # Addition of all Array elements
# # using predefined sum method
# Sum1 = np.sum(arr1)
# print("\nAddition of Array elements: ")
# print(Sum1)
#
# # Square root of Array
# Sqrt = np.sqrt(arr1)
# print("\nSquare root of Array1 elements: ")
# print(Sqrt)
#
# # Transpose of Array
# # using In-built function 'T'
# Trans_arr = arr1.T
# print("\nTranspose of Array: ")
# print(Trans_arr)
#
# vector_a = 2 + 3j
# vector_b = 4 + 5j
# product = np.dot(vector_a, vector_b)
#
# array = np.arange(8).reshape(2, 4)
#

import sys
#
# try:
#     f = open('story.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#
# import math
# class Circle():
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         area=math.pi*pow(self.radius,2)
#         return area
#     def perimeter(self):
#         perimeter=2*math.pi*self.radius
#         return perimeter
#
# NewCircle=Circle(0)
# print(NewCircle.area())
# print(NewCircle.perimeter())