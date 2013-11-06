import unittest
import lbol.bc_polynomial as bc_polynomial
import lbol.constants as constants

class TestBolometricCorrection(unittest.TestCase):

    def test_set_coefficients_to_BminusV(self):
       expected = constants.coeff_BminusV
       result = bc_polynomial.set_coefficients("BminusV")
       self.assertEqual(expected, result)
   
    def test_set_coefficients_to_VminusI(self):
       expected = constants.coeff_VminusI
       result = bc_polynomial.set_coefficients("VminusI")
       self.assertEqual(expected, result)

    def test_set_coefficients_to_BminusI(self):
       expected = constants.coeff_BminusI
       result = bc_polynomial.set_coefficients("BminusI")
       self.assertEqual(expected, result)

    def test_set_coefficients_bad_argument_type(self):
       self.assertRaises(TypeError, bc_polynomial.set_coefficients, 2)

    def test_set_coefficients_bad_argument_value(self):
        self.assertRaises(ValueError, bc_polynomial.set_coefficients, 'Hello')

if __name__ == '__main__':
    unittest.main()
