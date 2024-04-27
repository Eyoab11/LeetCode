class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        count = 0
        for i in range(n // 3, n, 2): 
            count += piles[i]
        return count