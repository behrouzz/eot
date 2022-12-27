import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from scipy import interpolate
import os
from urllib.request import urlretrieve


def tim2ord(t):
    d = (t - datetime(t.year, 1, 1)).total_seconds()/86400
    return d


def ord2tim(d, y):
    t = datetime(y, 1, 1) + timedelta(days=d)
    return t


def get_eot(t, file=None, interp_kind='cubic'):
    """
    Equation of time for a given moment
    
    Arguments
    ---------
        t : time (UTC)
        file: path to csv file containing table of equation of time
        interp_kind (str) : interpolation kind (linear, quadratic, cubic, etc.)

    Returns
    -------
        eot (float): equation of time
    """
    #linear, quadratic, cubic
    if file is None:
        file = 'eot_2020_2050.csv'
        if not os.path.isfile(file):
            url = 'https://github.com/behrouzz/astrodata/raw/main/eot/'+file
            print(f'Downloading "{file}"...')
            urlretrieve(url, file)
            print(f'"{file}" downloaded.')
            print()
            
    df = pd.read_csv(file)
    #y = df[str(t.year)].dropna().values
    #x = np.linspace(-0.5, 365.5, len(y))
    y = df[str(t.year)].dropna().values
    x = np.linspace(-0.5, len(y)-1.5, len(y))
    
    f = interpolate.interp1d(x, y, kind=interp_kind)
    equ_of_time = f(tim2ord(t)).flatten()[0]/60
    return equ_of_time


def get_noon(t, lon):
    """
    Calculate the noon time for a given longtitude in UTC

    Arguments
    ---------
        t (datetime): time (UTC)
        lon (float) : longtitude

    Returns
    -------
        noon (datetime): noon time in UTC
    """
    # mean solar time at noon (local in UTC):
    mean_st = datetime(t.year, t.month, t.day, 12) - \
              timedelta(hours=(lon/15))
    equ_of_time = get_eot(mean_st)
    equ_of_time = timedelta(minutes=equ_of_time)
    # true solar time at noon (local in UTC):
    true_st = mean_st - equ_of_time
    return true_st
