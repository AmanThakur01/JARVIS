def sayhi(name):
    print("hello " + name)


person = (input("Enter your Name : "))      # the value of name varable is  person
sayhi(person)


def cube(num):
    print(num*num*num)


cube(3)


def cube(num):
    return num*num*num


print(cube(3))
