#polymorphism
class car:
    def brand(self):
        print("brand new car")
class BMW(car):
    def brand(self):
        print("m4 model")
class benz(car):
    def brand(self):
        print("b2 model")
def show_brand(vechile:car):
    vechile.brand()

show_brand(car())   # brand new car
show_brand(BMW())   # m4 model
show_brand(benz())  # b2 model

class animal:
    def sound(self):
        print("animal is making sound")
class dog(animal):
    def sound(self):
        print("bow")
class cat(animal):
    def sound(self):
        print("meow")
def show_sound(ani: animal):
    ani.sound()
show_sound(animal())
show_sound(dog())
show_sound(cat())
