from lbol.bc_polynomial import calc_bolometric_correction as bc
import lbol.constants as constants
import math
def calc_log_Fbol(color_value, color_type, v_magnitude):

    bolometric_correction = bc(color_value, color_type)

    if bolometric_correction == None:
        log_Fbol = None
    else:
        log_Fbol = -0.4 * (bolometric_correction + v_magnitude
                       + constants.mbol_zeropoint)
    
    return log_Fbol

def calc_log_4piDsquared(distance):
    log_4piDsquared = math.log(4.0 * math.pi * distance**2.0, 10)
    
    return log_4piDsquared

def calc_log_Lbol(color_value, color_type, v_magnitude, distance):
    """Calculates the bolometric luminosity of a Type II-P Supernova using
       the method of Bersten & Hamuy (2009)

       Args:
           bolometric_corr: bolometric correction as calculated by
                            bc_color()
           v_magnitude: V-band apparent magnitude, corrected for exctinction
                        (host + MWG)
           distance_cm: Distance to the supernova in centimeters

       Returns:
           The value of the bolometric luminosity in ergs per second if the
           bolometric correction is not None

           None if the bolometric correction is None (invalid color)
    """
    log_Fbol = calc_log_Fbol(color_value, color_type, v_magnitude)
    log_4piDsquared = calc_log_4piDsquared(distance)
    
    if log_Fbol == None:
        log_Lbol = None
    else:
        log_Lbol = log_Fbol + log_4piDsquared

    return log_Lbol
