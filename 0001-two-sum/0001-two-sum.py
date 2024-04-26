class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(enumerate(nums), key=lambda x: x[1])
        left, right = 0, len(nums_sorted) - 1
        while left < right:
            current_sum = nums_sorted[left][1] + nums_sorted[right][1]
            
            if current_sum == target:
                return [nums_sorted[left][0], nums_sorted[right][0]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []