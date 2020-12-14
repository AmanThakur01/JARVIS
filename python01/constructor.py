class computer:
    def __init__(self):
        self.ram = "16gb"
        self.cpu = "i5"
    def compare(self,c2):
        self.cpu == c2.cpu

c1 = computer()
c2 = computer()
c2.cpu = "i10"
print(c1.cpu)
print(c2.cpu)
if c1.compare(c2):
    print("it is same...")
else:
    print("they are different...")

