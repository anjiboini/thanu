class Student:
    def setName(self,Name):
        self.Name=Name
    def setNum(self,Num):
        self.Num=Num
    def getName(self):
        return self.Name
    def getNum(self):
        return  self.Num
s1 = Student()
s1.setName("anji")
s1.setNum(101)
print(s1.getName())
print(s1.getNum())