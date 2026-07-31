class MinStack:

    def __init__(self):
       self.s = [] 

    def push(self, val: int) -> None:
        self.s.append(val)
        
    def pop(self) -> None:
        a = self.s[-1]
        del self.s[-1]
        return a
        
    def top(self) -> int:
        a = self.s[-1]
        return a
        
    def getMin(self) -> int:
        return min(self.s)
        
