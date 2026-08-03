class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        count = {}

        for num in nums:
            count[num] = count.get(num,0) + 1
        m = 0
        for i in range(3):
            
            while count.get(i,0) > 0:
                nums[m] = i
                m+=1
                count[i] = count.get(i,0) - 1

        
        return nums