# class Student:
#     def __init__(self):
#         self.name = "Aman"
#         self.std = "12"
#         self.age = 18
#         # self.email = "amanmrthakur@gmail.com"
#
#     @property
#     def email(self):
#         return "amanmrthakur@gmail.com"
#
#     @email.setter
#     def email(self,string):


# a = Student()
# print(a.email)
# Student.email = "racerBOT@gmail.com"
# print(a.email)
#     @email.deleter
#     a.email = None
# print(a.email)


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = "{}rm{}@gmail.com".format(fname, lname)

    def explain(self):
        return "this employ is {} {}".format(self.fname,self.lname)
    @property
    def email(self):
        if self.fname == None and self.lname == None:
            return "Email is not found"
        return "{}rm{}@gmail.com".format(self.fname, self.lname)
    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


a1 = Employee("aman","thakur")
print(a1.explain())
# print(a1.email())
print(a1.email) # using @property it take as attribute
a1.fname = "ran"
print(a1.email)
# print(a1.email())
a1.email = "this.that@gmail.com"
print(a1.email)
del a1.email

print(a1.email)
a = "aman"
print(dir(a))
# .id


import inspect
print(inspect.getmembers(a1))
