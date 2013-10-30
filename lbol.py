import math

# Coefficients for polynomial fit to bolometric correction - color relation
coeff_BminusV = [-0.823, 5.027, -13.409, 20.133, -18.096, 9.084, -1.950]
coeff_VminusI = [-1.355, 6.262, -2.676, -22.973, 35.524, -15.340]
coeff_BminusI = [-1.096, 3.038, -2.246, -0.497, 0.7078, 0.576, -0.713,
                 0.239, -0.027]

# Ranges of validity for polynomial fits
min_BminusV = -0.2
max_BminusV = 1.65
min_VminusI = -0.1
max_VminusI = 1.0
min_BminusI = -0.4
max_BminusI = 3.0

# Bolometric correction
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

# Bolometric luminosity
def calc_lbol(bolometric_corr, v_magnitude, distance_cm):
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
    if bolometric_corr == None:
        logL = None
    else:
        logL = -0.4 * (bolometric_corr + v_magnitude + 11.64) + \
               math.log(4.0 * math.pi * distance_cm**(2), 10)
    
    return logL
