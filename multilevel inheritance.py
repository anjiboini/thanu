class Aniamal:
    def eat(self):
                print("Eating")

class Dog(Aniamal):
    def bark(self):
                print("Barking")

class BabyDog(Dog):
    def sleep(self):
                print("Sleeping")

d = BabyDog()
d.eat()
d.bark()
d.sleep()
