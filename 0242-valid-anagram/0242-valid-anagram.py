class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        tt = sorted(t)
        return ss == tt
        
                
                