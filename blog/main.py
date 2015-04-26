__author__ = 'gabdulla'

from math import *
import bisect

class mapdata:

    def __init__(self,place,lat,long):
        self.place = place
        self.lat = lat
        self.long = long

 #create the class data


def house_keeping():
    #code to copy lat long to a list
    file = open("./blog/latlong.txt")

    xlist = []
    ylist = []
    for eachline in file:
        a = eachline.strip("\n")
        b = a.split(",")
        # print(b[1])
        x = b[0]
        y = b[1]
        xlist.append(float(x))
        ylist.append(float(y))

    #copy places to a list
    file1 = open("./blog/places.txt")

    plist = []
    for eachline in file1:
        a = eachline.strip("\n")
        plist.append(a)



    for count in range(len(plist)):
        x = mapdata(plist[count],xlist[count],ylist[count])
        simplelist.append(x)

    #sorting  the list on x coordinate
    simplelist.sort(key=lambda xy:xy.lat)
    xlist.sort()



    #function to convert lat to kilometers
    #def latToKilo(lat):
        #return lat*110.54
    #function to convert long to kilometers
    #def longToKilo(lat,long):
       # return long * cos(lat)*111.320

 #function to return the distance between two points
def distance(lat1,long1,lat2,long2):

    latdiff = abs(lat1-lat2)
    longdiff = abs(long1-long2)

    x= 110.54 * latdiff
    y= 111.320 * (cos(latdiff)) * longdiff

    z = sqrt(x**2+y**2)
    return z



#business logic to return places within th radius
def business_logic_2(lat,long,dist):
    for each in simplelist:
        distance_vector.append(distance(lat, long, each.lat, each.long))

    #for each in distance_vector:
    #    if each <= dist:
    #        final.append(each.place)

    for i in range(len(distance_vector)):
        if distance_vector[i] <= dist:
            final.append(simplelist[i].place)
    print (final)

    return final



distance_vector = []
final = []
simplelist = []
#lat = 12.9086164163
#long = 77.6456165313
house_keeping()
#business_logic_2(lat,long,2.5)
print (distance_vector)

#for count in simplelist:
 #   print ("place:%s  lat:%f   long %f" %(count.place,count.lat,count.long))