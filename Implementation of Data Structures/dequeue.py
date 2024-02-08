#Sample

from collections import deque

queue=deque()

queue.append(0)
queue.appendleft(1)
queue.appendleft(2)
queue.appendleft(3)
print(queue)
# pop
queue.pop()
queue.popleft(1)
print(queue)
#len
print(len(queue))

queue.append(0)
queue.appendleft(1)
print(queue)
queue.append(0)
queue.appendleft(1)
print(queue)


# Actual implementation

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.items)

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("queue:", queue.items)
print("length:", queue.size())
queue.peek()

dequeued_item = queue.dequeue()
print("Dequeued:", dequeued_item)
print("queue:", queue.items)
