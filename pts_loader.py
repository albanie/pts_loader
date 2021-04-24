# pts_loader provides a load() method to read data from .pts files of
# point clouds
#
# --------------------------------------------------------
# pts_loader
# Licensed under The MIT License [see LICENSE.md for details]
# Copyright (C) 2017 Samuel Albanie 
# --------------------------------------------------------

import numpy as np

def load(path, N):
    """takes as input the path to a .pts and returns a list of 
	tuples of floats containing the points in in the form:
	[(x_0, y_0, z_0),
	 (x_1, y_1, z_1),
	 ...
	 (x_n, y_n, z_n)]"""
    with open(path) as f:
        rows = [rows.strip() for rows in f]
    
    """Use the curly braces to find the start and end of the point data""" 
    try:
    	head = rows.index('{') + 1
    	tail = rows.index('}')
    	raw_points = rows[head:tail]
    except:
    	raw_points = rows
    # """Select the point data split into coordinates"""
    coords_set = [point.split() for point in raw_points]

    """Convert entries from lists of strings to tuples of floats"""
    points = np.array([tuple([float(point) for point in coords]) for coords in coords_set])
    idxs   = range(0, points.shape[0])
    points = points[np.random.choice(idxs,size=N, replace=False)]
    return points
