class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        
        for char in tokens:
            if char == "+":
                b = s.pop()
                a = s.pop()
                s.append(a + b)
            elif char == "-":
                b = s.pop()
                a = s.pop()
                s.append(a - b)
            elif char == "*":
                b = s.pop()
                a = s.pop()
                s.append(a * b)
            elif char == "/":
                b = s.pop()
                a = s.pop()
                s.append(int(a / b))
            else:
                s.append(int(char))
        return s.pop()

            
            