from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_nodes(self, first_node, second_node):
        if first_node not in self.graph:
            self.graph[first_node] = []
        self.graph[first_node].append(second_node)

        if second_node not in self.graph:
            self.graph[second_node] = []
        self.graph[second_node].append(first_node)


    def get_nodes(self):
        return list(self.graph.keys())


    def get_edges(self):
        edges = []
        for u in self.graph:
            for v in self.graph[u]:
                if (v, u) not in edges:
                    edges.append((u, v))
        return edges

    def get_neighbors(self, target):
        total_neighbors = 0
        key = self.graph[target]
        neighbors = []

        for values in key:
            if values not in neighbors:
                total_neighbors += 1
                neighbors.append(values)
        return (total_neighbors, neighbors)


    def get_total_nodes(self):
        return len(self.graph)

def breadth_first_search(graph, start, total_nodes):
    queue = deque([start])
    visited = set()

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    if (len(visited) == total_nodes):
        return 0
    else:
        return 1

def depth_first_search(graph, start, total_nodes):
    stack = [start]
    visited = set()

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for children in graph[vertex]:
                if children not in visited:
                    stack.append(children)
    if (len(visited) == total_nodes):
        return 0
    else:
        return 1