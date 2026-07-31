class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        
        lowest = min(strs, key=len)
        total = 0
        for i, s in enumerate(lowest):
            for j in strs:
                if s != j[i]:
                    return lowest[:total]
            total+=1
         
        return lowest
