import time
from random import randint
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from tsp_greedy import *
from tsp_bruteForce import *
from TSP_GeneticAlgorithm import *


def time_analysis(n):
    """
    :param n: Number of cities
    :return: Plot of the input case
    """
    time_total_brute = []
    time_total_greedy = []
    time_total_genetic = []

    for x in range(10):
        G = [(randint(1, 10000), randint(1, 10000))]  # starting from a random point
        time_taken_brute = []
        time_taken_greedy = []
        time_taken_genetic = []
        for t in range(1, n + 1):
            """
            Brute
            """
            start = int(round(time.time() * 1000))  # converting to milliseconds from seconds
            tspBrute(G)
            end = int(round(time.time() * 1000))
            time_diff = end - start
            time_taken_brute.append(time_diff)
            start = None
            end = None

            """
            Greedy
            """
            start = int(round(time.time() * 1000))  # converting to milliseconds from seconds
            greedyTSP(G,G[0])
            end = int(round(time.time() * 1000))
            time_diff = end - start
            time_taken_greedy.append(time_diff)
            start = None
            end = None

            """
            Genetic
            """
            start = int(round(time.time() * 1000))  # converting to milliseconds from seconds
            geneticAlgorithm(population=G, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
            end = int(round(time.time() * 1000))
            time_diff = end - start
            time_taken_genetic.append(time_diff)
            start = None
            end = None

            G.append((randint(1, 10000), randint(1, 10000)))

        time_total_brute.append(time_taken_brute)
        time_total_brute_greedy.append(time_taken_greedy)
        time_total_genetic.append(time_taken_genetic)

    time_total_brute = np.array(time_total_brute)
    time_total_greedy = np.array(time_total_greedy)
    time_total_genetic = np.array(time_total_genetic)

    numbers = np.arange(1, n + 1)
    """
    for brute
    """
    plt.plot(numbers, time_total_brute.mean(axis=0))
    plt.xlabel("number of cities")
    plt.ylabel("time taken in milliseconds")
    plt.title("Average case brute")
    plt.show()

    plt.plot(numbers, time_total_brute.min(axis=0))
    plt.xlabel("number of cities")
    plt.ylabel("time taken in milliseconds")
    plt.title("Best case brute")
    plt.show()

    plt.plot(numbers, time_total_brute.max(axis=0))
    plt.xlabel("number of cities")
    plt.ylabel("time taken in milliseconds")
    plt.title("Worst case brute")
    plt.show()

    """
    Greedy
    """
    plt.plot(numbers, time_total_greedy.mean(axis=0))
    plt.xlabel("number of cities")
    plt.ylabel("time taken in milliseconds")
    plt.title("Average case brute")
    plt.show()

    plt.plot(numbers, time_total_greedy.min(axis=0))
    plt.xlabel("number of cities")
    plt.ylabel("time taken in milliseconds")
    plt.title("Best case brute")
    plt.show()

    plt.plot(numbers, time_total_greedy.max(axis=0))
    plt.xlabel("number of cities")
    plt.ylabel("time taken in milliseconds")
    plt.title("Worst case brute")
    plt.show()

    """
    genetic
    """

    plt.plot(numbers, time_total_genetic.mean(axis=0))
    plt.xlabel("number of cities")
    plt.ylabel("time taken in milliseconds")
    plt.title("Average case brute")
    plt.show()

    plt.plot(numbers, time_total_genetic.min(axis=0))
    plt.xlabel("number of cities")
    plt.ylabel("time taken in milliseconds")
    plt.title("Best case brute")
    plt.show()

    plt.plot(numbers, time_total_genetic.max(axis=0))
    plt.xlabel("number of cities")
    plt.ylabel("time taken in milliseconds")
    plt.title("Worst case brute")
    plt.show()

#time_analysis(5)