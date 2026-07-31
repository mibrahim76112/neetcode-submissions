class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        l = 0
        n = len(fruits)

        best = 0
        count = {}
        for r in range(n):
            count[fruits[r]] = count.get(fruits[r],0) + 1
            while len(count)>2:
                count[fruits[l]]  -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l+=1

            best = max(r-l+1,best)
        return best




            
            
