class MyQueue:

    def __init__(self):
        self.stack=[]
        self.st=[]

    def push(self, x: int) -> None:

        while self.stack:
            self.st.append(self.stack.pop())
        self.stack.append(x)
        while self.st:
            self.stack.append(self.st.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
