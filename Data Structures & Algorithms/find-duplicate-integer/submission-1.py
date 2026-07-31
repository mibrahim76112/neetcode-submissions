class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        dist= {}
        for i in range(n):
            dist[nums[i]] = dist.get(nums[i],0) + 1
            if dist[nums[i]] > 1:
                return nums[i]
