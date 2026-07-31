class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        temp = []
        n = len(s)
        output = 0
        best = 0
        for i in range(0,n):
            
            while s[i] in temp:
                temp.pop(0)
            temp.append(s[i])
            best = max(best,len(temp))

            
        return best