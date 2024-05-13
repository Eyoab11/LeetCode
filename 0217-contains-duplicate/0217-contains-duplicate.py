class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = 0
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            if nums[i] < nums[i + 1]:
                pass
            else:
                count = 1 
        return count == 1