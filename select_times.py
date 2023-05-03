def select_times(drange, year, month=None):
    """
    inputs are drange: date time array in which to lookup indices
    year: year to lookup
    month: month to lookup (optional)
    takes array of date time objects and extracts list of indices 
    representing those matching the chosen year (and month if desired)
    """
    chosen_yr = [x for x in drange if x.year == year]
    ch_yr_ind = [drange.index(date) for date in chosen_yr]
    if month == None:
        return ch_yr_ind
    
    chosen_month = [x for x in chosen_yr if x.month == month]
    ch_month_ind = [drange.index(date) for date in chosen_month]
    return ch_month_ind