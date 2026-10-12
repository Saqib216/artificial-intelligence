class PriorityQueue:

    def __init__(self):
        self.queue = []

    def insert(self, item, priority):
        self.queue.append((item, priority))

    def remove(self):
        highest = 0

        for i in range(1, len(self.queue)):
            if self.queue[i][1] < self.queue[highest][1]:
                highest = i

        return self.queue.pop(highest)


pq = PriorityQueue()

pq.insert("A", 3)
pq.insert("B", 1)
pq.insert("C", 2)

while pq.queue:
    item = pq.remove()
    print(item[0], "Priority:", item[1])