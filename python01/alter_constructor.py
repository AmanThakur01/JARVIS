class student:
    def __init__(self, name, std, age):
        self.name = name
        self.std = std
        self.age = age

    @classmethod
    def string(cls, string):
        # a = string.split("-")
        # return a
        # return cls(a[0],a[1],a[2])
        # print((string.split("-")))
        return cls(*string.split("-"))

    @staticmethod
    def mustline(news):
        print("employ ", news)
        return "enjoy"

s1 = student("aman","1","8")
print(s1.age)
s2 = student.string("piyush-12-18")
print(s2.mustline("this month you get 100rs bonus"))
print(s2.name)