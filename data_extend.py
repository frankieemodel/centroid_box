def extend_darray(data, size=15):
    """
    Returns the data on a lat/lon grid extended in 
        each direction by size if input is data array
    Takes 2 arguments:
    data: np array with original data grid (lat, lon)
    size - degrees box should extend on each size (for 31x31 box, 
            size = 15, default)
    
    dependencies - numpy
    """
    import numpy as np

    addext = size+1
    addbxsz = 2*addext
    
    # create another array to extend grid on each side
    gridext = np.empty((data.shape[0]+addbxsz,data.shape[1]+addbxsz))
    gridext[:] = np.nan
    # print(gridext.shape)

    # replace gridext with oneday data so that theres only nan on 
    # each side in 10 indices per side
    # MAKE SURE THIS IS RIGHT CALL
    gridext[addext:gridext.shape[0]-addext,addext:gridext.shape[1]-addext] = data

    # copy lon 10 degrees on each side rather than Nan
    gridext[addext:gridext.shape[0]-addext,0:addext] = data[:,-addext:]
    gridext[addext:gridext.shape[0]-addext,gridext.shape[1]-addext:] = data[:,:addext]
    
    return gridext


def extend_dfile(size, dfile):
    """
    Returns data on a lat/lon grid extended in each direction 
        by size if input is data file
        input is file with 3D data, output is 3D array
    Takes 2 arguments:
    size - degrees box should extend on each size (for 21x21 box, 
            size = 10)
    dfile: nc file containing 1 year's worth of data

    dependencies - numpy, xarray (?), netCDF4
    """
    import numpy as np
    import xarray as xr
    import netCDF4

    ds = xr.open_dataset(dfile)
    data_var = list(ds.data_vars)[0]
    data = ds[data_var].to_numpy()

    addext = size+1
    addbxsz = 2*addext

    # create another array to extend grid on each side
    gridext = np.empty((data.shape[0],data.shape[1]+addbxsz,data.shape[2]+addbxsz))
    gridext[:] = np.nan
    print("shape of original grid: ", data.shape)
   

    # replace gridext with oneday data so that theres only nan on 
    # each side in 10 indices per side
    # MAKE SURE THIS IS RIGHT CALL
    gridext[:,addext:gridext.shape[1]-addext,addext:gridext.shape[2]-addext] = data

    # testing that gridext[10,10] and gridext[190,370] are the 
    # the first and last element of a but the ones on 
    # either side are still nan
    print(gridext[0,addext-1,addext-1],
        gridext[0,addext,addext],
        gridext[0,-addext-1,-addext-1],
        gridext[0,-addext,-addext])
    # print(data[0,0,0],data[0,-1,-1])

    # print(gridext.shape[0],gridext.shape[1],gridext.shape[2])

    # copy lon 10 degrees on each side rather than Nan
    gridext[:,addext:gridext.shape[1]-addext,0:addext] = data[:,:,-addext:]
    gridext[:,addext:gridext.shape[1]-addext,gridext.shape[2]-addext:] = data[:,:,:addext]
    # lonn[len(lonn)-ext:] = np.arange(lon[-1]+1,lon[-1]+11)
    # print(data[:,-addext:].shape)

    print("shape of extended grid: ", gridext.shape)
    # # printing bits of gridext
    # print("gridext samples")
    # print("lat 9 to 11, lon start and end")
    # # first rows should be nan, others filled
    # print(gridext[0,addext-2:addext+2,addext-1:addext+2])
    # print(gridext[0,addext-2:addext+2,-1-addext:-8])
    # print("lat end, lon start and end")
    # # first rows filled, last rows nan
    # print(gridext[0,-1-addext:-8,addext-1:addext+2])
    # print(gridext[0,-1-addext:-8,-1-addext:-8])

    return gridext

def extend_fll(size, dfile):
    """
    Returns 2 arrays: extended lat, extended lon, from nc file input
    Takes 2 arguments:
    size - degrees box should extend on each size (for 21x21 box, 
            size = 10)
    dfile: nc file with dimensions "lat" and "lon" in order lon, lat etc
     ** order of dimensions is crucial ie lon must be listed first

    dependencies - numpy, xarray (?), netCDF4
    """
    import numpy as np
    import xarray as xr
    import netCDF4

    ds = xr.open_dataset(dfile)
    lonv = list(ds.dims)[0]
    latv = list(ds.dims)[1]
    lon = ds[lonv].to_numpy()
    lat = ds[latv].to_numpy()

    addext = size+1
    addbxsz = 2*addext

    # edit lat/lon grids to account for extra degrees on each side
    latext = np.empty((len(lat)+addbxsz))
    lonext = np.empty((len(lon)+addbxsz))
    # fill extra grid with nan
    latext[:] = np.nan
    latext[addext:len(latext)-addext] = lat
    lonext[:] = np.nan
    lonext[addext:len(lonext)-addext] = lon
    
    # fill nans with new values so the finding indices works
    # otherwise it returns index 0 for all bc of the argmin method used

    # Lat fill assumes lat from -90 to 90
    # fill extended lat grid at start with range of vals from lat[0]-addext
    # adding extra row (addext = size+1) makes edge cases work
    latext[0:addext] = np.arange(lat[0]-addext,lat[0])
    # replace nan at end of lat grid
    latext[len(latext)-addext:] = np.arange(lat[-1]+1,lat[-1]+addext+1)

    # Lon fill assumes lonn from 0 to 360
    # note that data fill will wrap for longitude but lon grid can't 
    # wrap in order for finding vertices to work
    lonext[0:addext] = np.arange(lon[0]-addext,lon[0])
    lonext[len(lonext)-addext:] = np.arange(lon[-1]+1,lon[-1]+addext+1)

    return latext,lonext