import random


class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(100000, 9999999)):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        quotient = (self.price) / (self.weight)
        if quotient < 0.5:
            return "Not so stealable..."
        elif quotient >= 0.5 and quotient < 1.0:
            return "Kinda stealable."
        else:
            return "very stealable"

    def explode(self):
        product = (self.flammability) * (self.weight)
        if product < 10:
            return "....fizzle"
        elif product >= 10 and product < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(
        self,
        name,
        price=10,
        weight=10,
        flammability=0.5,
        identifier=random.randint(
            100000,
            9999999)):
        super().__init__(
            name,
            price,
            weight=20,
            flammability=0.5,
            identifier=random.randint(
                100000,
                9999999))

    def explode(self):
        return "...it's a glove"

    def punch(self, weight):
        if weight < 5:
            return "That tickles"
        elif weight >= 5 and weight < 15:
            return "Hey that hurt!"
        else:
            return "Ouch!"
