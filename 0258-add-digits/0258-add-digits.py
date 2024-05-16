class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum_ = 0
            while num > 0:
                sum_ += num % 10
                num //= 10
            num = sum_  
        return num  
