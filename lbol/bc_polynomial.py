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
               constants.max_BminusV
    elif color_type == "VminusI":
        return constants.coeff_VminusI, constants.min_VminusI, \
               constants.max_VminusI
    elif color_type == "BminusI":
        return constants.coeff_BminusI, constants.min_BminusI, \
               constants.max_BminusI
    elif type(color_type) != str:
        raise TypeError("The argument given is not a string")
    else:
        raise ValueError("The argument given is not a valid color")

def validity_check(color_value, range_min, range_max):
    if range_min <= color_value <= range_max:
        return True
    else:
        return False
    pass

def bc_color(color, coeff, range_min, range_max):
    """Calculates the bolometric correction, using the polynomial fits
       from Bersten & Hamuy (2009)

       Args:
           color: B-V, V-I, or B-I color of the supernova (corrected for
                  reddening and extinction from the host and MWG)
           coeff: polynomial fit coefficients corresponding to the chosen
                  color
           range_min: minimum value of the polynomial's range of validity
                      for the chosen color
           range_max: maximum value of the polynomial's range of validity
                      for the chosen color
       Returns:
           The bolometric correction for use in calculating the bolometric
           luminosity of the supernova, if the color given is within the
           valid range of the polynomial fit.

           None if the color is outside the valid range
    """
    bc_color = 0.0

    if range_min <= color <= range_max:
        for i in range(len(coeff)):
            bc_color += coeff[i] * color**(i)
    else:
        bc_color = None

    return bc_color

class bcColor():

    def __init__(self, color_value, range_minumum, range_maximum):
        self.color_value   = color_value
        self.range_minumum = range_minumum
        self.range_maximum = range_maximum
        self.result        = 0.0

    def calculate_polynomial_fit(self, coefficient_set):
        for order in range(len(coefficient_set)):
            add_term(calculate_term(order, coefficient_set[order]))
        return self.result

    def add_term(self, step):
      self.result += step

    def calculate_term(self, order, coefficient):
      return coefficient * self.color_value**(order)
