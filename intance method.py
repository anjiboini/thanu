class Student:
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def display(self):
        print(self.name)
        print(self.num)

s1 = Student("anji",101)
s2 = Student("thanu",102)
s1.display()
s2.display()

