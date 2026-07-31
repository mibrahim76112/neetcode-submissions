class StockSpanner:

    def __init__(self):
        self.s = []
        self.ch = []

    def next(self, price: int) -> int:
        val = 1
        while self.s and self.s[-1] <= price:
            val+=1
            a = self.s.pop()
            self.ch.append(a)
        while self.ch:
            self.s.append(self.ch.pop())
        self.s.append(price)
        return val

       

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)