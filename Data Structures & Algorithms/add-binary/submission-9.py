class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) -1
        j = len(b) - 1

        carry = 0
        out= []

        while i>=0 or j>=0 or carry:
            s = carry

            if i >=0:
                digA = int(a[i])
            else:
                digA = 0

            if j >=0:
                digB = int(b[j])
            else:
                digB = 0
            
            total = digA+digB+carry

            out.append(total%2)
            carry = total//2
            i-=1
            j-=1

        out.reverse()

        return ''.join(map(str, out))
                
