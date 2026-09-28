class Stack:
    def __init__(self):
        self.list = []
    def push(self, value):
        self.list = [value] + self.list
    def pop(self):
        return self.list.pop(0)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(stack.list)
print(stack.pop())
print(stack.list)