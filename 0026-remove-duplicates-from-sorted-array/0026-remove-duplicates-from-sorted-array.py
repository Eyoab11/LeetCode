class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = set()
        nxt = 0
        for i in nums:
            if i not in k:
                k.add(i)
                nums[nxt] = i
                nxt += 1
        return nxt