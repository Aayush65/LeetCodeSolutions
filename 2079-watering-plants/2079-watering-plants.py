class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        water = capacity
        for i in range(len(plants)):
            steps += 1
            if water < plants[i]:
                steps += 2 * i
                water = capacity
            water -= plants[i]
        return steps