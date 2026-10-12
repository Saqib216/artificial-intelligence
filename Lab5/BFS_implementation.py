class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        queue = []
        visited = []

        queue.append(start)
        visited.append(start)

        while queue:
            node = queue.pop(0)

            print(node, end=" ")

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)


g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 4)
g.add_edge(1, 3)
g.add_edge(1, 2)
g.add_edge(4, 3)
g.add_edge(3, 2)

print("BFS:")
g.bfs(0)