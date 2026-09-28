class MinStack:

    def __init__(self):
        self.stack = []
        self.minvalstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minvalstack) > 0:
            if val < self.minvalstack[-1]:
                self.minvalstack.append(val)
            else:
                self.minvalstack.append(self.minvalstack[-1])
        else:
            self.minvalstack.append(val)        
        

    def pop(self) -> None:
        self.stack.pop()
        self.minvalstack.pop()     

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        if len(self.minvalstack) > 0:
            return self.minvalstack[-1]
        else:
            return -1
        
