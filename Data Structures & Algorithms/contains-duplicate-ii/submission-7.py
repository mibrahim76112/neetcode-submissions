class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i = 1
        j=0
        while i < n:
            if nums[j] == nums[i]:
                return True

            if (i - j) < k:
                i += 1
            else:
                j += 1
                if j == i:
                    i += 1

    
        return False