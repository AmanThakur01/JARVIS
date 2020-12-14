class A:
    def __init__(self):
        print("init A is on...")

    def feature1(self):
        print("it is f1 of A")


class B:#B(A)
    def __init__(self):
        #super().__init__()#this super key can call parent class
        print("init B is on...")

    def feature1(self):
        print("it is f1 of B")


class C(B,A):
    def __init__(self):
        super().__init__()

        print( "it is f1 of c")


a1 = C()
a1.feature1()

