class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        max_value = total / k
        
        left = 0
        right = k
        while right < len(nums):
            total -= nums[left]
            total += nums[right]
            max_value = max(max_value, total / k)
            left += 1
            right += 1
            
        return max_value
        