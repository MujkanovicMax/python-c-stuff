import numpy as np
import requests

def sph2cart(r,theta,phi):

    

    x = r*np.sin(theta/180.*np.pi)*np.cos(phi/180.*np.pi)
    y = r*np.sin(theta/180.*np.pi)*np.sin(phi/180.*np.pi)
    z = r*np.cos(theta/180.*np.pi)

    return x,y,z

def getDist(lon1,lat1,lon2,lat2,h1,h2):
    
    r=6378137.  ###m

    x1,y1,z1=sph2cart(r+h1,lon1,lat1)
    x2,y2,z2=sph2cart(r+h2,lon2,lat2)

    dist = np.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2))

    return dist



def nearest_plane(lon,lat,h):

    url="https://opensky-network.org/api/states/all"

    response = requests.get(url)
    data = response.json()

    callsigns = np.array(data['states'])[:,1].astype(str)
    countries = np.array(data['states'])[:,2].astype(str)
    lons = np.array(data['states'])[:,5].astype(float)
    lats = np.array(data['states'])[:,6].astype(float)
    heights = np.array(data['states'])[:,7].astype(float)
    onground =np.array(data['states'])[:,8]

    
    filt = np.where((onground==False)&(lons!=None)&(lats!=None))
    dist = getDist(lons[filt],lats[filt],heights[filt],lon,lat,h)
    min = np.nanmin(dist)
    i = np.where(dist == min)


    print("Flight: "+str(callsigns[i]))
    print("From: "+str(countries[i]))
    print("Current location: " + str(lats[i]) +" °N " + str(lons[i]) + " °W")
    print("Altitude: " + str(heights[i]) + " m")
    print("Distance: " + str(min) + "m")
    

nearest_plane(11.576006, 48.137079, 519)


#url="https://opensky-network.org/api/states/all"

#response = requests.get(url)
#data = response.json()


