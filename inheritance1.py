class Parent:
    def m1(self):
        print("Parent Instance method")
    def m2(cls):
        print("Parent Class method")

class Child(Parent):
    @staticmethod
    def m3():
        print("Child Class Static method")

c1 =Child()
c1.m1()
c1.m2()
c1.m3()