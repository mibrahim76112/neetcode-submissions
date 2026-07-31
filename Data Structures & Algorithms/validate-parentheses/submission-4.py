class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <2:
            return False
        
        arr = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for i in s:
            if i in mapping.values():
                arr.append(i)
            elif i in mapping:
                if not arr or arr[-1] != mapping[i]:
                    return False
                arr.pop()

        return not arr
            
            
