# Author: Dahir Muhammad Dahir
# Date: 03-July-2019 9:38 PM
# About: bidirectional graph; this is my first graph
# implementation, a graph is a non-linear
# data structure containing a finite number of nodes
# or vertices and edges. edges connect the
# nodes or vertices
# this implementation uses adjacency list representation


class BiGraph:
    def __init__(self, no_of_vertices):
        self.graph = [[] for _ in range(no_of_vertices)]
        self.no_of_vertices = no_of_vertices

    def add_vertex(self, no_of_vertices=1):
        for i in range(no_of_vertices):
            self.graph.append([])

    def add_edge(self, edge):
        if self.graph[edge[0]]:
            self.graph[edge[0]].append(edge[1])
        else:
            self.graph[edge[0]].append(edge[0])
            self.graph[edge[0]].append(edge[1])

        if self.graph[edge[1]]:
            self.graph[edge[1]].append(edge[0])
        else:
            self.graph[edge[1]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

    def remove_edge(self, edge):
        for item in self.graph[edge[0]]:
            if item == edge[1]:
                self.graph[edge[0]].remove(item)

    def print_graph(self):
        for vertex in self.graph:
            print(vertex)
