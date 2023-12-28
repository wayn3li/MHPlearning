class people:
    def __init__(self,name):
        self.name = name
      
class postgraduates(people):
    def __init__(self,name,writing):
        super().__init__(name)
        self.writing = writing
    def write(self):
        print(f"{self.name}写了{self.writing}")
      
class university student(people):
    def __init__(self,name,prograss,learning):
        super().__int__(name)
        self.prograss = prograss
        self.learning = learning
    def learn(self):
        print(f"{self.name}在{self.prograss},学习{self.learning}")
