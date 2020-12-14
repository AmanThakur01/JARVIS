class Student:
    def __init__(self,name, std, age):
        self.name = name
        self.std = std
        self.age = age

    def __add__(self, other):       # that is called Dunder method/ operator overloading
        return self.std + other.std

    def __truediv__(self, other):
        return self.std / other.std     # you can use age also in place of std


a1 = Student("aman", 12, 18)
a2 = Student("Piyush", 12, 18)
a = a1 + a2         # we overload add operator
aa = a1 / a2
print(a)
print(aa)
