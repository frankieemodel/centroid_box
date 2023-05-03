def box_coords(latext, lonext, corners):
    """
    takes extended lat and lon arrays (latext and lonext); and corners, an(n,4) array of n=1 or more arrays of box corner indices and outputs an (n,4) array of n=1 or more arrays of box corner lat and lon coordinates

    dependencies = numpy
    """
    import numpy as np

    box_coords = []
    for x in corners:
        one_box = np.array([latext[x[0]],latext[x[1]],
                            lonext[x[2]],lonext[x[3]]])
        box_coords.append(one_box)
    box_coords = np.asarray(box_coords)
    return box_coords