# Queue (Manual Implementation)
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue()) 