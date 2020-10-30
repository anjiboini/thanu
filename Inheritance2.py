class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employ(Person):
    def __init__(self,name,age,empno,empsl):
        super().__init__(name,age)
        self.empno=empno
        self.empsl=empsl
    def display(self):
        print("Emp Name: ",self.name)
        print("Emp Age: ",self.age)
        print("Emp ID: ",self.empno)
        print("Emp Salary: ",self.empsl)

e1 = Employ("anji",40,12345,10000)
e1.display()
