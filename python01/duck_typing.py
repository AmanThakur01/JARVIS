class python:
    def code(self,ide):
        ide.execute()


class pycharm:
    def execute(self):
        print("compile")
        print("execute")


class my_ide(pycharm):
    def execute(self):
        super().execute()
    print("spell check")


ide = my_ide()
lan = python()
lan.code(ide)
