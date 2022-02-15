import unittest

class FirstUnitTest(unittest.TestCase):
    def test_upper(self):
        result= 'jktech'.upper()
        self.assertEqual(result, 'JKTECH')

class Greater_Then_2(unittest.TestCase):
    def __init__(self):
        self.numbers = [1,2,5,9,5,67,43,1,4,2,1,0]

    def greater_2(self):
        expected = [i for i in self.numbers if i < 2 ]
        print(expected)
        print(self.numbers)
        self.assertEqual(self.numbers, expected)

if __name__ == "__main__":
    unittest.main()
