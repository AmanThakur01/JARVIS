import re
string = """
We’d Love to Connect
Just drop us a line or
visit our social media pages
Send a Message
First Name
Last Name
Phone
Email
Organization
How can we help?
SUBMIT
Contact Info
Wynk Limited,
Bharti Crescent, 1,
Nelson Mandela Road,
Vasant Kunj Phase - II,
New Delhi – 110070
Corporate Identity Number: U74140DL2015PLC275325
Write to us
 webconnect@wynk.in 
CONTACT US
About Us
Solve hard problems. Impact Millions. All this while having fun.
Know More 
aman@gmail.com
thakur@ezeon.net
vyabha@yahoo.com
shubha@innoeye.in
Work with us
At Wynk Learn Earn Faster Execute at speed
Know More 
Life at Wynk
Join us for the most Memorable gig of your lif
Know More 
Tech at Wynk
Push code that brings Joy to Millions
Know More 
©Wynk 2018, All Rights Reserved"""
mail = []
sp = re.split("\s", string)
# print(sp)
for i in sp:
    path = re.compile(r".*@.*")
    s = path.finditer(i)
    for k in s:
        # print(k)
        print(k.span())
        a = k.group()
        mail.append(a)
print(mail)
