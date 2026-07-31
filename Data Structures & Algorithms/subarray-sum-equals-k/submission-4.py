class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0: 1}   # prefix sum 0 has appeared once
        running_sum = 0
        count = 0

        for num in nums:
            running_sum += num

            if running_sum - k in freq:
                count += freq[running_sum - k]

            freq[running_sum] = freq.get(running_sum, 0) + 1

        return count
