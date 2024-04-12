class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_ = float('inf')
        start=0
        window_sum=0
        for end in range(len(nums)):
            window_sum+=nums[end]
            while window_sum>=target:
                min_=min(min_,end-start+1)
                window_sum-=nums[start]
                start+=1
        return min_ if min_ != float('inf') else 0