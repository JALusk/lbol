import unittest
from lbol.bc_polynomial import calc_bolometric_correction as bc
import lbol.luminosity as luminosity
import lbol.constants as constants
import math


class TestLogLbol(unittest.TestCase):
    
    def setUp(self):
        self.color_value = 0.5
        self.color_type = "BminusV"
        self.v_magnitude = 16.59
        self.distance = 1.54E23
    
    def test_log_Fbol_calculation(self):
        expected = -0.4 * (bc(self.color_value, self.color_type) 
                          + self.v_magnitude + constants.mbol_zeropoint)
        result = luminosity.calc_log_Fbol(self.color_value, self.color_type,
                                         self.v_magnitude)
        self.assertEqual(expected, result)

    def test_log_Fbol_is_None_if_bc_is_None(self):
        color_value = 123.0
        expected = None
        result = luminosity.calc_log_Fbol(color_value, self.color_type,
                                          self.v_magnitude)
        self.assertEqual(expected, result)

    def test_log_4piDsquared_calculation(self):
        expected = math.log(4.0 * math.pi * self.distance**2.0, 10)
        result = luminosity.calc_log_4piDsquared(self.distance)
        self.assertEqual(expected, result)

    def test_log_Lbol(self):
        expected = -0.4 * (bc(self.color_value, self.color_type) 
                          + self.v_magnitude + constants.mbol_zeropoint) \
                   + math.log(4.0 * math.pi * self.distance**2.0, 10)
        result = luminosity.calc_log_Lbol(self.color_value, self.color_type,
                                          self.v_magnitude, self.distance)
        self.assertEqual(expected, result)
    
    def test_log_Lbol_is_None_if_bc_is_None(self):
        color_value = 123.0
        expected = None
        result = luminosity.calc_log_Lbol(color_value, self.color_type,
                                          self.v_magnitude, self.distance)
        self.assertEqual(expected, result)
