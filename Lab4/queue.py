class Queue:
    def __init__(self):
        self.list = []
    def enqueue(self, value):
        self.list = [value] + self.list
    def dequeue(self):
        return self.list.pop()

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.list)
print(queue.dequeue())
print(queue.list)