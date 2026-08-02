class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashsetA = {}

        for i in range(len(nums)):
            hashsetA[nums[i]] = hashsetA.get(nums[i],0) + 1
        
        return max(hashsetA,key=hashsetA.get)
