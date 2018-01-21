# Exoplanet Project
This repo is designed to provide educational resources related to the study of exoplanetary science.

## What are exoplanets?
Exoplanets are planets which orbit stars that are not our own Sun.

## Exoplanet Transit Lightcurve
![alt text](https://www.google.co.uk/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwig9_6tyunYAhVFCsAKHWdvC5AQjRwIBQ&url=http%3A%2F%2Fwww.phy.cuhk.edu.hk%2Fsure%2Fcomments_2015%2Fckw_pre.pdf&psig=AOvVaw0iTUVXPTLjJVv9P6yI9mFX&ust=1516642122231146 "Example Transit")


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
