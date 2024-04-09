class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            x, y = points[i]
            dist = math.sqrt(x**2 + y**2)
            points[i].append(dist)
        points.sort(key = lambda x:x[2])
        ans = []
        for i in range(k):
            ans.append([points[i][0], points[i][1]])
        return ans