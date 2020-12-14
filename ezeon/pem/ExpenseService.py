# The class handle all business operations
from datetime import datetime

from ezeon.pem.Expense import Expense


class ExpenseService():
    list = []  # common repository to store all expenses

    def addSampleData(self):
        # sample for year 2019
        expDate1 = datetime.strptime('10/10/2019', "%d/%m/%Y").date()
        ex1 = Expense('Fees', 5000, 'Bus Fee', expDate1)
        ex2 = Expense('Shopping', 6000, 'Birthday Shopping', expDate1)
        ex3 = Expense('Fees', 2000, 'Tuition Fees', expDate1)

        # sample for year 2020
        expDate2 = datetime.strptime('10/10/2020', "%d/%m/%Y").date()
        ex4 = Expense('Fees', 8000, 'Bus Fee', expDate2)
        ex5 = Expense('Party', 8000, 'Birthday party', expDate2)
        self.addExpense(ex1)
        self.addExpense(ex2)
        self.addExpense(ex3)
        self.addExpense(ex4)
        self.addExpense(ex5)

    def inputAndAddExpense(self):
        # take expense detail from user
        cat = input("Enter Category : ")
        amt = int(input("Enter Amount : "))
        desc = input("Enter Detail : ")
        expdateStr = input("Enter Date (DD/MM/YYYY) : ")
        expDate = datetime.strptime(expdateStr, "%d/%m/%Y").date()
        ex = Expense(cat, amt, desc, expDate)
        self.addExpense(ex)

    def addExpense(self, expense):
        self.list.append(expense)

    def printAll(self):
        for e in self.list:
            print(e.category, e.amount, e.desc, e.expdate.strftime('%d/%m/%Y'))

    def totalExpesne(self):
        total = 0;
        for e in self.list:
            total = total + e.amount
        return total

    # Total expense for input category
    def totalExpesneForCategory(self, category):
        total = 0;
        for e in self.list:
            if (e.category == category):
                total = total + e.amount

        return total

    def getCategories(self):
        catNameList = []
        for e in self.list:
            catNameList.append(e.category)

        cats = set(catNameList)
        return cats

    def totalCategoryWise(self):
        exCats = self.getCategories()
        for cat in exCats:
            total = self.totalExpesneForCategory(cat)
            print({cat: total})

    def totalExpesneYearWise(self):
        dictYears = {}
        for e in self.list:
            dictYears.update({e.expdate.year: 0})

        for y in dictYears.keys():
            total = 0;
            for e in self.list:
                if (y == e.expdate.year):
                    total = total + e.amount

            dictYears.update({y: total})

            # print(dictYears) : print year wise total
        allTotal = 0;
        for y in dictYears:
            allTotal = allTotal + dictYears[y];
            print({y: dictYears[y]})

        print("----------------")
        print("All Total : ",{allTotal})
