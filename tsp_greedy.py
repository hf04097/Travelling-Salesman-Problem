import  math

def distance(p1,p2):
     return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def greedyTSP(G,start):
     n = len(G)
     visited = [0 for e in G]
     path = []
     total_dist = 0
     current = start
    
     for i in range(n):
        min_dist = float("inf")
        min_k = -1
        for k in range(n):
            if visited[k] == 0:
                dist_ = distance(current,G[k])
                if dist_ < min_dist:
                    min_dist = dist_
                    min_k = k
        visited[min_k] = 1
        current = G[min_k]
        path.append(G[min_k])
        total_dist += dist_
     return path, total_dist



G = [(40,72), (120,67), (174,36), (8,44), (11,152), (116,102), (119,143), (149,24), (78,119), (188,140), (137,58),(143,57), (84,138),
     (121,45), (51,23), (186,78), (76,124), (96,41), (4,64), (131,153), (167,5), (31,2), (30,3), (133,186), (124,167)]


print(greedyTSP(G,(40,72)))