from datetime import datetime

import unittest

from ..stock import Stock


class StockTest(unittest.TestCase):

    def setUp(self):
        self.goog = Stock("GOOG")

    def test_price_of_a_new_stock_class_shoulb_be_None(self):
        self.assertIsNone(self.goog.price)

    def test_stock_update(self):
        """
        An update should set the price on the stock object
        We will be using the 'datetime' module for the timestamp
        This test follows the pattern Arrange-Act-Assert
        """
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.assertEqual(10, self.goog.price)

    def test_negative_price_should_throw_ValueError(self):
        with self.assertRaises(ValueError):
            self.goog.update(datetime(2014, 2, 13), -13)

    def test_stock_price_should_give_the_latest_price(self):
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.goog.update(datetime(2014, 2, 13), price=8.4)
        self.assertAlmostEqual(8.4, self.goog.price, delta=0.0001)
