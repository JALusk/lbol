import constants

def set_constants(color_type):
    """Sets the coefficients and valid range bounds based on what color
       is being used to determine the bolometric correction.

       Args:
           color_type: A string specifying the color combination. Must
               be "BminusV" for B-V, "VminusI" for V-I, or "BminusI" for
               B-I.

       Returns:
           A tuple containing the list of coefficients for the polynomial fit
           which correspond to the supplied color, the minimum value of the
           color for which the polynomial is valid, and the maximum value of
           the color for which the polynomial is valid

           [coefficients], min, max

       Raises:
           TypeError: The argument given is not a string
           ValueError: The argument given is not one of the three valid
               strings.
    """
    if color_type == "BminusV":
        return constants.coeff_BminusV, constants.min_BminusV, \
               constants.max_BminusV, constants.rms_err_BminusV
    elif color_type == "VminusI":
        return constants.coeff_VminusI, constants.min_VminusI, \
               constants.max_VminusI, constants.rms_err_VminusI
    elif color_type == "BminusI":
        return constants.coeff_BminusI, constants.min_BminusI, \
               constants.max_BminusI, constants.rms_err_BminusI
    elif type(color_type) != str:
        raise TypeError("The argument given is not a string")
    else:
        raise ValueError("The argument given is not a valid color")

def valid_color(color_value, range_min, range_max):
    """Checks that the color_value is within the bounds set by range_min
       and range_max. Returns True or False
    """
    if range_min <= color_value <= range_max:
        return True
    else:
        return False

def calculate_term(coefficient, variable, order):
    """Calculates a term in a polynomial
    """
    if type(order) != int:
        raise TypeError('Non-integer order in polynomial')
    else:
        return coefficient * variable**(order)

def calc_bolometric_correction(color_value, color_type):
    """Calculates the bolometric correction, using the polynomial fits
       from Bersten & Hamuy (2009)

       Args:
           color_value: B-V, V-I, or B-I color of the supernova in
               magnitudes (corrected for reddening and extinction from
               the host and MWG)
           color_type: String signifying which color color_value represents.
               Valid values are "BminusV" for B-V, "VminusI" for V-I, and
               "BminusI" for B-I.
       Returns:
           The bolometric correction for use in calculating the bolometric
           luminosity of the supernova, if the color given is within the
           valid range of the polynomial fit.

           None if the color is outside the valid range
    """
    bolometric_correction = 0.0

    coefficients, range_min, range_max, rms_err = \
                                              set_constants(color_type)

    if valid_color(color_value, range_min, range_max):
        for order in range(len(coefficients)):
            bolometric_correction += calculate_term(coefficients[order],
                                                    color_value, order)
    else:
        bolometric_correction = None

    return bolometric_correction
