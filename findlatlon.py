def findlat(latarr, clat):
    """
    Returns index of lat. Takes 2 args: 
    latarr - the array containing lat coords 
    clat - the lat whose index you're looking for 

    dependencies? numpy?
    """
    import numpy as np

    # no idea how to use this args syntax...
    lati = abs(latarr - clat).argmin()

    return lati

def findlon(lonarr, clon):
    """
    Returns index of lon. Takes 2 args: 
    lonarr - the array containing lon coords 
    clon - the lon whose index you're looking for 

    dependencies? numpy?
    """
    import numpy as np

    if clon != 360:
        clon = clon%360
    else:
        clon = 360
    
    loni = abs(lonarr - clon).argmin()

    return loni
