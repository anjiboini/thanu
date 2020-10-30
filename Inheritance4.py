class GrandParent:
    def m1(self):
        print("GrandParent class method")

class Parent(GrandParent):
    def m2(self):
        print("Parent calss method")

class Child(Parent):
    def m3(self):
        print("Child Method")

c1 = Child()
c1.m1()
c1.m2()
c1.m3()
