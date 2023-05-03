def box_data(corners,sel_data,size=15):
    """
    3 inputs: 
    corners - an (n,4) array containing corner indices of boxes of data that you'd like to extract from
    sel_data - (n, x, y) array containing a day's worth of data from which you'd like to extract boxes, each corresponding to a corner
    sz - sz by which the box extends on each side from box centroid (must be same size used to create the corners in corners fxn), default is 15

    output: one array (n,2*sz+1,2*sz+1) containing data from boxes located with indices for each day's worth of data, default is (n,31,31)

    dependencies: numpy, data_extend.extend_darray (user defined)
    """
    import data_extend
    import numpy as np
    centroid_data = []
    for x in range(corners.shape[0]):
        one_day = sel_data[x,:]
        one_ext = data_extend.extend_darray(one_day,size)
        c = corners[x]
        one_box = one_ext[c[0]:c[1]+1,c[2]:c[3]+1]
        centroid_data.append(one_box)
    centroid_data = np.asarray(centroid_data)
    return centroid_data