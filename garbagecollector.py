#import gc
#print(gc.isenabled())

#gc.disable()
#print(gc.isenabled())

#gc.enable()
#print(gc.isenabled())
import sys
class DestructorExample:
    def __init__(self):
        print("Constructor Excuted")
    def display(self):
        print("Method Excuted")
    def __del__(self):
        print("Destructor Excuted")

d = DestructorExample()
print(sys.getrefcount(d)) 

