import os
import sys
import numpy as np

def getLoc():

    print("\nFetching location")
    os.system('termux-location -p network > loc.txt')
    
    try:
        if os.path.getsize("loc.txt")==0:
            os.system("rm loc.txt")
            sys.exit("Fetching failed\n")
    except:
        sys.exit("Fetching failed\n")

    data = np.loadtxt('loc.txt',skiprows=1,max_rows=3,delimiter = ',',dtype = str)

    lat = float(data[0,0][14:])
    lon = float(data[1,0][15:])
    h = float(data[2,0][14:])

    os.system('rm loc.txt')
    print("Location fetched\n")

    return lon,lat,h

