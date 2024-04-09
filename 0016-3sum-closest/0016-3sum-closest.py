class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() 
        closest = float('inf') 
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current = nums[i] + nums[left] + nums[right] 
                if abs(current - target) < abs(closest - target):
                    closest = current
                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return target
        return closest