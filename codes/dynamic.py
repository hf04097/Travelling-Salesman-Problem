import random
import math
from random import randint


def CoordinatesToDictionary(points):
    points_dict = {}
    for i in range(len(points)):
        for j in range(len(points)):
            if i + 1 == j + 1:
                points_dict[(i + 1, j + 1)] = 0
            else:
                points_dict[(i + 1, j + 1)] = math.sqrt(
                    pow(points[j][0] - points[i][0], 2) + pow(points[j][1] - points[i][1], 2))
    # print(points_dict)
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


def GetCostVal(row, col, source, cities):
    if col == 0:
        col = source
        return cities[(row, col)]
    return cities[(row, col)]


def TSPMinDistanceDP(main_source, source, cities, G):
    memory = len(cities)
    num_cities = CoordinatesToDictionary(G)
    print(CoordinatesToDictionary(G))
    memory += len(num_cities)

    if len(cities) == 1:
        minimumDis = (GetCostVal(source, cities[0], main_source, num_cities) +
                      GetCostVal(cities[0], 0, main_source, num_cities))

        memory += 1
        return minimumDis, memory

    else:
        distance = []
        for city in cities:
            dcities = cities[:]
            dcities.remove(city)
            distance.append(
                GetCostVal(source, city, source, num_cities) + TSPMinDistanceDP(main_source, city, dcities, G)[0])
            # distance.append(GetCostVal(source, city, source, num_cities) + TSPMinDistanceDP(main_source, city, dcities))

        minimumDis = min(distance)
        # print(distance)

        memory += len(distance)
        memory += len(dcities)
        return minimumDis, memory


def GetCities(G, main_source):
    lst = [i + 1 for i in range(len(G))]
    lst.remove(main_source)
    return lst

# G = [(1,2),(3,4)]
# G = [(randint(1, 10), randint(1, 10)),(randint(1, 10), randint(1, 10)), (randint(1, 10), randint(1, 10)), (randint(1, 10), randint(1, 10)),
#      (randint(1, 10), randint(1, 10)), (randint(1, 10), randint(1, 10)), (randint(1, 10), randint(1, 10)), (randint(1, 10), randint(1, 100))]
# print(G, len(G))
# print(len(G))
# print(G1)

# TSPMinDistanceDP(G[0][0],G[0][0], GetCities(G, G[0]))
# print(GetCities(G, 1))

# G =[]
# for i in range(3):
#   G.append((randint(1,100),randint(1,100)))
# #print(G)
# TSPMinDistanceDP(1, 1, GetCities(G, 1), G)