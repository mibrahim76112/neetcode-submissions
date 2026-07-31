class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dicthash = set(nums)
        high = 0
        for num in dicthash:
            if (num-1) not in dicthash:
                current = num
                count = 1

                while (current + 1) in dicthash:
                    current += 1
                    count += 1
                high = max(high,count)
        return high
            