
class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)

    def dls(self, node, goal, limit):
        print(node, end=" ")

        if node == goal:
            return True

        if limit <= 0:
            return False

        for neighbour in self.graph[node]:
            if self.dls(neighbour, goal, limit - 1):
                return True

        return False

    def ids(self, start, goal, max_depth):
        for limit in range(max_depth + 1):
            print("\nDepth limit:", limit)
            print("Visited nodes:", end=" ")

            if self.dls(start, goal, limit):
                print("\nGoal found!")
                return True

        print("\nGoal not found.")
        return False


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

print("IDS Search:")
g.ids("A", "G", 5)
