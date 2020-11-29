import time
from random import randint
import matplotlib.pyplot as plt
import numpy as np


def time_analasyis(function, n, case, plotTitle):
    """
    :param function: The function one will be analysis
    :param n: Number of cities
    :param case: average case,worst case,best case. For average case case will be average, for best case, best, for worst case, worst.
    :param plotTitle: The title that time analysis graph will have
    :return: Plot of the input case
    """
    time_total = []
    for x in range(10):
        G = [(randint(-10000, 10000), randint(-10000, 10000))]  # starting from a random point
        time_taken = []
        for t in range(1, n + 1):
            start = None
            end = None

            start = int(round(time.time() * 1000))  # converting to milliseconds from seconds
            function(G, G[-0])
            end = int(round(time.time() * 1000))
            time_diff = end - start
            time_taken.append(time_diff)

            G.append((randint(-10000, 10000), randint(-10000, 10000)))
        time_total.append(time_taken)

    total_time = np.array(time_total)
    if case == "average":
        plot_time = total_time.mean(axis=0)     # Averaging over all iterations

    elif case == "best":
        plot_time = total_time.min(axis=0)      # finding the best set of time

    elif case == "worst":
        plot_time = total_time.min(axis=0)      # finding the worst set of time
    else:
        raise Exception("Invalid case")

    numbers = np.arange(1, n + 1)
    plt.plot(numbers, plot_time)
    plt.xlabel("number of cities")
    plt.ylabel("time taken in milisecods")
    plt.title(plotTitle + " "+ case + " case")
    plt.show()
