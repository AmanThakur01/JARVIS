from ezeon.pem.ExpenseService import ExpenseService
from ezeon.pem.UserInterfacePem import UserInterfacePem

service = ExpenseService()
service.addSampleData()

ui = UserInterfacePem(service)
ui.printMenu()