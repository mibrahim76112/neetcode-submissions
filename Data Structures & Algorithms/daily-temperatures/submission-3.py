class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        s = []
        out = [0]*len(temperatures)
    
        for i, t in enumerate(temperatures):
            while s and temperatures[s[-1]]<t:
                idx = s.pop()
                out[idx] = i - idx

            s.append(i)
        return out
