
num = 5
guess = ""
guess_count = 0
while guess != num and not(guess_count>=3):
    guess = int(input("Enter Your Lucky Number : "))
    guess_count += 1
if guess_count>=3 and guess != num:
        print("Count out . YOU LOSE! ")
else:
    print("You win! ")
print("----------------------------------------------------------------------------------------------------------------")

