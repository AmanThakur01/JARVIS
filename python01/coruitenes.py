import time


def cor():
    time.sleep(3)
    book = "aman got some new books"
    print("it started")

    while True:
        text = (yield)
        if text in book:
            print("found")
        else:
            print("not found")


a = cor()
next(a)
a.send("aman")
input()
a.send("got")
