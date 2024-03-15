class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        temp_step = 0
        amount = capacity

        for i in range(len(plants)):
            if amount >= plants[i]:
                amount -= plants[i]
                temp_step += 1
            else:
                temp_step += (2*i) + 1
                amount = capacity  
                amount -= plants[i]

        return temp_step