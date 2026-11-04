
class Solution:
    def longestNiceSubarray(self, nums):
        mask = 0
        left = 0
        ans = 0

        for right in range(len(nums)):
            while mask & nums[right]:
                mask ^= nums[left]
                left += 1

            mask |= nums[right]

            ans = max(ans, right - left + 1)

        return ans
