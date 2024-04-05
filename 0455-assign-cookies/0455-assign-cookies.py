class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        left = 0
        right = 0
        
        while left < len(g) and right < len(s):
            
            if s[right] >= g[left]:
                count+= 1
                left+=1
            right+=1
            
        return count
                
            