num = [1,2,3,4,5,56,57,4,45]
even = list(filter(lambda a:a%2==0,num))    # it filter data acording to function
print(even)
add = list(map(lambda a:a+2,even))  # it do a specific function
print(add)

# always keep in mind use this type of function for short program....

from functools import reduce
re = reduce(lambda a,b:a+b,add)
print(re)

