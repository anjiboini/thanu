class Aniamal:
    def eat(self):
                print("Eating")

class Dog(Aniamal):
    def bark(self):
                print("Barking")

class Tiger(Dog):
    def cry(self):
                print("Cry")


class Lion(Tiger):
    def run(self):
                print("Runing")


class BabyDog(Lion):
    def sleep(self):
                print("Sleeping")

d = BabyDog()
d.sleep()
d.eat()
d.bark()
d.cry()
d.run()




