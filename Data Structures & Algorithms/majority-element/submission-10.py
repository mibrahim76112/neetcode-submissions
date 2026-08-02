class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashsetA = {}

        for num in nums:
            hashsetA[num] = hashsetA.get(num,0) + 1
        
        return max(hashsetA,key=hashsetA.get)
