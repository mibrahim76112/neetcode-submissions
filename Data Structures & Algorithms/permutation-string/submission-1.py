class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count = {}
        for p in s1:
            count[p] = count.get(p, 0) + 1
        
        n1 = len(s1)
        n2 = len(s2)
        l = 0
        
        total = n1
        for r in range(n2):
            if s2[r] in count:
                if count[s2[r]] > 0:
                    total -= 1
                count[s2[r]] -= 1

            if r - l + 1 > len(s1):
                if s2[l] in count:
                    if count[s2[l]] >= 0:
                        total += 1
                    count[s2[l]] += 1
                l += 1

            if total == 0:
                return True
        return False
