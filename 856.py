import unittest

def multiply(a,b):
    return a*b

class Testmultiply(unittest.TestCase):
    def test_multiply(self):

        self.assertEqual(multiply(4,5) , 20)

unittest.main()