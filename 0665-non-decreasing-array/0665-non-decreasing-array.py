class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
            counter = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i] > nums[i + 1]:
                    counter += 1
                    if counter > 1:
                        return False
                    if i > 0 and nums[i - 1] > nums[i + 1]:
                        nums[i + 1] = nums[i]
                    else:
                        nums[i] = nums[i + 1]
                else:
                    i += 1
            return True