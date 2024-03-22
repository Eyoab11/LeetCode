class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_index = 0
        negative_index = 1
        result = [0] * len(nums)
        
        for num in nums:
            if num > 0:
                result[positive_index] = num
                positive_index += 2
            else:
                result[negative_index] = num
                negative_index += 2
        
        return result