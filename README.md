**Author:** [Behrouz Safari](https://astrodatascience.net/)<br/>


# Equation of time
*Calculating and using the equation of time*


## Quick start

Download [this CSV file](https://raw.githubusercontent.com/behrouzz/eot/main/eot_2020_2050.csv) which is the table of equation of time for all days at 12:00:00 from 2020 to 2050.
You can use it as you want, fit curve, interpolation, etc.


## Package *eot*

The package *eot* contains several functions that you can use easily to calculate equation of time.
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


See more examples at [astrodatascience.net](https://astrodatascience.net/)
