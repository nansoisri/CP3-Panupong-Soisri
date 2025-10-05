class Animal:
    def eat(self):
        print("Eating Eating!")

class Cat(Animal):
    name = ""
    def setName(self,text):
        self.name = text
        print("Setting Cat Name = ", self.name)
    def eat(self):
        print("Meow Eating!")

cat1 = Cat()
cat1.name = "Tufu"
cat1.eat()