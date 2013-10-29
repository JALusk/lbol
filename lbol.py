import math

# Coefficients for polynomial fit to bolometric correction - color relation
coeff_BminusV = [-0.823, 5.027, -13.409, 20.133, -18.096, 9.084, -1.950]
coeff_VminusI = [-1.355, 6.262, -2.676, -22.973, 35.524, -15.340]
coeff_BminusI = [-1.096, 3.038, -2.246, -0.497, 0.7078, 0.576, -0.713,
                 0.239, -0.027]

# Bolometric correction
def bc_color(color, coeff):
    """Calculates the bolometric correction, using the polynomial fits
       from Bersten & Hamuy (2009)

       Args:
           color: B-V, V-I, or B-I color of the supernova
           coeff: polynomial fit coefficients corresponding to the chosen
                  color
       Returns:
           The bolometric correction for use in calculating the bolometric
           luminosity of the supernova
    """
    bc_color = 0.0

    for i in range(len(coeff)):
        bc_color += coeff[i] * color**(i)

    return bc_color
        
        

# Bolometric luminosity
def calc_lbol(bolometric_corr, v_magnitude, extinction, distance_cm):
    """Calculates the bolometric luminosity of a Type II-P Supernova using
       the method of Bersten & Hamuy (2009)
       
       Args:
           bolometric_corr: bolometric correction as calculated by
                                  bc_color()
           v_magnitude: Observed V-band magnitude
           extinction: Observed Atotal(V) extinction (host + MWG)
           distance_cm: Distance in centimeters
       
       Returns:
           The value of the bolometric luminosity in ergs per second
    """
    
    logL = -0.4 * (bolometric_corr + v_magnitude - extinction + 11.64) + \
           math.log(4.0 * math.pi * distance_cm**(2), 10)
    
    return logL
