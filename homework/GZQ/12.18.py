class person:
    def __init__(self,name,sex):
        self.name =name
        self.sex = sex
class undergraduate(person):
    def study(self,name,department):
        super().__init__(name)
        self.department=department
class graduate_student(person):
    def study(self,name,work):
        super().__init__(name)
        self.work=work
