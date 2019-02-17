"""
----------------------------------------------------------------
                    Acme Reports
--------------------------------------------------------------
"""
import random
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Book']

# ____________________________________________
#      Create a list of random products
# ____________________________________________


def generate_products(size=30):
    try:
        err_msg = 'Error:  size argument cannot be 0'
        assert (size != 0), err_msg
        assert (size is not None), err_msg
        prod_list = []
        for i in range(size):
            name = (random.choice(ADJECTIVES) + " " + random.choice(NOUNS))
            price = random.randint(5, 100)
            weight = random.randint(5, 100)
            flammability = random.uniform(0.0, 2.5)
            prod = Product(name, price, weight, flammability)
            prod_list.append([prod.name,
                              prod.price,
                              prod.weight,
                              prod.flammability])
        return prod_list
    except:
        print(err_msg + "Please try again")

# _________________________________________(___
#       Print Inventory Report
# ____________________________________________


def inventory_report(prod_list):
    try:
        err_msg = "Product list is empty.  "
        assert (len(prod_list) > 0), err_msg
        # unzip the product list into separate lists for reporting
        name, price, weight, flammability = zip(*prod_list)
        print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
        print('Unique Product Names:', len(set(name)))
        print('Average Price:', sum(price)/len(price))
        print('Average Weight:', sum(weight)/len(weight))
        print('Average flammability:', sum(flammability)/len(flammability))
    except:
        print(err_msg)

#  Launched from the command line
if __name__ == '__main__':
    inventory_report(generate_products())