import math

import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from timeAnalysis import *


def distance(p1, p2):
    """
    :return: distance between two points
    """
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


def greedyTSP(G, start):
    """
    :param G: list of tuples with x and y coordinates of a city in the tuple
    :param start: The city/point from which the journey will start
    :return: The path taken and the distance covered.
    """
    n = len(G)
    visited = [0 for e in G]  # keeping in record the cities visited
    path = []
    total_dist = 0
    current = start

    for i in range(n):
        min_dist = float("inf")
        min_k = -1
        for k in range(n):
            if visited[k] == 0:
                dist_ = distance(current, G[k])     # calculating the distance between current point and kth point
                if dist_ < min_dist:
                    min_dist = dist_        # if the distance is less than the minimum distance we will go to that city
                    min_k = k
        visited[min_k] = 1
        current = G[min_k]
        path.append(G[min_k])
        total_dist += dist_
    return path, total_dist


time_analasyis(greedyTSP, 100, "average", "Greedy")
