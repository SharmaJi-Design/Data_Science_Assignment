# Part II
# Stack (Manual Implementation)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

s = Stack()
s.push(10)
s.push(20)
print(s.pop())  