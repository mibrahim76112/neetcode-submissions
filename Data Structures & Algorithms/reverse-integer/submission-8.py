class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        res= 0
        c = 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            d = x%10
            x = x//10
            
            c = c*10

            if res > MAX_INT/10 or res < MIN_INT/10:
                return 0
            elif res == MIN_INT/10 and d < MIN_INT%10:
                return 0
            res = res * 10 + d
        res *= sign
        return res