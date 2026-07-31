class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n+1):
            c =0
            while i:
                i&= i-1
                c+=1
            out.append(c)
        return out
