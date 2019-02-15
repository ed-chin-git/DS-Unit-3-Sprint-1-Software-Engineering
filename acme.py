import random

# for x in range(10):
#  print random.randint(1,101)


class Product:
    """  Product Class
    """
    def __init__(self, 
                 name: str, 
                 price=int(10), 
                 weight=int(20), 
                 flammability=float(0.5)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        steal_ratio = self.price / self.weight
        if steal_ratio < 0.5:
            return "Not so stealable..."
        else:
            if steal_ratio > 1:
                return "Very stealable!"
            else:
                return "Kinda stealable"

    def explode(self):
        flammability_factor = self.flammability * self.weight
        if flammability_factor < 10:
            return "...fizzle"
        else:
            if flammability_factor > 50:
                return "...BABOOM!!"
            else:
                return "...boom!"


class BoxingGlove(Product):
    """  Product Class
    """
    def __init__(self, name: str):
        Product.__init__(self, name)
        self.weight = int(10)

    def explode(self):
        return "...it's a glove"

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        else:
            if self.weight > 15:
                return "OUCH!"
            else:
                return "Hey that hurt!"