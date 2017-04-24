# -*- coding: utf-8 -*-                                                     
from collections import namedtuple, deque
from pprint import pprint as pp
 
#reference: https://rosettacode.org/wiki/Dijkstra's_algorithm#Python
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')
 
cdef class Graph(object):
    cdef:
        list edges 
        set vertices
        
    def __cinit__(self, edges):
        cdef list edges2
        #each edge: Edge(start='a', end='b', cost=7)
        edges2 = [Edge(*edge) for edge in edges]
        self.edges = edges2 
        #get vertex 
        self.vertices = set(sum(([e.start, e.end] for e in edges2), []))   

    cdef dijkstra(self, source, dest):
        cdef:
            str u, v, start, end, vertex
            int cost
            dict dis, previous, neighbours 

        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
        #pp(neighbours)

        while q:
            #u = min(q, key=lambda vertex: dist[vertex])
            u = min(q, key = dist.get)
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost 
                if alt < dist[v]:                                  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        #pp(previous)
        #from here, we know the order of vertex
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s

cpdef main():
    graph = Graph([("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
               ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
               ("e", "f", 9)])
    return pp(graph.dijkstra("a", "e"))


# reference: https://www.allegro.cc/forums/thread/605619
# Dijkstra's Algorithm
# Implements Dijkstra's algorithm
# CS338
# Neil Black

# Ah, nexted sequences. This one takes form of Vertices = (A, B, C...)
# Where A, B, and so on are all sequences containing the weights of paths
# to other vertices, with the form Weights = (A, B, C...)
# I simply used a high number to represent a non-existent path

# This is, I believe, called a Weighted Adjacency Matrix

#weights = ((0, 2, 999, 999, 1, 4, 999, 5, 999, 999),
#           (2, 0, 1, 999, 999, 3, 999, 999, 999, 999),
#           (999, 1, 0, 2, 999, 999, 999, 999, 999, 4),
#           (999, 999, 2, 0, 999, 999, 3, 999, 999, 1),
#           (1, 999, 999, 999, 0, 3, 999, 2, 999, 999),
#           (4, 3, 999, 999, 3, 0, 2, 1, 999, 999),
#           (999, 999, 999, 3, 999, 2, 0, 3, 999, 2),
#           (5, 999, 999, 999, 2, 1, 3, 0, 2, 999),
#           (999, 999, 999, 999, 999, 999, 999, 2, 0, 3),
#           (999, 999, 4, 1, 999, 999, 2, 999, 3, 0))

# This list stores visited nodes, in the same order as the tuple above stores
# their weighted paths. Therefore the visited list and the weighted tuple
# will use the same index to refer to the same vertex.

#visited = []

# This list stores the total length from the starting vertex to the vertex
# matching the index (the first index goes with A, the second with B, and so
# on, like with the previous sequences). Since I cannot represent infinity in
# my code, I will use 999, since that's higher than any path that will come
# with the given data.

#length = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999]

# Stores the shortest distance from A to vertices

#distance = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999]

# This tuple is used merely for printing purposes

#letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")

# Since all the calculations start at A, I set Start to 0 (the index
# corresponding to A) and leave it there. I set w to equal Start and
# change it in the algorithm
#vertex = {vertex: None for vertex in xrange(10)}

#def neighbors(i, j):
#    return weights[i][j] != 999
#
#Start = 0
#w = Start
#length = [0, 999, 999, 999, 999, 999, 999, 999, 999, 999]
#
#visited = []
#
#for i in range(10):
#    # These two need to be reset for every iteration of the algorithm
#    # while i not in visited:
#    # Find the vertex with the lowest length, that is not in visited
#    lowest = 9999
#    l = -1
#    for j in range(10):
#        if j not in visited and neighbors(i, j):
#            if length[j] < lowest:
#                lowest = length[j]
#                l = j
#                visited.append(j)
#    
#    for j in range(10):
#        if neighbors(l, j):
#            if length[l] + weights[l][j] < length[j]:
#                length[j] = length[l] + weights[l][j]
#                vertex[j] = l
#
#    distance[i] = length[i]
#
#print vertex 
#print distance
#s, u = [], 9
#while vertex[u] != None:
#    s.append(u)
#    u = vertex[u]
#s.append(u)
#s.reverse()
#print s
#for i in range(10):
#    print(letters[i], ":", distance[i])
#
