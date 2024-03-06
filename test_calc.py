import unittest





def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Erreur division par 0"
    return a / b


class TestAddition(unittest.TestCase):
    def test_deux_zero(self):
        self.assertEqual(add(1, 2), 3, "1 + 2 = 3")

    def test_decimaux(self):
        self.assertEqual(add(6.1, 4.7), 10.8)

    def test_negatifs(self):
        self.assertAlmostEqual(add(5, 0.1), 5.1)

    def test_entiers(self):
        self.assertEqual(add(5, 7), 12)


class TestSoustraction(unittest.TestCase):
    def test_deux_zero(self):
        self.assertEqual(sub(0, 0), 0)

    def test_decimaux(self):
        self.assertAlmostEqual(sub(6.1, 4.7), 1.4)

    def test_negatifs(self):
        self.assertAlmostEqual(sub(-2.1, -3.4), 1.3)

    def test_resultat_negatif(self):
        self.assertEqual(sub(5, 7), -2)


class TestMultiplication(unittest.TestCase):
    def test_deux_zero(self):
        self.assertEqual(mul(0, 0), 0)

    def test_decimaux(self):
        self.assertEqual(mul(1.1, 2), 2.2)

    def test_negatifs(self):
        self.assertEqual(mul(-7, 8), -56)

    def test_entiers(self):
        self.assertAlmostEqual(mul(5, 7), 35)


class TestDivision(unittest.TestCase):
    def test_divide_by_zero(self):
        self.assertEqual(div(5, 0), "Erreur division par 0")

    def test_entiers(self):
        self.assertEqual(div(15, 5), 3)

    def test_decimaux(self):
        self.assertAlmostEqual(div(30.6, 6), 5.1)


if __name__ == "__main__":
    unittest.main()

    
