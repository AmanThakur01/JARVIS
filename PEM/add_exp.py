amt = 0
class Expanse:
    common = ["(Category, Amount, Date, Details)",
              "(school_free, 4000, 01/04/2020,Monthly fee)",
              "( room_rent, 4000,01/04/2020,without Electricity bil)",
              "(Travelling, 2000, 01/04/2020, including luxurious travel)"
              ]
    cat = ["school_free", "room_rent", "Travelling"]
    def add():
        try:
            global amt
            category = str(input("Enter Category of Expanse : "))
            amount = int(input("Enter Amount of Expanse : "))
            date = float(input("Enter date of Expanse(e.g DD.MM) : "))
            detail = input("Enter Detail about Expanse : ")
            a = "{}, {}, {}, {}".format(category, amount, date, detail)
            Expanse.cat.append(category)
            Expanse.common.append(a)
            amt = amt + amount
        except Exception:
            print("Something went wrong please check it.!!!!")

    def view():
        for i in Expanse.common:
            print(i)

    def tot_exp():
        tot = 10000 + amt
        print(tot)

    def view_cat():
        for i in Expanse.cat:
            print(i)

