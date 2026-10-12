class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)

    def dfs_with_goal(self, start, goal):
        stack = []
        visited = []

        stack.append(start)
        visited.append(start)

        while stack:
            node = stack.pop()

            print(node, end=" ")

            if node == goal:
                print("\nGoal found!")
                break

            for neighbour in reversed(self.graph[node]):
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)


g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "F")
g.add_edge("A", "D")
g.add_edge("A", "E")

g.add_edge("B", "K")
g.add_edge("B", "J")

g.add_edge("K", "N")
g.add_edge("K", "M")

g.add_edge("D", "G")

g.add_edge("E", "C")
g.add_edge("E", "H")
g.add_edge("E", "I")

g.add_edge("I", "L")

print("DFS with Goal:")
g.dfs_with_goal("A", "G")
