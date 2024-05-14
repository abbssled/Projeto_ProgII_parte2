# 2023-2024 Programacao 2 LTI
# Grupo 24
# 56387 Ana Bentes
# XXXXX Maria Silva

from Station import Station
from Link import Link
from Path import Path

# python safeLevadas.py inputFile1.txt inputFile2.txt outputfile.txt

def readNetwork(file):
    networkFile = open(file, 'r')
    networkLines = networkFile.readlines()
    network = {}
    for line in networkLines:
        if line != '#Id, Name, Connected:\n':
            newLine = line.split('[')
            network[newLine[0].strip(', ')] = newLine[1].strip('\n')
    
    networkFile.close()

    return network


def readStations(file):
    stationsFile = open(file, 'r')
    stationsLines = stationsFile.readlines()
    paths = {}
    for line in stationsLines:
        paths['source'] = line.split('-')[0]
        paths['destination'] = line.split('-')[1]

    stationsFile.close()

    return paths
    
# print(readNetwork('myLevadasNetwork.txt'))
# print(readStations('myStations.txt'))


def DFS(graph, start, end, path, shortest):
    """
    Depth first search in a directed graph

    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph
    """

    # accumulates; start node entered into the path
    path = path + [start]
    
    # just to keep watching the recursion progressing
    print('Current DFS path:', printPath(path))

    # recursion: base
    # target node is reached (or initially start and end nodes are the same)
    if start == end: 
        return path

    # recursion: step
    # target was not reached and start node is not a leaf (i.e. it has children)
    for node in graph.childrenOf(start):
        
        if node not in path: # to avoid cycles

            # recursive call of DFS function to itself
            # if target was never reached yet before OR
            # this path is still the shortest so far
            if shortest == None or len(path) < len(shortest): 
                newPath = DFS(graph, node, end, path, shortest)
                
                if newPath != None: # if target node was reached
                    shortest = newPath
                    
    # the shortest path found so far after running the for cycle
    return shortest


    