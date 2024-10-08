class animal:

    def __init__(self,name):
        self.name = name
        self.is_Alive = True


    def eat(self):
        print(f"{self.name}is eating...")

    def sleep(self):
        print(f"{self.name} is sleeping...")

class Dog(animal):  #Child class takes arguments and attributes of parent class
    pass

class Cat(animal):
    pass

class Penguin(animal):
    pass

dog = Dog("Scooby")
cat = Cat("Garfield")
penguin = Penguin("Linux")

print(dog.name)
print(dog.eat)

print(penguin.name)
print(penguin.eat)
print(penguin.is_Alive)