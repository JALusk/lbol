def log_lbol(bolometric_corr, v_magnitude, distance_cm):
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
        logFbol = -0.4 * (bolometric_corr + v_magnitude + 11.64)
        log4piD = math.log(4.0 * math.pi * distance_cm**(2), 10)

        logL = logFbol + log4piD

    return logL
