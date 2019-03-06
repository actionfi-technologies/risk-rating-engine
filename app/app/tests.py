from django.test import TestCase
from app.calc import add, subtract

class ClacTests(TestCase):
    """docstring for .
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg"""
    def test_add_numbers(self):
        """Test that 2 numbers are added together"""
        self.assertEqual(add(3,8),11)

    def test_subtract_numbers(self):
        """Test values are subtracted and returned"""
        self.assertEqual(subtract(5,11),6)
