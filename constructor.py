
##defult contructor
#class constructorDemo:

    #def __init__(self):
     #   print("Constructor excuted")
   # def tutorial(self):
   #     print("anji python tutorial")


##bj.tutorial()
##obj.tutorial()
##obj.tutorial()

#parameter contructor
class Student:
    def __init__(self,n,r):
        self.name=n
        self.rollno=r
    #def display(self):
       # print("   Student name: {} \n   Student Rollno: {}".format(self.name,self.rollno))
       # print("Name:%s  Rollno:%d"  %(self.name,self.rollno))
#s1= Student("yeshu",104)
#s2=Student("thanu",105)

#s1.display()
#s2.display()

s1= Student("yeshu1",107)

setattr(s1,'name','anju')
print(getattr(s1,'name'))
print(hasattr(s1,'Address'))
print(hasattr(s1,'name'))
delattr(s1,'name')
print(getattr(s1,'name'))

