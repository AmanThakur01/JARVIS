from PEM.add_exp import *
while True:
    print("----------------Welcome-----------------")
    usr = int(input("Press 1. For Add Expanse.\nPress 2. For View Expanse.\nPress 3."
                    " For Total Expanse.\nPress 4. For View Expanse Category.\nPress 0. For Exit\n"))

    if usr == 1:
        Expanse.add()
    elif usr == 2:
        Expanse.view()
    elif usr == 3:
        Expanse.tot_exp()
    elif usr == 4:
        Expanse.view_cat()
    elif usr == 0:
        break
    else:
        print("Enter valid integer..! ")


























