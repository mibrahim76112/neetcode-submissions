class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        r = 1
        best = 0

        while r <n:

            if prices[r] > prices[l]:
                profit = prices[r]-prices[l]
                if profit  > best:
                    best = profit
            else:
                l=r
            r+=1
        return best

            


