import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import ephem


def get_noon_exact(t, lon, lat):
    # just for testing the results
    t = datetime(t.year, t.month, t.day, 12) - timedelta(hours=(lon/15))
    o = ephem.Observer()
    o.long = str(lon)
    o.lat = str(lat)
    sun = ephem.Sun()
    sunrise = o.previous_rising(sun, start=ephem.date(t))
    noon = o.next_transit(sun, start=sunrise)
    return noon.datetime()


def gmt_noon_exact(t):
    t = datetime(t.year, t.month, t.day, 12)
    o = ephem.Observer()
    o.long = '0'
    o.lat = '0'
    sun = ephem.Sun()
    sunrise = o.previous_rising(sun, start=ephem.date(t))
    noon = o.next_transit(sun, start=sunrise)
    return noon.datetime()


def eot_table_year(year):
    t0 = datetime(year, 1, 1, 12) - timedelta(days=1)
    tw = np.array([t0 + timedelta(days=i) for i in range(367)])
    y = np.array([(t-gmt_noon_exact(t)).total_seconds() for t in tw])
    return y


def eot_table(y1, y2):
    dc = {}
    for i in range(y1, y2+1):
        dc[str(i)] = eot_table_year(i)

    df = pd.DataFrame(dc)

    t0 = datetime(y1, 1, 1, 12) - timedelta(days=1)
    tw = np.array([t0 + timedelta(days=i) for i in range(367)])
    
    df.index = [str(i)[5:-3] for i in tw]
    df.index.name = 'time'
    return df



if __name__ == "__main__":
    df = eot_table(2020, 2050)
    df.to_csv('eot_2020_2050.csv')
