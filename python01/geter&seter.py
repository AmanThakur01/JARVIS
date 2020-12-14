
class student:
    school = "telusko"

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        self.lap = self.laptop()

    def avg(self):
        return (self.m1 + self.m2)/3

    def show(self):
        print(self.m1,self.m2)
        # self.lap.show()

    class laptop:
        def __init__(self):
            self.ram =8
            self.cpu = "i5"

        def show(self):
            print(self.ram,self.cpu)


s1 = student(12,34)
s2 = student(98,34)
print(s1.avg())
s1.show()
