class Lab:
    def __init__(self,A,B,group1,group2,group3):
        self.A=A
        self.B=B
        self.group1 = group1
        self.group2 = group2
        self.group3 = group3
    def classA(self):
        A='第一部分'
        print(f"{A}是供研究生使用")
    def classB(self):
        B='第二部分'
        print(f"{B}是供实验室成员使用使用")
class partA(Lab):
    def classA(self):
        print("共有研究生12名")
class partB(Lab):
    group1="第一小组"
    print(f"{group1}的职能是：  共有 4人")
    group2="第二小组"
    print(f"{group2}的职能是：  共有 4人")
    group3="第三小组"
    print(f"{group3}的职能是：  共有 4人")
