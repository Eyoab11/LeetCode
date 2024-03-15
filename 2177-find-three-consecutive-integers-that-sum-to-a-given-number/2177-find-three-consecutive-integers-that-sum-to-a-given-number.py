class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        result = []
        if (num//3)-1 + (num//3) + (num//3)+1 == num:
            result = [(num//3)-1, (num//3), (num//3)+1]
        return result