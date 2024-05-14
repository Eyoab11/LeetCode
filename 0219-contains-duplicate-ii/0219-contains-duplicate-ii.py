class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx = {}  
        for i, num in enumerate(nums):
            if num in idx and abs(i - idx[num]) <= k:
                return True  
            else:
                idx[num] = i  
        
        return False 