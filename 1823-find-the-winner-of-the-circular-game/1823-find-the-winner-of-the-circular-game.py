class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        list_of_friends = list(range(1, n + 1))
        start = 0
        while len(list_of_friends) > 1:
            removing = (start + k - 1) % len(list_of_friends)
            list_of_friends.pop(removing)
            start = removing % len(list_of_friends)
        return list_of_friends[0]