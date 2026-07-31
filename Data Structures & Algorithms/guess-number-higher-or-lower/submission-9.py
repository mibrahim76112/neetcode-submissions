class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            mid = (l + r) // 2
            a = guess(mid)

            if a == 0:
                return mid
            elif a < 0:        # mid is too high
                r = mid - 1
            else:              # a > 0, mid is too low
                l = mid + 1

        return -1
