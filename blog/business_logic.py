__author__ = 'gabdulla'

from math import *




#to hold the latitude and longitude data
class polygon_data:

    def __init__(self,x,y):
        self.x = x
        self.y = y

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



#area for polygon
def area_for_polygon(polygon):
    print("i am here also")
    result = 0
    imax = len(polygon) - 1
    print(imax)
    for i in range(0,imax):
        print(i)
        result += (polygon[i].x * polygon[i+1].y) - (polygon[i+1].x * polygon[i].y)
        print(result)
    result += (polygon[imax].x * polygon[0].y) - (polygon[0].x * polygon[imax].y)
    print (result)
    return result / 2.

# centroid of a set of points
def centroid_for_polygon(polygon):
    print("i am here")
    print(polygon[0].y)
    print(polygon[1].y)
    area = area_for_polygon(polygon)
    print(area)
    imax = len(polygon) - 1

    result_x = 0
    result_y = 0
    for i in range(0,imax):
        result_x += (polygon[i].x + polygon[i+1].x) * ((polygon[i].x * polygon[i+1].y) - (polygon[i+1].x * polygon[i].y))
        result_y += (polygon[i].y + polygon[i+1].y) * ((polygon[i].x * polygon[i+1].y) - (polygon[i+1].x * polygon[i].y))
    result_x += (polygon[imax].x + polygon[0].x) * ((polygon[imax].x * polygon[0].y) - (polygon[0].x * polygon[imax].y))
    result_y += (polygon[imax].y + polygon[0].y) * ((polygon[imax].x * polygon[0].y) - (polygon[0].x * polygon[imax].y))
    result_x /= (area * 6.0)
    result_y /= (area * 6.0)
    print(result_x)
    print(result_y)
    var = polygon_data(result_x, result_y)
    print("after var")
    print(result_x)
    print(result_y)
    return var

def distance_between(lat1,long1,lat2,long2):

    x = abs(lat1-lat2) * 100
    y = abs(long1-long2) * 100

    z = sqrt(x**2+y**2)
    return z


#finding the farthest points
def farthest_points(polygon):
    val = len(polygon)
    max = 0.0
    point1 = polygon_data(0.0,0.0)
    point2 = polygon_data(0.0,0.0)
    for i in range(val):
        for j in range(i+1, val):
            temp = distance_between(polygon[i].x, polygon[i].y, polygon[j].x, polygon[j].y)
            if max < temp:
                point1.x = polygon[i].x
                point1.y = polygon[i].y
                point2.x = polygon[j].x
                point2.y = polygon[j].y
                max = temp

    dis = distance(point1.x, point1.y, point2.x, point2.y)
    dis *= 0.3
    return dis


distance_vector = []
final = []
simplelist = []

lat1 = 16.4535553
lon1 = 31.465645435
lat2 = 12.4556756
lon2 = 35.475676867
lat3 = 17.23436456
lon3 = 38.12234565

polygon =[]
x = polygon_data(lat1,lon1)
polygon.append(x)
y = polygon_data(lat2,lon2)
polygon.append(y)
z = polygon_data(lat3,lon3)
polygon.append(z)

cen = centroid_for_polygon(polygon)

print(cen.x)