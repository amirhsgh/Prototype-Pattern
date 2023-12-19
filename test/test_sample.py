import unittest
from models import User, Order, Item


class TestSample(unittest.TestCase):

    def test_clone_method_exists(self):
        user1 = User("ali", "alavi", "Tehran, ...")
        order1 = Order(1, user1, "Kish, ...")
        order1.clone()
        
    def test_clone_output_type(self):
        user1 = User("ali", "alavi", "Tehran, ...")
        order1 = Order(1, user1, "Kish, ...")
        order2 = order1.clone()
        self.assertIsInstance(order2, Order)