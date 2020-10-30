#class Student:
  #  college = "Python Tutorials"
  #  @classmethod
  #  def display(cls):
  #          print(Student.college)
  #          print(cls.college)
#s1 = Student()
#s1.display()

class addition:
    @staticmethod
    def add(x,y):
        print("the sum is:",x+y)
a1 = addition()
a1.add(3.7,4.7)
addition.add(3,6)