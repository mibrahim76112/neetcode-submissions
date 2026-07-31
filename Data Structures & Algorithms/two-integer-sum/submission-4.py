class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #a = target - nums[i]

        hashA = {}
        for i in range(len(nums)):
            hashA[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hashA and hashA[diff] != i:
                return [i,hashA[diff]]
        
        return False
            
            



        