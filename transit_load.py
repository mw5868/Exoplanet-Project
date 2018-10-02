# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:22:29 2018

@author: mwood
"""

from astropy.table import Table, Column
import time
import calendar

# Generate timestamp for file name
ts = str(calendar.timegm(time.gmtime()))

# API for whole exoplanet archive database
url= "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets"

# Reads in the API data and store in table
t = Table.read(url,format='csv')

# Generates second table containing only transit planets
t_transit = t[t['pl_discmethod']=='Transit']

# Writes the transit data table to csv file, appenidng timestamp into filename.
t_transit.write('Transit_Data_%s.csv'%ts,format='csv')

# Prints a message comfirming completion, and states the filename.
print("Transit data-loading is complete.")
print("It has been stored in the main directory - Transit_Data_%s.csv"%ts)
