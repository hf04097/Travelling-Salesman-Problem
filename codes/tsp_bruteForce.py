from itertools import permutations

def distance(p1, p2):
    d = (((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2)) ** .5
    return d

def tspBrute(Points):
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



