"""
----------------------------------------------------------------
            Acme Class Library
----------------------------------------------------------------
"""
import random


class Product:
    # __________________________________________
    #                Product Class
    # __________________________________________

    # Contructor
    def __init__(self,
                 name: str,
                 price=int(10),
                 weight=int(20),
                 flammability=float(0.5)):
        try:
            # check for null arguments
            err_msg = "Name cannot be blank. "
            assert (name != ""), err_msg
            assert (name is not None), err_msg
            err_msg = "Weight cannot be 0. "
            assert (weight != 0), err_msg
            assert (weight is not None), err_msg
            err_msg = "Price cannot be 0. "
            assert (price != 0), err_msg
            assert (price is not None), err_msg
            err_msg = "Flammability cannot be 0. "
            assert (flammability != 0), err_msg
            assert (flammability is not None), err_msg
            # assign args to class properties(fields)
            self.name = name
            self.price = price
            self.weight = weight
            self.flammability = flammability
            self.identifier = random.randint(1000000, 9999999)
            return
        except:
            #  error message
            print(err_msg + "Please try again")
    # ____________________________________________
    #       Methods
    # ____________________________________________

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
    # _________________________________
    #        BoxingGlove Class
    # _________________________________
    def __init__(self,
                 name: str,
                 price=int(10),
                 weight=int(10),
                 flammability=float(0.5)):
        Product.__init__(self, name, price, weight, flammability)
        return
    # ____________________________________________
    #       Methods
    # ____________________________________________

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