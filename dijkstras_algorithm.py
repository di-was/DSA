import sys


STARTING_POINT = 'A'
NEIGHBOURS = 'adjacent_nodes'
MINIMUM_DISTANCE = 'min_distance'
GRAPH = {
    'A': {NEIGHBOURS: {'B': 3, 'C': 4, 'D': 7},},
    'B': {NEIGHBOURS : {'C': 1, 'F': 5},},
    'C': {NEIGHBOURS: {'F': 6, 'D': 2},},
    'D': {NEIGHBOURS : {'E': 3, 'G': 6},},
    'E': {NEIGHBOURS : {'G': 3, 'H': 4},},
    'F': {NEIGHBOURS : {'E': 1, 'H': 8},},
    'G': {NEIGHBOURS : {'H': 2},},
    'H': {NEIGHBOURS : {},}
}



def dijkstras_algorith(graph, starting_point):
    for keys in graph.keys():
        graph[keys][MINIMUM_DISTANCE] = sys.maxsize   
    
    graph[starting_point][MINIMUM_DISTANCE] = 0
    visited = set()
    while len(visited) < len(graph):
        min_distance = sys.maxsize
        min_node = None
        
        for key in graph:
            if key not in visited and graph[key][MINIMUM_DISTANCE] < sys.maxsize:
                min_node = key
                min_distance = graph[key][MINIMUM_DISTANCE]
        visited.add(min_node)
        
        for neighbour, weight in graph[min_node][NEIGHBOURS].items():
            distance = min_distance + weight
            if graph[neighbour][MINIMUM_DISTANCE] > distance:
                graph[neighbour][MINIMUM_DISTANCE] = distance
    return graph


print(dijkstras_algorith(GRAPH, STARTING_POINT))
