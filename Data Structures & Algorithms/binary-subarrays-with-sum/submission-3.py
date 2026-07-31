class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = {0: 1}
        curr_sum = 0
        ans = 0

        for num in nums:
            curr_sum += num
            if curr_sum - goal in prefix_count:
                ans += prefix_count[curr_sum - goal]
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

        return ans
