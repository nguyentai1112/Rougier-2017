#! /usr/bin/env python3

import numpy as np
import tsp

if __name__ == '__main__':
    points = np.load('../data/boots-stipple.npy')
    convert_points = list(map(tuple, points))
    result = tsp.tsp(convert_points)