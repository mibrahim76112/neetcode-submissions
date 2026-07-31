class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      
        short = min(strs,key = len)
        output = ""
        for i in range(len(short)):
            cur = short[i]
            for num in range(len(strs)):
                if strs[num][i] != cur:
                    return output
            output += cur
        return output
