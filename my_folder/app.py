import os


def string():
    file = os.listdir("/media/aman/Drive/Downloads")
    text = "videoplayback"
    j = 0
    for i in file:
        if text in i:
            j += 1
            source = "/media/aman/Drive/Downloads/{}".format(i)
            dest = "/media/aman/Drive/Downloads/{}".format(j)
            print("found : ", i)
            os.rename(source, dest)
        else:
            print("not found : ", i)
            k = i.capitalize()
            dest = "/media/aman/Drive/Downloads/{}".format(k)
            source = "/media/aman/Drive/Downloads/{}".format(i)
            os.rename(source, dest)
    print(os.listdir("/media/aman/Drive/Downloads"))


string()


def string1():
    file = os.listdir("/media/aman/Drive/AMAN/ohSolderPretifyMyFolder")
    j = 0
    for i in file:
        if i.isnumeric():
            j += 1
            source = "/media/aman/Drive/AMAN/ohSolderPretifyMyFolder/{}".format(i)
            dest = "/media/aman/Drive/AMAN/ohSolderPretifyMyFolder/{}{}".format("aman", j)
            print("found : ", i)
            os.rename(source, dest)
        else:
            print("not found : ", i)
            k = i.lower()
            dest = "/media/aman/Drive/AMAN/ohSolderPretifyMyFolder/{}".format(k)
            source = "/media/aman/Drive/AMAN/ohSolderPretifyMyFolder/{}".format(i)
            os.rename(source, dest)
    print(os.listdir("/media/aman/Drive/AMAN/ohSolderPretifyMyFolder"))

