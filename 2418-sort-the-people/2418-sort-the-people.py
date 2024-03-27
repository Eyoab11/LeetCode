class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nums = list(range(len(heights)))
        nums.sort(key=lambda i: -heights[i])
        return [names[i] for i in nums]