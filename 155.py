class MinStack:

    def __init__(self):
        self.stack = []
        self.arr = []

    def push(self, x: int) -> None:
        if (not self.arr) or x < self.arr[-1]:
            self.arr.append(x)
        else:
            self.arr.append(self.arr[-1])
        self.stack.append(x)

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.arr = self.arr[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.arr is None: return None
        return self.arr[-1]