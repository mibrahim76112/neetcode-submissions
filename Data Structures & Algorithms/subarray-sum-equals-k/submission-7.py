class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dicthash = {}
        dicthash[0] = 1
        count = 0
        sum_all=0
        for num in nums:
            sum_all+=num
            if sum_all -k in dicthash:
                count+= dicthash[sum_all-k]
            if sum_all in dicthash:
                dicthash[sum_all] += 1
            else:
                dicthash[sum_all] = 1
        return count


        
