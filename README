# Lbol

Release: 1.0.1

Python package to calculate the bolometric luminosity of a Type II-P Supernova, as published by Bersten, M. C., & Hamuy, M. (2009)

### Current Status

This package has basic functionality. Given a B-V, V-I, or B-I color as well as a V magnitude and distance (in cm) it will calculate the base-10 logarithm of the bolometric luminosity. The directory structure needs to be cleaned up to make importing and using the luminosity module easier.

## Background

Determining the bolometric luminosity of anything is hard. Ideally, one needs to know the distance to the object (hard), and then observe its magnitude at every wavelength (impossible) in order to calculate an apparent bolometric magnitude and convert that to an asbolute bolometric magnitude (or luminosity.)

To solve these challenges, Bersten and Hamuy used three well-observed supernovae (1987A, 1999em, and 2003hn) as templates. These template supernovae had photometric observations in enough bands that they could re-construct approximate bolometric fluxes, filling in the missing UV and far IR with blackbody fits (see the paper for the gritty details.) With these bolometric fluxes, bolometric magnitudes were calculated, using Vega as a zeropoint.

Since most supernovae are not this well-observed, they needed a way to determine the bolometric magnitudes of other supernovae using less information. To do this, they used the tight correlation between the bolometric correction (difference in magnitudes between the observed V band magnitude of the supernova and the apparent bolometric magnitude) and the color of a supernova in the B-V, V-I, and B-I bands. Using the date from the template supernovae, they constructed polynomial fits that can be used to determine the unknown bolometric correction from only the color of a Type II supernova.

The goal of this code is to provide an easy way to take photometric observations of a Type II-P supernova and convert them into bolometric magnitudes.
