class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
 
        r = sum(weights)
        l = max(weights)
        

        while l < r:
            cap = 0
            days_used = 1
            mid = (l+r)//2

            for w in weights:
                if cap + w <= mid:
                    cap += w
                else:
                    days_used += 1
                    cap = w
            if days_used <= days:
                r = mid
            else:
                l = mid + 1
        return l

                    
                

