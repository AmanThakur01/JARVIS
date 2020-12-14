l = [10,20,30,40]
print(l)
print(l[0])       #index value
print(l[1:])
l.append(50)
print(l)
l.insert(2,25)
print(l)
l.remove(25)      #remove value
print(l)
l.pop(1)          #remove value index wise
print(l)
l.extend([60,70])
print(l)
del l[3:]
print(l)
l.sort()
print(l)
print(sum(l))
print(min(l))
print(max(l))