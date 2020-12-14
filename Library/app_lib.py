from userInterface import UserInterface
from bookService import BookService

service = BookService()
service.old()

ui = UserInterface(service)
ui.main_menu()