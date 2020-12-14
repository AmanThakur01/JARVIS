from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(50):
            print("hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(50):
            print("hi")
            sleep(1)


r1 = Hello()
r2 = Hi()
r1.start()
r2.start()
r1.join()