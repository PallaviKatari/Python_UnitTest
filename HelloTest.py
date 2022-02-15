import unittest
from Hello import greeting

class TestingHelloWorld(unittest.TestCase):
    def test_helloworld(self):
        self.assertEqual(greeting(),'HelloWorld!')

if __name__ == '__main__':
    unittest.main()