
def sum(a, *b):     # it is tupal kind of list ;;Tupal == company = ("mi" , "lenovo")
    print(*b)
    for i in b:
        a = a + i
    print(a)


sum(1, 2, 3, 4)


def x(name, **data):        # dict thisdict = {
                            #   "brand": "Ford",
                            #   "model": "Mustang",
                            #   "year": 1964
                            # }
    for c in data.items():
        print(c)
    print(name)


x(" aman ", age=18, std=12, city="bhopal")