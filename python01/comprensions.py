
lst = [i for i in range(100) if i%3 == 0]
print(lst)

dect = {i:"item{}".format(i) for i in range(100) if i%3==0}
print(dect)
dect = {value:key for key,value in dect.items()}
print(dect)

dd1 = {i for i in ["a1", "a2", "a3", "a1", "a2", "a3"]}
print(dd1)

gen = (i for i in range(100))
print(gen)