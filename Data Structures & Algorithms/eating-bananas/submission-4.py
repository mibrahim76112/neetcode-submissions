class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minrate = max(piles)
        n = len(piles)
        if h < n:
            return False

        l = 1
        r = minrate

        while l <= r:
            best = 0
            mid = (l+r)//2
            for i in range(n):
                best += (piles[i] + mid-1)//mid
            
            if best <= h:
                minrate = mid
                r = mid-1
            else:
                l = mid+1
        
        return l 

            
