class Parent1:
    def m1(self):
        print("Parent1 class method")

class Parent2:
    def m2(self):
        print("Parent2 calss method")

class Child(Parent1,Parent2):
    def m3(self):
        print("Child Method")

c1 = Child()
c1.m1()
c1.m2()
c1.m3()
