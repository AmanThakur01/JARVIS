import random
# 3 CHANCE AFTER YOU LOOSE THE GAME
for i in range(3):
    lst = ["Stone", "Paper", "scissors"]
    rn = random.choice(lst)
    ip = int(input("Press 1. For Stone\nPress 2. For Paper.\nPress 3. For Scissors.\n"))
    if ip == rn:
        print("!!!you win the GAME !!!")
    elif ip != rn and 0 < ip < 4:
        print("YOU LOOSE...Try Again")
    else:
        print("???Enter valid number???")
print("You LOOSE the Game ...BYE")
