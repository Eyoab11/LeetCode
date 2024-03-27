class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n - 1):
            last = i
            for j in range(i + 1, n):
                if heights[j] > heights[last]:
                    last = j
            names[i], names[last] = names[last], names[i]
            heights[i], heights[last] = heights[last], heights[i]
        return names