# Exoplanet Project
This repo is designed to provide educational resources related to the study of exoplanetary science.

## What are exoplanets?
Exoplanets are planets which orbit stars that are not our own Sun.

![alt text](https://en.wikipedia.org/wiki/Methods_of_detecting_exoplanets#/media/File:Planetary_transit.svg "Example Transit")


## Transit Basics
Transit elements are fairly easy to quantify with the following parameters

```python
t0 = 0.                       #time of inferior conjunction
per = 1.                      #orbital period
rp = 0.1                      #planet radius (in units of stellar radii)
a = 15.                       #semi-major axis (in units of stellar radii)
inc = 87.                     #orbital inclination (in degrees)
ecc = 0.                      #eccentricity
w = 90.                       #longitude of periastron (in degrees)
u = [0.1, 0.3]                #limb darkening coefficients [u1, u2]
limb_dark = "quadratic"       #limb darkening model

```
