class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, max_ = 0, 0
        for i, n in enumerate(nums):
            k -= (1 - n)
            if k < 0:
                k += (1 - nums[left])
                left += 1
            max_ = max(max_, i - left + 1)
        return max_
