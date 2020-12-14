class student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def on_honor(self):
        if self.grade == "1":
            return "true"
        else:
            return "false"

