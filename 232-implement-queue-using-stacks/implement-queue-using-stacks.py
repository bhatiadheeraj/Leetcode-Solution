class MyQueue:
    stack = []
    selfTransfer = []
    def __init__(self):
        self.stack = []
        self.stackTransfer = []
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while(len(self.stack)):
            self.stackTransfer.append(self.stack.pop())
        ret = self.stackTransfer.pop()
        while(len(self.stackTransfer)):
            self.stack.append(self.stackTransfer.pop())
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