# datetime_tools.py>

import datetime as dt

# create_6hrly_timeseries

def create6hrly_timeseries(year):
    """
    Returns datetime array of the year input broken into 6 hour increments.
    """
    #JFB Revisit
    #import datetime as dt
    
    if year%4==0:
        num_ints = 366*4
    else: 
        num_ints = 365*4
    
    print(num_ints)
    
    date_range = [dt.datetime(year, 1, 1) + dt.timedelta(hours=i*6) for i in range(num_ints)]
    
    return date_range


# create_daily_timeseries
def createdaily_timeseries(year):
    """
    Returns datetime array of the year input broken into daily increments.
    """
    #JFB Revisit
    #import datetime as dt
    
    if year%4==0:
        num_ints = 366
    else: 
        num_ints = 365
    
    print(num_ints)
    
    date_range = [dt.datetime(year, 1, 1) + dt.timedelta(days=i) for i in range(num_ints)]
    
    return date_range
    
# create daily time series given start and end dates

def createdaily_startenddate(start_date, end_date):
    """
    returns datetiem array of days given start and end date. Both dates must be in datetime format.
    ie start_date = dt.datetime(yr, mnth, day) etc
    """
    days = (end_date - start_date).days + 1

    print(days)

    date_range = [start_date + dt.timedelta(days=i) for i in range(days)]

    return date_range

# return end date given start date and number of days

def give_enddate(start_date, numdays):
    """
    returns range of end dates given start date and number of days.
    Start date must be in datetime format.
    ie start_date = dt.datetime(yr, mnth, day) etc
    numdays must be 1 or more iterables (list or array etc)
    dependencies: numpy
    """
    import numpy as np
    
    intdays = [int(x) for x in numdays if not(np.isnan(x)) == True]
    # intdays = [1]
    date_range = [start_date + dt.timedelta(days=i) for i in intdays]

    return date_range

