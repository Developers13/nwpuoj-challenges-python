from math import *
def hav(x):
    return (sin(x/2))**2
def ahav(x):
    return 2*asin(sqrt(x))
lat1=radians(float(input()))
lon1=radians(float(input()))
lat2=radians(float(input()))
lon2=radians(float(input()))
R=6371
_result=hav(lat2-lat1)+cos(lat1)*cos(lat2)*hav(lon2-lon1)
print(f"{R*ahav(_result):.4f}km")