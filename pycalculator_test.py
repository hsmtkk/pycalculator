import pycalculator
import unittest

class TestAdd(unittest.TestCase):
    def testAdd(self):
        want = 3
        got = pycalculator.add(1, 2)
        self.assertEqual(want, got)

if __name__ == '__main__':
    unittest.main()
