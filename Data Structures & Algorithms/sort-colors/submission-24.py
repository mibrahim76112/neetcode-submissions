class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3

        for num in nums:
            count[num] +=1
        m = 0
        for i in range(3):  
            while count[i]:
                nums[m] = i
                m+=1
                count[i]-=1
        
        return nums