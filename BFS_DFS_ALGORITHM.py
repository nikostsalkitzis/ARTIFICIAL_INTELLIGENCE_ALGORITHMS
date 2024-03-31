import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                for neighbor in self.adjacency_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    def dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

    def draw(self):
        G = nx.Graph()
        for u in self.adjacency_list:
            for v in self.adjacency_list[u]:
                G.add_edge(u, v)
        nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
        plt.show()


# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(3, 4)

g.draw()
print("BFS traversal starting from vertex 0:")
g.bfs(0)
print("\nDFS traversal starting from vertex 0:")
g.dfs(0)




