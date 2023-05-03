def month_indices(leap=False):
    """
    Returns months and indices of month. Takes one optional arg:
    leap=True for a leap year 
    Access with mondict['Jan'] 
    Ignoring leap year...
    depends on numpy... (idk how to deal with dependencies 
        - import in function?)
    """
    import numpy as np
    
    # creating dictionary of indices for days of each month
    # to access a month's indices: mondict['Jan']]
    # or a day's index: mondict['Feb'][0]) 
    # indices can be used as input for NUMPY array

    Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
               'Sep', 'Oct', 'Nov', 'Dec']
    
    mondict = dict.fromkeys([i for i in Months])

    count = 0
    
    if leap:
        mon_len = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        mon_len = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    for x in Months:
        mondict[x] = np.arange(sum(mon_len[0:count]), 
                               sum(mon_len[0:count+1]))
        count+=1

    return Months, mondict


def day_index(month, day, year):
    """
    day: an integer, in range of days in that month
    year: an int, the year x
    Returns index of a day. Takes 3 arguments 
    month: an integer representing a month (1 through 12)
    

    depends on numpy and calls month_indices
    """
    import numpy as np
    if year % 4 == 0:
        months, mi = month_indices(leap=True)
    else:
        months, mi = month_indices()
    
    mnth = months[month-1]

    di = mi[mnth][day-1]

    return di

    

