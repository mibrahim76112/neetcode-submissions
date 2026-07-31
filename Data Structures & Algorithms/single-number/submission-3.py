class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        k = 0
        out = 0
        for num in nums:
            out = num ^ out
        return out
