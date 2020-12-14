
import time
'''if u want to print comment so call like this -(func1.__doc__)'''
ini = time.time()
#COUNT
ttt = "a"
phrase = "aman thakur"
k = phrase.split(" ")# it return array having splited word
print(k)
#print(phrase.capitalize())# it capitilize first letter
aman = " aman"
print(aman.isnumeric())
print(phrase.count(ttt))# it will give no. of count of word come in phrase varable
print(phrase.center(99))
print(phrase.endswith("thakur"))# it give bool for ending word of string
index = phrase.find("m") #it return -1 if substring dosn't exist in string(true = +ev, false = -ev)
print(index)
print(ascii("jamuntoal"))

print(phrase[2])
print(phrase.index("a"))
print(len(phrase))
print(phrase[0:3]) # slicing
print(phrase[0:3:2])
print("-----",phrase[:])
#CHARACTER
character = "Python."
print(" trying to learn " + character)

#CASE PROBLEM
print(phrase.upper())
print("aman".isupper())
print(character.lower())
for i in range(0,10,2):
    print(i)

#NUMBER PROBLEM
print(12%5)#output is reminder that is
print(abs(2-4))# abs means mode
num = 5
print(str(num) + " is my favourate number.")
print(pow(2,4) + 16)
print(max(2,3,4,5))
print(min(1,2,3,45,3))
print(round(2.4657584))
from math import *
print(floor(3.4))
print(ceil(3.5))
print(sqrt(81))
# symbol
print(phrase[::-1]) # 1,2....


d1 = {1:"aman",2:"thakur"}#dictionary
print(d1)
d1.update({3:"name"})
print(d1)


with open("list.py") as f: #we can open file without close
    a = f.readlines()
    print(a)
list1 = ['1', '2', '3', '4']
s = "-"
s = s.join(list1)
print(s)
ini2 = time.time() - ini
print(ini2)
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

from _datetime import datetime
expDate2 = datetime.strptime('10/10/2020', "%d/%m/%Y").date()
print(expDate2)

# raise ZeroDivisionError("Ewww....")
