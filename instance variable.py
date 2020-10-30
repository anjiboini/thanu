#class Student:
 #   def __init__(self,n,r):
   #     self.name=n
   #     self.rollno=r
#s=Student("thanu",105)
#print(s.__dict__)
#s1 = Student("thanu",106)
#s2 = Student("yeshu",109)
#print(s1.__dict__)
#print(s2.__dict__)
#...........................................#

#class Student:
  #  def display(self):
   #     self.ename="Anji"
   #     self.eno=1123
     #   self.salary=20000

#el = Student()
#el.display()
#print(el.__dict__)

#..................................................#
#class Student:
   # def Display(self):
    #    print("welcome to instance variables")

#s1 = Student()
#s1.name="anji"
#s1. rollno=1123
#s1.address="Hyderabad"
#print(s1.__dict__)

#................................................................#

class Student:
    def __init__(self):
        self.name = "anji"
    def display(self):
        self.rollno=101

s1 = Student()
s1.display()
s1.address="hyderabad"

#print(s1.name,s1.rollno,s1.address)
del s1.address
print(s1.name,s1.rollno,s1.address)