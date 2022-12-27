**Author:** [Behrouz Safari](https://astrodatascience.net/)<br/>


# Equation of time
*Calculation and application of the equation of time*


## Quick start

Download [this CSV file](https://raw.githubusercontent.com/behrouzz/eot/main/eot_2020_2050.csv) which is the table of equation of time for all days at 12:00:00 from 2020 to 2050.
You can use it as you want, fit curve, interpolation, etc.


## Package *eot*

The package *eot* contains several functions that you can use easily to calculate equation of time with *very high precision*.
Let's find *mean solar time* and *true solar time* for the city of Tehran with longitude of 51.3347.

```python
from datetime import datetime, timedelta
from eot import get_eot

t = datetime.utcnow()
lon = 51.3347

print('UTC time now    :', t)
print('-'*44)
print('Tehran:')
print('-------')

mean_solar_time = t + timedelta(hours=(lon/15))
print('Mean solar time :', mean_solar_time)
    
equ_of_time = get_eot(t)
print('Equation of time (min) :', equ_of_time)

equ_of_time = timedelta(minutes=equ_of_time)
true_solar_time = mean_solar_time - equ_of_time
print('True solar time :', true_solar_time)
```

Here's the results:

```
UTC time now    : 2022-12-27 04:18:30.351416
--------------------------------------------
Tehran:
-------
Mean solar time : 2022-12-27 07:43:50.679416
Equation of time (min) : -0.8560962378834734
True solar time : 2022-12-27 07:44:42.045190
```

The most straight forward way of getting solar times is using the function *solar_time*:

```python
from eot import solar_time
from datetime import datetime

t = datetime.utcnow()
lon = 51.3347

ture_st, mean_st = solar_time(t, lon)
```


## Time of the noon

You can use the equation ot time to calculate the noon for a given longtitude. But for ease of use, I have created the function *get_noon* which gives the noon for a given longtitude in UTC.


```python
from datetime import datetime
from eot import get_noon

t = datetime.utcnow()
lon = 51.3347

noon = get_noon(t, lon)
print(noon)
```

And the result is:

```
2022-12-27 08:35:36.301976
```

## Equation of time for a time window

If you want to calculate the equation of time for a time interval, the fast way to do is using *eot_time_window*.

```python
from datetime import datetime, timedelta
from eot import eot_time_window

t0 = datetime(2023, 12, 15)
time_window = [t0 + timedelta(days=i) for i in range(50)]
eot_arr = eot_time_window(time_window)
print(eot_arr)
```

The output is:

```
[  5.25224961   4.76996051   4.28386278   3.79457555   3.30270395
   2.808835     2.31353591   1.81735451   1.32082148   0.82445362
   0.32875763  -0.16576608  -0.65862038  -1.14930923  -1.63733655
  -2.12220615  -2.60342224  -3.08049063  -3.55291896  -4.02021874
  -4.48190398  -4.93749137  -5.38649874  -5.8284435   -6.26284094
  -6.68920347  -7.10704078  -7.51586183  -7.9151797   -8.30451867
  -8.68342306  -9.05146586  -9.4082556   -9.75344065 -10.08671092
 -10.40779741 -10.71647012 -11.01253466 -11.295828   -11.56621407
 -11.82357945 -12.06782971 -12.29888703 -12.51668874 -12.72118689
 -12.91234821 -13.09015412 -13.25460055 -13.40569681 -13.5434638 ]
```

See more examples at [astrodatascience.net](https://astrodatascience.net/)
