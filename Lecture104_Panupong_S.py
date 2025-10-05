class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " +self.lastName+ "'s cart")

P1 = Customer()
P1.name = "Panupong"
P1.lastName = "Soisri"
P1.age = 28
P1.addCart()

P2 = Customer()
P2.name = "Sombat"
P2.lastName = "Batdee"
P2.age = 30
P2.addCart()

P3 = Customer()
P3.name = "Sompong"
P3.lastName = "Longdoo"
P3.age = 25
P3.addCart()