from bc_polynomial import calc_bolometric_correction as bc
import bc_polynomial
import constants
import math

def calc_log_Fbol(color_value, color_err, color_type, v_magnitude,
                  v_magnitude_err):
    """Calculates the log10 of the bolometric flux of a Type II-P supernova.

    Args:
        color_value: B-V, V-I, or B-I color of the supernova in 
            magnitudes (corrected for reddening and extinction from 
            the host and MWG)
        color_err: Uncertainty in the photometric color.
        color_type: String signifying which color color_value represents.
            Valid values are "BminusV" for B-V, "VminusI" for V-I, and
            "BminusI" for B-I.
        v_magnitude: Photometric magnitude in the V band, corrected for
            host + MWG extinction
        v_magnitude_err: Uncertainty in the V band magnitude after correction
            for host + MWG extinction

    Returns:
        A tuple containing the base-10 logarithm of the bolometric flux used 
        when calculating the bolometric luminosity, and the uncertainty in
        that number.

        (log_Fbol, uncertainty)

        (None, None) if the bolometric correction calculated from the 
        color_value and color_type is None (which means the observed color
        is outside the range of validity of the polynomial fit.)
    """ 
    bolometric_correction, bc_err = bc(color_value, color_err, color_type)

    if bolometric_correction == None:
        log_Fbol = None
        log_Fbol_uncertainty = None
    else:
        log_Fbol = -0.4 * (bolometric_correction + v_magnitude
                       + constants.mbol_zeropoint)
        log_Fbol_uncertainty = 0.4 * (bc_err + v_magnitude_err)
    
    return log_Fbol, log_Fbol_uncertainty

def calc_log_4piDsquared(distance, distance_err):
    """Calculates the log10 of 4*pi*D^2, the proportionality between
       luminosity and flux.

    Args:
        distance: The distance to the supernova
        distance_err: The uncertainty in the distance to the supernova

    Returns:
        A tuple containing the base-10 logarithm of 4*pi*D^2, and the
        luminosity of this number.

        (log_4piDsquared, uncertainty)
    """
    log_4piDsquared = math.log(4.0 * math.pi * distance**2.0, 10)
    log_4piDsquared_uncertainty = 2.0 / (math.log(10) * distance) * \
                                  distance_err
    
    return log_4piDsquared, log_4piDsquared_uncertainty

def calc_log_Lbol(color_value, color_err, color_type, v_magnitude,  
                  v_magnitude_err, distance, distance_err):
    """Calculates the bolometric luminosity of a Type II-P Supernova using
       the method of Bersten & Hamuy (2009)

    Args:
        color_value: B-V, V-I, or B-I color of the supernova in 
            magnitudes (corrected for reddening and extinction from 
            the host and MWG)
        color_err: Uncertainty in the photometric color.
        color_type: String signifying which color color_value represents.
            Valid values are "BminusV" for B-V, "VminusI" for V-I, and
            "BminusI" for B-I.
        v_magnitude: Photometric magnitude in the V band, corrected for
            host + MWG extinction
        v_magnitude_err: Uncertainty in the V band magnitude after correction
            for host + MWG extinction
        distance: The distance to the supernova in centimeters
        distance_err: The uncertainty in the distance to the supernova
 
    Returns:
        A tuple containing the value of the base-10 logarithm of the 
        bolometric luminosity in ergs per second, and the uncertainty
        in that value.

        (log_Lbol, uncertainty)

        (None, None) if the bolometric correction is None (which means the
        observed color value is outside the range of vaidity of the 
        polynomial fit used to determine the bolometric correction.)
    """
    log_Fbol, log_Fbol_err = calc_log_Fbol(color_value, color_err, 
                                           color_type, v_magnitude, 
                                           v_magnitude_err)
    log_4piDsquared, log_4piDsquared_err = calc_log_4piDsquared(distance, 
                                                              distance_err)
    
    if log_Fbol == None:
        log_Lbol = None
        log_Lbol_uncertainty = None
    else:
        log_Lbol = log_Fbol + log_4piDsquared
        log_Lbol_uncertainty = bc_polynomial.quadrature_sum(log_Fbol_err, 
                                                      log_4piDsquared_err)

    return log_Lbol, log_Lbol_uncertainty
