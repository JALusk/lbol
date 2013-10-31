import unittest
import lbol.correction as correction

class bcColor_TestCase(unittest.TestCase):
    def setUp(self):
        self.color_value   = 15
        self.range_minumum = 13
        self.range_maximum = 42

        self.color = correction.bcColor(
            self.color_value,
            self.range_minumum,
            self.range_maximum
        )

    def test_calculate_term(self):
        order       = 2
        coefficient = 0.37645654
        expected    = 84.7027215
        calculated  = self.color.calculate_term(order, coefficient)
        self.assertEqual(expected, calculated)

if __name__ == '__main__':
    import BC_color_TestCase
    unittest.main()
