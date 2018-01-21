# Exoplanet Project
This repo is designed to provide educational resources related to the study of exoplanetary science.
>Astronomy reseach and outreach, exoploring and discovering Other Worlds!

## What are exoplanets?
Exoplanets are planets which orbit stars that are not our own Sun.

>As of early 2018 there are over 3500 confirmed exoplanets in 594 mulit-planet systems.

A lot of the data this tutorial will use will be pulled from the [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/index.html)
The archive is a repository of opensource data collated from a number of observatories, including the famous KEPLER space telescope. 


## Exoplanet Transit Lightcurve
![alt text](http://www.exoplanetproject.co.uk/uploads/6/9/9/9/6999140/9299476_orig.jpg "Example Transit")


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
