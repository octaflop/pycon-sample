import unittest


class SimpleTest(unittest.TestCase):

    def test(self):
        num1 = 22
        num2 = 28
        self.assertEqual(num1, num2)


if __name__ == '__main__':
    unittest.main()
