class Father:
        a = 2   # this is public varable
        _s = 3   # it is protected varable
        __d = 4  # is private


class Son(Father):
    print(Father.__d)


k = Son()

