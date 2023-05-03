def corners(latarr,lonarr,cents, size=15):
    """
    Returns the indices of corners of box centered at clat, clon,
    extending 'size' degrees in each direction from center.
     - also returns the extended lat and lon grids
     - out: corners, latext, lonext
    Takes 4 args:
    latarr, lonarr - arrays of lat and lon coords
    cents: list or array of 1 or more centroids: clat, clon - lat and lon where
         box(es) are centered 
            (must be paired ie [clat,clon])
    size - degrees box should extend on each size (for 31x31 box, 
            size = 15, default)
    
    dependencies - numpy, findlatlon (mine)
    """
    import numpy as np
    from findlatlon import findlat
    from findlatlon import findlon

    addext = size+1
    addbxsz = 2*addext

    # edit lat/lon grids to account for extra degrees on each side
    latn = np.empty((len(latarr)+addbxsz))
    lonn = np.empty((len(lonarr)+addbxsz))
    # fill extra grid with nan
    latn[:] = np.nan
    latn[addext:len(latn)-addext] = latarr
    lonn[:] = np.nan
    lonn[addext:len(lonn)-addext] = lonarr
    
    # fill nans with new values so the finding indices works
    # otherwise it returns index 0 for all bc of the argmin method used

    # Lat fill assumes lat from -90 to 90
    # fill extended lat grid at start with range of vals from lat[0]-addext
    # adding extra row (addext = size+1) makes edge cases work
    latn[0:addext] = np.arange(latarr[0]-addext,latarr[0])
    # replace nan at end of lat grid
    latn[len(latn)-addext:] = np.arange(latarr[-1]+1,latarr[-1]+addext+1)

    # Lon fill assumes lonn from 0 to 360
    # note that data fill will wrap for longitude but lon grid can't 
    # wrap in order for finding vertices to work
    lonn[0:addext] = np.arange(lonarr[0]-addext,lonarr[0])
    lonn[len(lonn)-addext:] = np.arange(lonarr[-1]+1,lonarr[-1]+addext+1)
    corners = []
    for cent in cents:
    # boxi = np.empty((len(args),4))
        # boxi = np.empty(4)
        # print(len(args))
        if cent[1] != 360:
            cent[1] = cent[1]%360
        else:
            cent[1] = 360
        # if box is 20x20 for ex, itll extend by 10 in each dir
        cw = cent[1] - size
        # print("cw", cw)
        ce = cent[1] + size
        # print("ce", ce)
        cn = cent[0] + size
        # print("cn", cn)
        cs = cent[0] - size
        # print("cs", cs)
        
        # find indices (should I loop this?)
        wi = abs(lonn - cw).argmin()
        ei = abs(lonn - ce).argmin()
        ni = findlat(latn, cn)
        si = findlat(latn, cs)

        # put into box index array
        boxi = np.array([si,ni,wi,ei])
        # put boxi into corners list
        corners.append(boxi)
    
    # turn corners list into array
    corners = np.asarray(corners)

    return corners, latn, lonn
    return lonn, latn
    

    # if clon != 360:
    #     clon = clon%360
    # else:
    #     clon = 360
    # # if box is 20x20 for ex, itll extend by 10 in each dir
    # cw = clon - size
    # ce = clon + size
    # cn = clat + size
    # cs = clat - size
    
    # # find indices (should I loop this?)
    # wi = findlon(lonarr, cw)
    # ei = findlon(lonarr, ce)
    # ni = findlat(latarr, cn)
    # si = findlat(latarr, cs)

    # return si,ni,wi,ei

    