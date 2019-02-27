class Dog():
    # class object attribute
    species = "mammal"
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog("Lab","boi")
print(mydog.breed)
print(mydog.name)
print(mydog.species)

class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*Circle.pi

    def set_radius(self,new_r):
        self.radius = new_r

myc = Circle(3)
print(myc.area())
myc.set_radius(100)
print(myc.area())

# Inheritance
class Animal():
    def __init__(self):
        print("animal created")

    def whoAmI(self):
        print("animal")

    def eat(self):
        print("eating")

class Dog(Animal):
    def __init__(self):
        # Animal.__init__(self)
        print("dog created")

    def bark(self):
        print("woof")

    def eat(self):
        print("dog eating")


mya = Animal()
mya.whoAmI()
mya.eat()

mydog = Dog()
mydog.whoAmI()
mydog.eat()

# Special Methods
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("destroyed the book!")

b = Book("Python","nathan",200)
print(b)
print(len(b))
del b
