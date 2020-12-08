from itertools import permutations


def distance(p1, p2):
    dist = (((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2)) ** .5
    return dist


def TspBruteForce(Points):
    memory = 0

    length = len(Points)
    memory += 1

    min = None
    minroute = []
    memory += 1

    permute = list(permutations(range(0, length)))
    memory += len(permute)

    for perm in permute:
        curdist = 0
        prev = Points[0]
        # Two units of memory used above

        for i in perm:

            curdist = curdist + distance(prev, Points[i])
            prev = Points[i]

            if min and curdist > min:
                break
        else:
            if not min or curdist < min:
                min = curdist
                minroute = perm

    memory += len(perm)
    memory += 2
    return min, minroute, memory
