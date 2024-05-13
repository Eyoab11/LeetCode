class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  
        left = 0
        right = x
        while left < right:
            middle_num = left + (right - left ) //2
            if middle_num **2 <= x:
                left = middle_num + 1
            else:
                right = middle_num
                
        return left-1
                