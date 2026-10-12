class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)

    def dfs(self, start):
        stack = []
        visited = []

        stack.append(start)
        visited.append(start)

        while stack:
            node = stack.pop()

            print(node, end=" ")

            for neighbour in reversed(self.graph[node]):
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)


g = Graph()

g.add_edge(1, 2)
g.add_edge(1, 7)
g.add_edge(1, 8)

g.add_edge(2, 3)
g.add_edge(2, 6)

g.add_edge(3, 4)
g.add_edge(3, 5)

g.add_edge(8, 9)
g.add_edge(8, 12)

g.add_edge(9, 10)
g.add_edge(9, 11)

print("DFS Traversal:")
g.dfs(1)
