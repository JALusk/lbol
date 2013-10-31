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

    def fit(self, coefficient_set):
        for index in range(len(coefficient_set)):
            add_term(calculate_term(index, coefficient_set[index]))
        return self.result

    def add_term(self, step):
      self.result += step

    def calculate_term(self, index, coefficient):
      return coefficient * self.color_value**(index)
