import random
import math


def CoordinatesToDictionary(points):
    points_dict = {}
    for i in range(len(points)):
      for j in range(len(points)):
        if i + 1 == j + 1:
           points_dict[(i + 1, j + 1)] = 0
        else:
          points_dict[(i + 1, j + 1)] = math.sqrt(pow(points[j][0] - points[i][0], 2) + pow(points[j][1] - points[i][1], 2))
    return points_dict
      

def SetCostMatrix(num):
    cmatrix = {}
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i == j:
                cmatrix[(i, j)] = 0
            else:
                cmatrix[(i, j)] = random.randint(10, 50)
    return cmatrix


def GetCostVal(row, col, source):
    if col == 0:
        col = source
        return num_cities[(row, col)]
    return num_cities[(row, col)]

iterative_process = []

def TSPMinDistanceDP(main_source, source, cities):
    #print(num_cities)
    if len(cities) == 1:
        minimumDis = (GetCostVal(source, cities[0], main_source) +
        GetCostVal(cities[0], 0, main_source))
        return minimumDis
    else:
        distance = []
        for city in cities:
            dcities = cities[:]
            dcities.remove(city)
            #cost = GetCostVal(source, city, source) + TSPMinDistanceDP(main_source, city, dcities)
            #distance.append(cost)
            distance.append(GetCostVal(source, city, source) + TSPMinDistanceDP(main_source, city, dcities))
            #path[cost] = [source, city]
            #print("main_source: ",main_source, "source: ",source, "city: ",city)
        iterative_process.append(distance)
        minimumDis = min(distance)
        #return path[min_distance], min_distance
        return minimumDis

TSPMinDistanceDP(main_source, source, cities)