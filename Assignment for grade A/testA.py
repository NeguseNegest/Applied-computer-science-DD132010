#Deployed a testing file that checks that all outputs are as expected, particular cases of when n is outside the allowed bound, n is odd and even.

import unittest
import Alabbb

class TestAlabbb(unittest.TestCase):

    def test_low_n(self):
        with self.assertRaises(Exception): 
            Alabbb.compute(1)  

    def test_high_n(self):
        # Here we assume that the program should at least be able to handle n = 10000. 
        # Depending on the actual performance of your program, you might want to adjust this number.
        result = Alabbb.compute(10000)
        self.assertIsInstance(result, str)

    def test_odd_even_n(self):
        # We check that for odd n, the largest number starts with '7', and for even n, it starts with '1'
        odd_result = Alabbb.compute(21)
        self.assertTrue(odd_result.split()[1].startswith('7'))
        even_result = Alabbb.compute(22)
        self.assertTrue(even_result.split()[1].startswith('1'))

if __name__ == '__main__':
    unittest.main()
