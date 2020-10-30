class Outer:
    def __init__(self):
        print("Outer class contructor")
    class Inner1:
        def __init__(self):
            print("Inner class1 constructor")
        def m1(self):
            print("Inner class1 method")
    class Inner2:
        def __init__(self):
            print("Inner class2 constructor")
        def m1(self):
            print("Inner class2 method")

#o = Outer()
#i = o.Inner()
#i.m1()
#i = Outer().Inner()
#i.m1()

Outer().Inner1().m1()
Outer().Inner2().m1()