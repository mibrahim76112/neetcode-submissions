class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        dicthash = {}
        for num in nums:
            if num in dicthash:
                dicthash[num] += 1
            else:
                dicthash[num] =1
        
        arr =[]
        for num in dicthash:
            if dicthash[num] > len(nums)/3:
                arr.append(num)

        return arr

