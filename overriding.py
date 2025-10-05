class Animal:
    def eat(self):
        print("Eating Eating!")

class Cat(Animal):
    def eat(self):
        print("Meow Eating!")

cat1 = Cat()
cat1.eat()

