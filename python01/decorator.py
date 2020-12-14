def dec1(dec2):
    def sup():
        print("It is most useful")
        dec2()
        print("hence it is called decorator.")
    return sup()


@dec1
def supose():
    print("because supo() can use between multi function")


