"""
----------------------------------------------------------------
            Acme Unit Tests
-----------------------------------------------------------
"""
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Test default flammability over 50."""
        prod1 = Product('Test Product', flammability=51, weight=1)
        self.assertEqual(prod1.explode(), "...BABOOM!!")
        """Test default flammability UNDER 10"""
        prod2 = Product('Test Product', flammability=9, weight=1)
        self.assertEqual(prod2.explode(), "...fizzle")
        """Test default flammability BETWEEN 10 & 49"""
        prod3 = Product('Test Product', flammability=10, weight=1)
        self.assertEqual(prod3.explode(), "...boom!")

    def test_default_product_stealability(self):
        """Test default stealability ratio over 1.0 """
        prod1 = Product('Test Product', price=14, weight=30)
        self.assertEqual(prod1.stealability(), "Not so stealable...")
        prod2 = Product('Test Product', price=15, weight=30)
        self.assertEqual(prod2.stealability(), "Kinda stealable")
        prod3 = Product('Test Product', price=15, weight=15)
        self.assertEqual(prod3.stealability(), "Kinda stealable")
        prod4 = Product('Test Product', price=16, weight=15)
        self.assertEqual(prod4.stealability(), "Very stealable!")


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme Reports are OK"""
    def test_default_num_products(self):
        """Test default number product items being 30."""
        prod_list = generate_products()
        self.assertEqual(len(prod_list), 30)

    def test_legal_names(self):
        """Test if generated product names are valid."""
        prod_list = generate_products()
        # unzip the product list into separate lists for testing
        names, prices, weights, flammability = zip(*prod_list)
        valid_words = ADJECTIVES + NOUNS
        for name in names:
            words = name.split() 
            for word in words:
                self.assertIn(word, valid_words)

if __name__ == '__main__':
    unittest.main()