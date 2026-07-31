
class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [0]*k
        self.k = k
        self.start = 0
        self.end = 0 
        self.total = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.arr[self.end] = value
        self.end = (self.end+1)%self.k
        self.total+=1
        return True
    def deQueue(self) -> bool:

        if self.isEmpty():
            return False
        
        self.arr[self.start]  = 0
        self.start = (self.start+1)%self.k
        self.total-=1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.start]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.end-1)%self.k]
        
    def isEmpty(self) -> bool:
        if self.total == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.total == self.k:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()