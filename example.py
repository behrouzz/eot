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


'''
from datetime import datetime
from eot import get_noon

t = datetime.utcnow()
lon = 51.3347

noon = get_noon(t, lon)
print(noon)
'''
