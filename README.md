# Lbol

Release: 1.0.1

Python package to calculate the bolometric luminosity of a Type II-P Supernova, as published by Bersten, M. C., & Hamuy, M. (2009)

### Current Status

This package has basic functionality. Given a B-V, V-I, or B-I color as well as a V magnitude and distance (in cm) it will calculate the base-10 logarithm of the bolometric luminosity. The directory structure needs to be cleaned up to make importing and using the luminosity module easier.

## Background

Determining the bolometric luminosity of any distant object is difficult. Ideally, one needs to know the distance to the object (hard), and then observe its magnitude at every wavelength (impossible) in order to calculate an apparent bolometric magnitude and convert that to an asbolute bolometric magnitude (or luminosity.)

To solve these challenges, Bersten and Hamuy used three well-observed supernovae (1987A, 1999em, and 2003hn) as templates. These template supernovae had photometric observations in enough bands that the authors could re-construct approximate bolometric fluxes, filling in the missing UV and far IR with blackbody fits (see the paper for the gritty details.) With these bolometric fluxes, bolometric magnitudes were calculated, using Vega as a zeropoint.

Since most supernovae are not this well-observed, the authors needed a way to leverage the template supernovae to determine the bolometric magnitudes of less well-observed supernovae. To do this, they used the tight correlation between the bolometric correction (difference in magnitudes between the observed V band magnitude of the supernova and the apparent bolometric magnitude) and the color of a supernova in the B-V, V-I, and B-I bands. Using the data from the template supernovae, they constructed polynomial fits that can be used to determine the unknown bolometric correction from only the color of a Type II supernova.

The goal of this code is to provide an easy way to take photometric observations of a Type II-P supernova and convert them into bolometric magnitudes.

## Basic Usage

In order to calculate a bolometric luminosity, simply import the `calc_log_Lbol` function from the `luminosity` module. Then, call the function with four arguments:

* The color of the supernova `[float]` (either B-V, V-I, or B-I)
* A string signifying the color you are using `[string]` (either `"BminusV"`, `"VminusI"` or `"BminusI"`)
* The apparent V-band magnitude, corrected for extinction `[float]`
* The distance to the supernova in cm `[float]`

The funcion will return the base-10 logarithm of the bolometric luminosity.

Example:

    >>> from lbol.luminosity import calc_log_Lbol
    >>> calc_log_Lbol(1.014295, "BminusV", 3.918, 1.523E23)
    41.2553

(The numbers in the example above were taked from SN 1987A)

## Planned features

Future releases will include the option to pass the observational error into the function. This will be combined with best estimates of the systematic errors in the luminosity calculation to output the log10 of the luminosity, and an error to go along with it.

