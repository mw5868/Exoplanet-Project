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
## Generating a transit model using BATMAN
The BATMAN library is an opensouce code library which enables simple simulation of transit lightcurves using user defined paramenters (Examples above)

```python
import batman
import numpy as np
import matplotlib.pyplot as plt

params = batman.TransitParams()
params.t0 = 0.                       #time of inferior conjunction
params.per = 1.                      #orbital period
params.rp = 0.1                      #planet radius (in units of stellar radii)
params.a = 15.                       #semi-major axis (in units of stellar radii)
params.inc = 87.                     #orbital inclination (in degrees)
params.ecc = 0.                      #eccentricity
params.w = 90.                       #longitude of periastron (in degrees)
params.u = [0.1, 0.3]                #limb darkening coefficients [u1, u2]
params.limb_dark = "quadratic"       #limb darkening model

t = np.linspace(-0.05,0.05,100)

m = batman.TransitModel(params, t)    #initializes model

flux = m.light_curve(params)          #calculates light curve


plt.plot(t,flux)
plt.xlabel("Time from central transit")
plt.ylabel("Relative flux")
plt.show()

```
