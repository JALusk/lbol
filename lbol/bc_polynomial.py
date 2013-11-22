import constants
import math

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
           color for which the polynomial is valid, the maximum value of the 
           color for which the polynomial is valid, and the rms error of the
           polynomial fit for the supplied color.

           ([coefficients], min, max, rms_error)

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

def calculate_polynomial_term(coefficient, variable, order):
    """Calculates a term in a polynomial

    Args:
        coefficient: FLOAT which is the coefficient to use in calculating
            the polynomial term.
        variable: FLOAT to plug in for the variable in the polynomial term.
        order: INTEGER to use as the order of the polynomial term.

    Returns:
        FLOAT which is the result of coefficient * variable**(order)

    Raises:
        TypeError if a non-integer order is given
    """
    if type(order) != int:
        raise TypeError('Non-integer order in polynomial')
    else:
        return coefficient * variable**(order)

def calculate_polynomial(coefficients, variable):
    """Calculates a polynomial

       Args:
           coefficients: LIST of polynomial coefficients. The length
               of the list will be used as the order of the polynomial.
           variable: FLOAT to plug in for the variable in the polynomial.
       Returns:
           FLOAT, which is the result of summing the polynomial terms
           calculated from the coefficients and variable given.
    """
    polynomial = 0.0

    for order in range(len(coefficients)):
        polynomial += calculate_polynomial_term(coefficients[order],
                                                variable,
                                                order)
    return polynomial

def calculate_derivative_term(coefficient, variable, order):
    """Calculates a term in the derivative of a polynomial
    """
    if type(order) != int:
        raise TypeError('Non-integer order in polynomial')
    else:
        return order * coefficient * variable**(order - 1)

def quadrature_sum(x, y):
    """Calculate the quadrature sum of two variables x and y
    """
    return math.sqrt(x**2 + y**2)

def calc_bolometric_correction_err(color_value, color_err, color_type):
    """Calculates the uncertainty in the bolometric correction

       Two uncertainties are added in quadrature to get the total
       uncertainty in the bolometric correction. The first is uncertainty
       in the BC due to uncertainties in the measured color value (simple
       error propagation using a derivative.) The second is the RMS error
       inherent in the polynomial fit to the template data as reported in
       Bersten & Hamuy (2009.)

       Args:
           color_value: B-V, V-I, or B-I color of the supernova in
               magnitudes (corrected for reddening and extinction from
               the host and MWG)
           color_err: Uncertainty in the photometric color.
           color_type: String signifying which color color_value represents.

   """
    coefficients = set_constants(color_type)[0]
    rms_err = set_constants(color_type)[3]
    bc_derivative = 0.0
    
    for order in range(1,len(coefficients)):
        bc_derivative += calculate_derivative_term(coefficients[order],
                                                   color_value, order)
  
    bc_polynomial_err = abs(bc_derivative) * color_err
    bolometric_correction_uncertainty = quadrature_sum(bc_polynomial_err, 
                                                       rms_err)
    return bolometric_correction_uncertainty

def calc_bolometric_correction(color_value, color_err, color_type):
    """Calculates the bolometric correction, using the polynomial fits
       from Bersten & Hamuy (2009)

       Args:
           color_value: B-V, V-I, or B-I color of the supernova in
               magnitudes (corrected for reddening and extinction from
               the host and MWG)
           color_err: Uncertainty in the photometric color.
           color_type: String signifying which color color_value represents.
               Valid values are "BminusV" for B-V, "VminusI" for V-I, and
               "BminusI" for B-I.
       Returns:
           A tuple containing the bolometric correction for use in 
           calculating the bolometric luminosity of the supernova, and the 
           uncertainty in that bolometric correction (if the color given 
           is within the valid range of the polynomial fit.)

           (bolometric_correction, uncertainty)

           (None, None) if the color is outside the valid range
    """
    bolometric_correction = 0.0

    coefficients, range_min, range_max, rms_err = set_constants(color_type)

    if valid_color(color_value, range_min, range_max):
        bolometric_correction = calculate_polynomial(coefficients,
                                                    color_value)
        uncertainty = calc_bolometric_correction_err(color_value,
                                                     color_err,
                                                     color_type) 
    else:
        bolometric_correction = None
        uncertainty = None

    return bolometric_correction, uncertainty
