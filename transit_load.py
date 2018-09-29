# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:22:29 2018

@author: mwood
"""

from astropy.table import Table, Column
import time
import calendar

ts = str(calendar.timegm(time.gmtime()))

url= "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets"

t = Table.read(url,format='csv')

t_transit = t[t['pl_discmethod']=='Transit']


t_transit.write('Transit_data_%s.csv'%ts,format='csv')
