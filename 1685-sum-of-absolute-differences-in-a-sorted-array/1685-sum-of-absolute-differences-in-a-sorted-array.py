class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixSum = [0] * (n + 1) 
        res = []
        for i, num in enumerate(nums):
            prefixSum[i + 1] = prefixSum[i] + num
        for i, num in enumerate(nums):
            res.append((i * num - prefixSum[i]) + prefixSum[n] - prefixSum[i] - (n - i) * num)

        return res