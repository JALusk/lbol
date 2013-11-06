import unittest
import lbol.bc_polynomial as bc_polynomial
import lbol.constants as constants

class TestBolometricCorrection(unittest.TestCase):

    def test_set_coefficients_to_BminusV(self):
       expected = constants.coeff_BminusV
       result = bc_polynomial.set_constants("BminusV")[0]
       self.assertEqual(expected, result)
   
    def test_set_coefficients_to_VminusI(self):
       expected = constants.coeff_VminusI
       result = bc_polynomial.set_constants("VminusI")[0]
       self.assertEqual(expected, result)

    def test_set_coefficients_to_BminusI(self):
       expected = constants.coeff_BminusI
       result = bc_polynomial.set_constants("BminusI")[0]
       self.assertEqual(expected, result)

    def test_set_range_min_to_BminusV(self):
       expected = constants.min_BminusV
       result = bc_polynomial.set_constants("BminusV")[1]
       self.assertEqual(expected, result)

    def test_set_range_min_to_VminusI(self):
       expected = constants.min_VminusI
       result = bc_polynomial.set_constants("VminusI")[1]
       self.assertEqual(expected, result)

    def test_set_range_min_to_BminusI(self):
       expected = constants.min_BminusI
       result = bc_polynomial.set_constants("BminusI")[1]
       self.assertEqual(expected, result)

    def test_set_range_max_to_BminusV(self):
       expected = constants.max_BminusV
       result = bc_polynomial.set_constants("BminusV")[2]
       self.assertEqual(expected, result)

    def test_set_range_max_to_VminusI(self):
       expected = constants.max_VminusI
       result = bc_polynomial.set_constants("VminusI")[2]
       self.assertEqual(expected, result)

    def test_set_range_max_to_BminusI(self):
       expected = constants.max_BminusI
       result = bc_polynomial.set_constants("BminusI")[2]
       self.assertEqual(expected, result)

    def test_set_constants_bad_argument_type(self):
       self.assertRaises(TypeError, bc_polynomial.set_constants, 2)

    def test_set_constants_bad_argument_value(self):
        self.assertRaises(ValueError, bc_polynomial.set_constants, 'Hello')

if __name__ == '__main__':
    unittest.main()
