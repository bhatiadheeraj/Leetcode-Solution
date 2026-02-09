class MyQueue:
    stack = []
    transferStack = []
    def __init__(self):
        self.stack = []
        self.transferStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while len(self.stack):
            self.transferStack.append(self.stack.pop())
        ret = self.transferStack.pop()
        while len(self.transferStack):
            self.stack.append(self.transferStack.pop())
        return ret

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()