f = open("/home/shubha/Desktop/Aman/photo/_20200319_203026.JPG","rb")
f1 = open("my_pic","wb")
for i in f:
    f1.write(i)