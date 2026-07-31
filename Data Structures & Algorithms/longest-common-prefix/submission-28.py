class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        
        lowest = min(strs, key=len)
        total = 0
        for i, s in enumerate(lowest):
            for j in range(len(strs)):
                if s != strs[j][i]:
                    a = 0
                    return lowest[:total]
            total+=1
         
        return lowest[:total]
