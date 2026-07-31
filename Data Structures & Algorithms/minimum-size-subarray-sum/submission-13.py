class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums) < target:
            return 0

        n = len(nums)
        l=0
        sum_all = 0
        best = 100
        for r in range(n):
            sum_all+=nums[r]
            while sum_all >= target:
                best = min(best,r-l+1)
                sum_all-=nums[l]
                l+=1

            
        return 0 if best == 100 else best





