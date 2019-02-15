"""
    Utility Module for Acme Products
"""
from collections import defaultdict
from acme import Product
import random
import pandas as pd

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Book']


def generate_products(size=30):
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


def inventory_report(prod_list):
    prod_df = pd.DataFrame(prod_list)
    prod_df.rename(columns={0: 'name',
                            1: 'price',
                            2: 'weight',
                            3: 'flammability'},
                   inplace=True)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique Product Names:', len(set(prod_df.name)))
    print('Average Price:', prod_df.price.mean())
    print('Average Weight:', prod_df.weight.mean())
    print('Average flammability:', prod_df.flammability.mean())


def inventory_report_new(prod_list):
    print(prod_list)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    # print('Unique Product Names:', len(set(prod_df.name)))
    # print('Average Price:', prod_df.price.mean())
    # print('Average Weight:', prod_df.weight.mean())
    # print('Average flammability:', prod_df.flammability.mean())

if __name__ == '__main__':
    inventory_report(generate_products())