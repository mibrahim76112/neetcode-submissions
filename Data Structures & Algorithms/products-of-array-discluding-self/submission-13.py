class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1

        zeros= 0
        for i in range(n):
            if nums[i] != 0:
                prod = prod*nums[i]
            else:
                zeros += 1

        for i in range(n):
            if zeros > 1:
                nums[i] = 0
            elif zeros ==1:
                if nums[i] == 0:
                    nums[i] = prod
                else:
                    nums[i] = 0 
            else:
                nums[i] = int(prod/nums[i]) 

        return nums