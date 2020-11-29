from itertools import permutations
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from timeAnalysis import *


def distance(p1, p2):
    d = (((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2)) ** .5
    return d

def tsp(Points,start):
    length = len(Points) 
    min = None
    minroute = []
    permutacje = list(permutations(range(0, length)))
    for perm in permutacje:
        curdist = 0
        prev = Points[0]
        for i in perm:
            curdist = curdist + distance(prev, Points[i])
            prev = Points[i]
            if min and curdist > min:
                break
        else:
            if not min or curdist < min:
                min = curdist
                minroute = perm
    return min, minroute

# points = [(40,72), (120,67), (174,36), (8,44)]
#
# #print(points)
# dist, route = tsp(points)
# print((dist, route))





time_analasyis(tsp,30,"best","BruteForce")