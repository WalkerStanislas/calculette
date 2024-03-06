import unittest
import function_add
import numpy as np
class TestAddition(unittest.TestCase):
    def test_deux_zeros(self):
        self.assertEqual(function_add.add(0,0),0)
    def test_pi_nombre(self):
        self.assertAlmostEqual(function_add.add(np.pi,1),np.pi + 1)

if __name__ == "__main__":
    unittest.main()