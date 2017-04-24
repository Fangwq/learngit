#-*- coding: utf-8 -*-
#reference:http://www.gilles-bertrand.com/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html
cdef dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
    """ calculates a shortest path tree routed in src
    """
    cdef:
        int count
        list path 
        str k, pred 
        int new_distance

    if src == dest:
        path=[]
        pred=dest
        count = 0
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
            count = count + 1
        if count > 1:
            return 'shortest path:'+str(path)+" cost="+str(distances[dest])
        else:
            path.append(dest)
            return 'shortest path:'+str(path)+" cost= " + str(0)
    else :
        # if it is the initial  run, initializes the cost
        if not visited:
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        visited.append(src)
        # now that all neighbors have been visited: recurse
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited={}
        for k in graph:
            #print k
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))
        x = min(unvisited, key=unvisited.get)
        return dijkstra(graph,x,dest,visited,distances,predecessors)

#input a graph
def main():
    cdef:
        dict graph = {'s': {'a': 2, 'b': 1},
                      'a': {'s': 3, 'b': 4, 'c':8},
                      'b': {'s': 4, 'a': 2, 'd': 2},
                      'c': {'a': 2, 'd': 7, 't': 4},
                      'd': {'b': 1, 'c': 11, 't': 5},
                      't': {'c': 3, 'd': 5}}
    return dijkstra(graph,'s','c')

