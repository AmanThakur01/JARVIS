from Book import Book
from datetime import datetime
y = float
e = int
h = dict
p = ""


class BookService:
    Horror = {}
    Action_and_adventure = {}
    History = {}
    Thriller = {}
    Fantasy = {}
    Fiction = {}
    Mystery = {}
    Other = {}
    categories = ["Action_and_adventure", "History", "Thriller", "Fantasy", "Fiction", "Mystery", "Horror", "Other"]

    def cat_list(self):
        j = 1
        for i in self.categories:
            print("Press {} For {}.".format(j, i))
            j += 1

    def old(self):
        bk1 = [Book("A SUITABLE BOY", "Vikram Seth", "2020", 400, "Fiction")]
        bk2 = [Book("MAHABHARATA", "Vyasa", "2006", 800, "Action_and_adventure")]
        bk3 = [Book("WINGS OF FIRE", "A.P.J. Abdul Kalam", "2009", 600, "History")]
        bk10 = [Book("THE DISCOVERY OF INDIA", "Jawaharlal Nehru", 2012, 299, "History")]
        bk4 = [Book("CHANDRAKANTA", "Devaki Nandan Khatri", "2000", 769, "Fantasy")]
        bk12 = [Book("CHANDRAKANTA", "Devaki Nandan Khatri", "2017", 769, "Fantasy")]
        bk5 = [Book("SACRED GAMES", "Vikram Chandra", "2020", 300, "Thriller")]
        bk11 = [Book("SACRED GAMES", "Vikram Chandra", "2015", 300, "Thriller")]
        bk6 = [Book("THE UNEXPECTED INHERITANCE OF INSPECTOR CHOPRA", "Vaseem Khan", "2010", 500, "Mystery")]
        bk13 = [Book("THE UNEXPECTED INHERITANCE OF INSPECTOR CHOPRA", "Vaseem Khan", "2018", 500, "Mystery")]
        bk7 = [Book("SITA: WARRIOR OF MITHILA", "‎Amish Tripathi", "2020", 100, "Horror")]
        bk8 = [Book("TALE OF TWO CITIES", "Charles Dickens", "2019", 100, "Other")]
        bk9 = [Book("GEETA", "Vyasa", 2009, 800, "Other")]
        bk0 = [Book("HARRY POTTER", "J.K. Rowling", 2019, 700, "Action_and_adventure")]
        self.adv_book(bk2)
        self.hist_book(bk13)
        self.hist_book(bk12)
        self.hist_book(bk11)
        self.hist_book(bk3)
        self.thrill_book(bk5)
        self.fan_book(bk4)
        self.horr_book(bk7)
        self.mstry_book(bk6)
        self.oth_book(bk8)
        self.oth_book(bk9)
        self.fic_book(bk1)
        self.fic_book(bk0)
        self.fic_book(bk10)

    try:
        def addbook(self):
            global val
            while True:
                print("----Choose Category of Book you want to Donate.\n")
                self.cat_list()
                cat = int(input("Press 0. To Go Back.\nEnter Your Choice.\n>>>"))
                if cat < 9 and cat != 0:
                    name = input("Enter Book Name in Capital Letter.\n>>>")
                    writer = input("Enter Writer Name : ")
                    while True:
                        edition = int(input("Enter Book Edition Year : "))
                        ct_date = datetime.now()
                        val_ct_date = ct_date.strftime("%Y")
                        val = int(val_ct_date) - edition
                        if val <= 15:
                            break
                        else:
                            print("Book should not older than 15 year.")
                    mrp = float(input("Enter Marked Price in Book : "))
                    if cat == 1:
                        n = "Action_and_adventure"
                        bk = [Book(name, writer, edition, mrp, n)]
                        self.adv_book(bk)
                    elif cat == 2:
                        n = "History"
                        bk = [Book(name, writer, edition, mrp, n)]
                        self.hist_book(bk)
                    elif cat == 3:
                        n = "Thriller"
                        bk = [Book(name, writer, edition, mrp, n)]
                        self.thrill_book(bk)
                    elif cat == 4:
                        n = "Fantasy"
                        bk = [Book(name, writer, edition, mrp, n)]
                        self.fan_book(bk)
                    elif cat == 5:
                        n = "Fiction"
                        bk = [Book(name, writer, edition, mrp, n)]
                        self.fic_book(bk)
                    elif cat == 6:
                        n = "Mystery"
                        bk = [Book(name, writer, edition, mrp, n)]
                        self.mstry_book(bk)
                    elif cat == 7:
                        n = "Horror"
                        bk = [Book(name, writer, edition, mrp, n)]
                        self.horr_book(bk)
                    elif cat == 8:
                        n = "Other"
                        bk = [Book(name, writer, edition, mrp, n)]
                        self.oth_book(bk)
                    print("Book added Successfully+++")
                elif cat == 0:
                    break
                else:
                    print("Enter valid integer.")
    except ValueError:
        print("Oops! Something went wrong in addbook().!!!")

    def adv_book(self, book):
        self.Action_and_adventure.update({book[0]: book})

    def horr_book(self, book):
        self.Horror.update({book[0]: "book"})

    def fan_book(self, book):
        self.Fantasy.update({book[0]: "book"})

    def hist_book(self, book):
        self.History.update({book[0]: "book"})

    def thrill_book(self, book):
        self.Thriller.update({book[0]: "book"})

    def fic_book(self, book):
        self.Fiction.update({book[0]: "book"})

    def mstry_book(self, book):
        self.Mystery.update({book[0]: "book"})

    def oth_book(self, book):
        self.Other.update({book[0]: "book"})

    def printcate(self):
        line = "\n-------"
        self.cat_list()
        cat_no = int(input())
        self.condition(cat_no)

    def printall(self):
        print("All Books in Library-")
        for num in range(1, 9):
            self.condition(num)

    def condition(self, cat_no):
        line = "-------"
        if cat_no == 1:
            print("\nAction_and_adventure")
            for i in self.Action_and_adventure:
                print(line, i.book_name)
        elif cat_no == 2:
            print("\nHistory")
            for i in self.History:
                print(line, i.book_name)
        elif cat_no == 3:
            print("\nThriller")
            for i in self.Thriller:
                print(line, i.book_name)
        elif cat_no == 4:
            print("\nFantasy")
            for i in self.Fantasy:
                print(line, i.book_name)
        elif cat_no == 5:
            print("\nFiction")
            for i in self.Fiction:
                print(line, i.book_name)
        elif cat_no == 6:
            print("\nMystery")
            for i in self.Mystery:
                print(line, i.book_name)
        elif cat_no == 7:
            print("\nHorror")
            for i in self.Horror:
                print(line, i.book_name)
        elif cat_no == 8:
            print("\nOther")
            for i in self.Other:
                print(line, i.book_name)
        else:
            print("Enter valid integer.")

    def buy(self):
        try:
            print("----Choose Category of Book you want to buy.\n")
            self.cat_list()
            cate = int(input("Enter Your Choice.\n>>>"))
            if cate < 9 and cate != 0:
                name = input("Enter Book Name in Capital Letter.\n>>>")
                x = self.diff_cate(cate, name)
                if x==None:
                    for num in range(1, 10):
                        x = self.diff_cate(num, name)
                        if x==None:
                            pass
                        else:
                            print(x)
                            break
                else:
                    print(x)
                self.calculate()
            else:
                print("Oops! Invalid Input!!!")
        except:
            print("Oops! Something went wrong in buy()!!!")

    def diff_cate(self, cate, name):
        global y, e, h
        if cate == 1:
            for i in self.Action_and_adventure:
                if i.book_name == name:
                    y = i.MRP + 0.0
                    e = i.edition
                    h = i.category
                    return "{} <Writer: {}> <Edition: {}> <M.R.P.: {}Rs.> <{}>".format(i.book_name, i.writer, i.edition, i.MRP, i.category)
        elif cate == 2:
            for i in self.History:
                if i.book_name == name:
                    y = i.MRP
                    e = i.edition
                    h = i.category
                    return "<{}> <Writer: {}> <Edition: {}> <M.R.P.: {}Rs.> <{}>".format(i.book_name, i.writer, i.edition, i.MRP, i.category)
        elif cate == 3:
            for i in self.Thriller:
                if i.book_name == name:
                    y = i.MRP + 0.0
                    e = i.edition
                    h = i.category
                    return "<{}> <Writer: {}> <Edition: {}> <M.R.P.: {}Rs.> <{}>".format(i.book_name, i.writer, i.edition, i.MRP, i.category)
        elif cate == 4:
            for i in self.Fantasy:
                if i.book_name == name:
                    y = i.MRP + 0.0
                    e = i.edition
                    h = i.category
                    return "<{}> <Writer: {}> <Edition: {}> <M.R.P.: {}Rs.> <{}>".format(i.book_name, i.writer, i.edition, i.MRP, i.category)
        elif cate == 5:
            for i in self.Fiction:
                if i.book_name == name:
                    y = i.MRP + 0.0
                    e = i.edition
                    h = i.category
                    return "<{}> <Writer: {}> <Edition: {}> <M.R.P.: {}Rs.> <{}>".format(i.book_name, i.writer, i.edition, i.MRP, i.category)
        elif cate == 6:
            for i in self.Mystery:
                if i.book_name == name:
                    y = i.MRP + 0.0
                    e = i.edition
                    return "<{}> <Writer: {}> <Edition: {}> <M.R.P.: {}Rs.> <{}>".format(i.book_name, i.writer, i.edition, i.MRP, i.category)
        elif cate == 7:
            for i in self.Horror:
                if i.book_name == name:
                    y = i.MRP + 0.0
                    e = i.edition
                    h = i.category
                    return "<{}> <Writer: {}> <Edition: {}> <M.R.P.: {}Rs.> <{}>".format(i.book_name, i.writer, i.edition, i.MRP, i.category)
        elif cate == 8:
            for i in self.Other:
                if i.book_name == name:
                    y = i.MRP + 0.0
                    e = i.edition
                    h = i.category
                    return "<{}> <Writer: {}> <Edition: {}> <M.R.P.: {}Rs.> <{}>".format(i.book_name, i.writer, i.edition, i.MRP, i.category)
        else:
            print("Oops! Input Not Found???")

    def rent(self):
        global y
        try:
            print("----Choose Category of Book you want in Rent.\n")
            self.cat_list()
            cate = int(input("Enter Your Choice.\n>>>"))
            if cate < 9 and cate != 0:
                name = input("Enter Book Name in Capital Letter.\n>>>")
                v = self.diff_cate(cate, name)
                if v==None:
                    for num in range(1, 10):
                        v = self.diff_cate(num, name)
                        if v==None:
                            pass
                        else:
                            print(v)
                            break
                else:
                    print(v)
                day = int(input("Enter Number Of Renting Days (maximum 30day only): "))
                print("-----It Cost you Rs.", (((y / 100) * 1.00)*day), "only.")
                input("Press key to continue Payment....")
                print("====Collect Your Book\n-------Come Again-------")
            else:
                print("Oops! Invalid Input!!!")
        except:
            print("Oops! Something went wrong in rent()!!!")

    def calculate(self):
        global e
        ct_date = datetime.now()
        val_ct_date = int(ct_date.strftime("%Y"))
        interest = ((int(val_ct_date)-int(e))*4) + 00.00
        int_val = (y/100.0)*interest
        print("-----It cost you {} Rs. only".format((y - int_val)))
        input("Press key to continue Pay1ment....")
        print("====Collect Your Book\n-------Come Again-------")


