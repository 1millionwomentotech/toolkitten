#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:43:43 2018

@author: shanmugamjanaki
"""

# hours in a year
Yr_Hrs = 365*24
print(Yr_Hrs)

#minutes in a decade
print(10*Yr_Hrs*60)

from datetime import date
from datetime import timedelta
from datetime import datetime

#calculate age (in years)
birthday = date(1988,10,7)
def calc_age_yrs(birthday):
    today = date.today()
    return today.year - birthday.year - ((today.month,today.day) < (birthday.month,birthday.day))
calc_age_yrs(birthday)

# age (in seconds)
birthday = datetime(1988,10,7,8,44,0)
(datetime.now() - birthday).total_seconds()

# calculate birthdate (reverse)
#birthday = datetime.now() - timedelta(0,939606855.727789)
birthday = datetime.now() - timedelta(0,48618000)
birthday.strftime("%d %b %Y")