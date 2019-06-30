import os
import numpy as np

def getLoc():
    os.system('termux-location -p network > loc.txt')

    data = np.loadtxt('loc.txt',skiprows=1,max_rows=3,delimiter = ',',dtype = str)

    lat = float(data[0,0][14:])
    lon = float(data[1,0][15:])
    h = float(data[2,0][14:])

    os.system('rm loc.txt')
    return lon,lat,h

