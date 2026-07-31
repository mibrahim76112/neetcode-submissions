class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        n = len(nums)
        ans.extend([0] * n)
        for i in range(0,n):
            ans[n+i] = nums[i]
        return ans
