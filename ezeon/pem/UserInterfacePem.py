class UserInterfacePem():
    def __init__(self, service):
        self.service = service

    def printMenu(self):
        # Menu Navigation
        while True:
            print('-------MENU-------')
            print('1. Add Expense')
            print('2. List Expense')
            print('3. Total Expense')
            print('4. Total Category Wise')
            print('5. Total Year Wise')
            # TODO other menu options
            print('0. Exit')
            print('--------------')
            try:
                choice = int(input('Enter Choice: '))
            except:
                print("Invalid Choice Entered")
                choice = int(input('Enter Valid Choice: '))

            if choice == 1:
                # print('Add Expense Task')
                try:
                    self.service.inputAndAddExpense()
                except ValueError:
                    print('Invalid Input')

                input('Press any key to continue...')
                print('\n\n')

            if choice == 2:
                # print('List Expense Task')
                self.service.printAll()
                input('Press any key to continue...')
                print('\n\n')

            if choice == 3:
                # print('Total Expense')
                print('Total Expesne: {}'.format(self.service.totalExpesne()))
                input('Press any key to continue...')
                print('\n\n')

            if choice == 4:
                # print('Total Expense Category Wise')

                self.service.totalCategoryWise()

                input('Press any key to continue...')
                print('\n\n')

            if choice == 5:
                # print('Total Expense Year Wise')

                self.service.totalExpesneYearWise()

                input('Press any key to continue...')
                print('\n\n')

            if choice == 0:
                break

        print('Program end.')
