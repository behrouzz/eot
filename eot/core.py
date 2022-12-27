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


def download_eot_file(path=None):
    if path is None:
        path = ''
    tbl_file = 'eot_2020_2050.csv'
    url = 'https://raw.githubusercontent.com/behrouzz/eot/main/'+tbl_file
    print(f'Downloading "{tbl_file}"...')
    urlretrieve(url, path+tbl_file)
    print(f'"{tbl_file}" downloaded.')
    print()
    return path+tbl_file


def get_eot(t, tbl_file=None, interp_kind='cubic'):
    """
    Equation of time for a given moment
    
    Arguments
    ---------
        t (datetime)     : time (UTC)
        tbl_file (str)   : path to csv file (table of daily values of EoT)
                           (Default is None, i.e. file will be downloaded)
        interp_kind (str): interpolation kind (linear, quadratic, cubic, etc.)

    Returns
    -------
        eot (float): equation of time in minutes

    Note: the csv file containing daily values of EoT from 2020 to 2050:
    https://raw.githubusercontent.com/behrouzz/eot/main/eot_2020_2050.csv
    """
    if tbl_file is None:
        tbl_file = 'eot_2020_2050.csv'
        if not os.path.isfile(tbl_file):
            tbl_file = download_eot_file()
            
    df = pd.read_csv(tbl_file)
    y = df[str(t.year)].dropna().values
    x = np.linspace(-0.5, len(y)-1.5, len(y))
    
    f = interpolate.interp1d(x, y, kind=interp_kind)
    equ_of_time = f(tim2ord(t)).flatten()[0]/60
    return equ_of_time


def solar_time(t, lon, tbl_file=None):
    """
    Mean and True solar times
    
    Arguments
    ---------
        t (datetime)   : time in UTC
        lon (float)    : longtitude of observer
        tbl_file (str) : path to csv file (table of daily values of EoT)
                         (Default is None, i.e. file will be downloaded)
                             
    Returns
    -------
        mean_solar_time (datetime)
        true_solar_time (datetime)
    """
    mean_solar_time = t + timedelta(hours=(lon/15))
    equ_of_time = get_eot(t=t, tbl_file=tbl_file)
    equ_of_time = timedelta(minutes=equ_of_time)
    true_solar_time = mean_solar_time - equ_of_time
    return mean_solar_time, true_solar_time


def get_noon(t, lon, tbl_file=None):
    """
    Calculate the noon time for a given longtitude in UTC

    Arguments
    ---------
        t (str/datetime) : time (UTC)
        lon (float)      : longtitude
        tbl_file (str)   : path to csv file (table of daily values of EoT)
                           (Default is None, i.e. file will be downloaded)

    Returns
    -------
        noon (datetime): noon time in UTC
    """
    if isinstance(t, str):
        t = datetime.strptime(t[:10], '%Y-%m-%d')
    # mean solar time at noon (local in UTC):
    mean_st = datetime(t.year, t.month, t.day, 12) - \
              timedelta(hours=(lon/15))
    equ_of_time = get_eot(t=mean_st, tbl_file=tbl_file)
    equ_of_time = timedelta(minutes=equ_of_time)
    # true solar time at noon (local in UTC):
    true_st = mean_st - equ_of_time
    return true_st
