class UserInterface():
    def __init__(self, service):
        self.service = service

    def main_menu(self):
        while True:
            try:
                print("-------------------Welcome---------------")
                usr = int(input("Press 1. To Donate Book.\nPress 2. To View Books Category wise."
                                "\nPress 3. To Buy Book.\nPress 4. To Take Book In Rent.\nPress 5. "
                                "To View All Books.\nPress 0. To Get out from library.\n>>>"))
                if usr == 1:
                    self.service.addbook()
                elif usr == 2:
                    self.service.printcate()
                elif usr == 3:
                    self.service.buy()
                elif usr == 4:
                    self.service.rent()
                elif usr == 5:
                    self.service.printall()
                elif usr == 0:
                    print("-------Thank You-------")
                    break
                else:
                    print("Enter Valid Integer.!!!")
            except ValueError:
                print("Oops! Something Went wrong from user!!!")