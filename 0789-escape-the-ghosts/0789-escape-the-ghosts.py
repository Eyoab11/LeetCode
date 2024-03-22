class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        destination = abs(target[0]) + abs(target[1])
    
        for i in ghosts:
            are_equal = abs(target[0] - i[0]) + abs(target[1] - i[1])
            if are_equal <= destination:
                return False
            
        return True

