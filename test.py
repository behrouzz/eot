import numpy as np
from datetime import datetime, timedelta
import ephem
from eot import get_noon


def noon_exact(t, lon, lat):
    t = datetime(t.year, t.month, t.day, 12) - timedelta(hours=(lon/15))
    o = ephem.Observer()
    o.long = str(lon)
    o.lat = str(lat)
    sun = ephem.Sun()
    sunrise = o.previous_rising(sun, start=ephem.date(t))
    noon = o.next_transit(sun, start=sunrise)
    return noon.datetime()


t = datetime.utcnow()
lon, lat = 52.5, 0


# Calculated noon
noon_calcu = get_noon(t, lon)

# Exact noon
noon_exact = noon_exact(t, lon, lat)

print('noon_calcu :', noon_calcu)
print('noon_exact :', noon_exact)

diff = (noon_exact - noon_calcu).total_seconds()
print('Difference (sec):', diff)


