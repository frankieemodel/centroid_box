def data_from_dates(drange, filepath):
    # must change this - the range put in should already start in 2001...
    """
    two inputs: 
        drange, a list of 1 or more datetime objects; 
        filepath, full filepath to *yearly* data file from which you want data extracted
            - IMPORTANT! to replace year in filepath with {year}

    outputs: if drange is length 10 and dfile (365,180,360), outputs array (10, 180,360) selecting the days given in the drange from the requisite datafile(s) and stacking them into an array

    dependencies: python modules: numpy, xarray, user created: month_indices.day_index, select_times.select_times
    """
    import numpy as np
    import xarray as xr
    import month_indices 
    from select_times import select_times

    # if drange[0].year != 2001:
    #     st = select_times(drange, 2001)[0]
    # else:
    #     st = 0
    datalist = []
    date_year = -2000
    for date in range(len(drange)):
        # datapath = '/Volumes/T7/yearly_cloud_data_anom/' + str(drange[date].year) + '/'
        if date_year != drange[date].year:
            # cloudfile = "anom_CERES_"+ str(drange[date].year)+"_cldfrac.nc"
            # cloudpath = datapath + cloudfile
            cloudpath = filepath.format(year=str(drange[date].year))
            ds = xr.open_dataset(cloudpath)
            data_var = list(ds.data_vars)[0]
            cloud_data = ds[data_var].to_numpy()
        date_day = drange[date].day 
        date_month = drange[date].month
        date_year = drange[date].year
        # print(date_year,date_month,date_day)
        # print(cloudfile)
        day_index = month_indices.day_index(date_month,date_day,date_year) 
        
        day_data = cloud_data[day_index,:]
        datalist.append(day_data)
    datalist = np.asarray(datalist)

    return datalist