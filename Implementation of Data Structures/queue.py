#Simple example
queue=[]
#add
queue.append(1)
queue.append(2)
queue.append(3)
#pop
queue.pop()
queue.pop()
queue.pop()
#top
print(queue[0])
#size
print(len(queue))


# Actual implementation
class Queue:
  def __init__(self):
      self.items = []

  def empty(self):
      return self.items == []

  def enqueue(self, item):
      self.items.append(item)

  def dequeue(self):
      if not self.empty():
          return self.items.pop(0)
      else:
          return "Queue is empty"

  def peek(self):
      if not self.empty():
          return self.items[0]
      else:
          return "Queue is empty"

  def size(self):
      return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Current queue:", queue.items)
print("Size of queue:", queue.size())
print("Front element of queue:", queue.peek())

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)
print("Current queue:", queue.items)

queue.dequeue()

print(queue)

