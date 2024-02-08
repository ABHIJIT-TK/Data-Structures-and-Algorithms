
#Simple example

st=[]
#add
st.append(1)
st.append(2)
st.append(3)
#pop
st.pop()
st.pop()
st.pop()
#top
print(st[-1])
#size
print(len(st))

#The actual implementation

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Current stack:", stack.items)
print("Size of stack:", stack.size())
print("Top element of stack:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)
print("Current stack:", stack.items)


