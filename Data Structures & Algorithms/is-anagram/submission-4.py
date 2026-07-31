class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        

        setA,setB = {}, {}
        for i in range(len(s)):
            setA[s[i]] = 1+ setA.get(s[i],0)
            setB[t[i]] = 1+ setB.get(t[i],0)
        
       
        return setA == setB
