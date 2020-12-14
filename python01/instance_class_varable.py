class car:
    wheel = 4
    def __init__(self):
        self.comp = "BMW"
        self.color = "Black"

c1 = car()
c2 = car()
c2.color = "Red"
print(c2.color,car.wheel)

#wheel is class varable and color is instant varable

