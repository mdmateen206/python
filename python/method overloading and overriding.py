#method overriding
class animal:
    def sound(self):
        print("animal is braking")
class dog(animal):
    def sound(self):
        print("bow")
class cat(animal):
    def sound(self):
        print("meow")
a=animal()
a.sound()
d=dog()
d.sound()
c=cat()
c.sound()

#overloading method
class cal:
    def add(self,a,b,c=0):
        print(a+b+c)
    def sub(self,a,b,c=0):
        print(a-b-c)
    def mult(self,a,b,c=1):    #defult c=1 for multiply a*b*c(1)
        print(a*b*c)
c=cal()
c.add(1,2)
c.add(1,2,3)
c.sub(3,1)
c.sub(4,5,3)
c.mult(1,2,1)
c.mult(2,2)

