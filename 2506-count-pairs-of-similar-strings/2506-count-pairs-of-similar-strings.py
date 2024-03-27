class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        num = len(words)
        for i in range(num):
            for j in range(i+1, num):
                if set(words[i]) == set(words[j]):
                    count += 1
        return count
        